import os
import telebot
from telebot import types
import numpy as np
import matplotlib.pyplot as plt


class PlotBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token, parse_mode=None)
        self.kind = None
        self.X, self.Y = None, None
        self.x_name, self.y_name = None, None
        self.title = "График без названия"
        self.register_handlers()

    def register_handlers(self):
        self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.bot.message_handler(regexp=r'столб|линия|круг')(self.kind_plot)
        self.bot.message_handler(regexp=r'x_values:')(self.x_axis_values)
        self.bot.message_handler(regexp=r'y_values:')(self.y_axis_values)
        self.bot.message_handler(commands=['title'])(self.ask_title)
        self.bot.message_handler(commands=['plot'])(self.domeaplot)
        self.bot.message_handler(func=lambda m: True)(self.echo_all)

    def send_welcome(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Столбчатая диаграмма')
        itembtn2 = types.KeyboardButton('График-линия')
        itembtn3 = types.KeyboardButton('Круговая диаграмма')
        markup.add(itembtn1, itembtn2, itembtn3)
        self.bot.reply_to(message, "Привет! Через этого бота можно построить какой-нибудь график. Вот небольшая инструкция:\n\n"
                                   "1. Отправь данные по оси X. Пример: `X_values: Год, 2000, 2001, 2002`\n"
                                   "2. Отправь данные по оси Y. Пример: `Y_values: Продажи, 100, 200, 150`\n"
                                   "3. Отправь команду /title, затем, следующим сообщением, введи название графика\n"
                                   "4. Напиши команду /plot или нажми на одну из кнопок. Бот выдаст готовый график",
                          reply_markup=markup, parse_mode='markdown')

    def kind_plot(self, message):
        self.kind = message.text.lower().split(" ")[0]
        self.bot.reply_to(message, "Вся информация успешно проверена. Напиши /plot для отрисовки данных.")

    def x_axis_values(self, message):
        try:
            values = np.array(message.text.split(":")[1].split(","))
            self.X = values[1:]
            self.x_name = values[0]
            self.bot.reply_to(message, "Данные успешно записаны.")
        except:
            self.bot.reply_to(message, "Ошибка, что-то введено не в том формате.")

    def y_axis_values(self, message):
        try:
            values = np.array(message.text.split(":")[1].split(","))
            self.Y = np.array(values[1:], dtype=np.float64)
            self.y_name = values[0]
            self.bot.reply_to(message, "Данные успешно записаны.")
        except:
            self.bot.reply_to(message, "Ошибка, что-то введено не в том формате")

    def ask_title(self, message):
        answer = self.bot.reply_to(message, "Введите название графика:")
        self.bot.register_next_step_handler(answer, self.add_title)

    def add_title(self, message):
        self.title = str(message.text)
        self.bot.reply_to(message, "Название успешно установлено.")

    def domeaplot(self, message):
        try:
            if self.kind == "столбчатая":
                plt.figure(figsize=(8, 4.5))
                y_pos = np.arange(len(self.X))
                plt.bar(y_pos, self.Y, align="center", alpha=0.55, edgecolor="black", color=(0.1, 0.2, 0.7))
                plt.xticks(y_pos, self.X)
                plt.ylabel(self.y_name)
                plt.xlabel(self.x_name)
                plt.title(self.title)
                plt.savefig("last_plot.png")
            if self.kind == "график-линия" or not self.kind:
                plt.figure(figsize=(8, 4.5))
                plt.plot(self.X, self.Y, alpha=0.7, c="#bf280a")
                plt.scatter(self.X, self.Y, alpha=0.7, c="#bf280a")
                plt.ylabel(self.y_name)
                plt.xlabel(self.x_name)
                plt.title(self.title)
                plt.savefig("last_plot.png")
            if self.kind == "круговая":
                fig1, ax1 = plt.subplots(figsize=(8, 4.5))
                ax1.pie(self.Y, labels=self.X, autopct='%1.1f%%',
                        shadow=False, startangle=90)
                ax1.axis('equal')
                plt.title(self.title, bbox={'facecolor': '1', 'pad': 6})
                plt.savefig("last_plot.png")
            self.bot.send_photo(message.chat.id, photo=open('last_plot.png', 'rb'))
            os.remove('last_plot.png')
        except Exception as e:
            print(e)
            self.bot.reply_to(message, "Ошибка, что-то введено не в том формате")

    def echo_all(self, message):
        self.bot.reply_to(message, "Для начала работы с ботом используйте /start.")

    def run(self):
        self.bot.polling()


if __name__ == "__main__":
    bot = PlotBot("6895763742:AAHMCA3OQNDtasldzwfInnc8lDPO5DPO5Dk")
    bot.run()
