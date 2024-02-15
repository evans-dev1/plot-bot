
Телеграм-бот для построения графиков @plot13bot
 
Цель работы: Создать Телеграм-бота для эффективного и простого построения графиков.
Задачи: Исследовать технологии разработки ботов для Telegram, инструменты визуализации графиков. Сопоставить готовый проект с конкурентами на современном рынке. Запустить программу на постоянную работу.
Этапы исследования: Сначала были написаны программа для построения графиков и сохранения их в виде изображения и основа бота, затем они были соединены. Разработаны дополнительные функции, особенности, позволяющие более гибко и удобно решать поставленные задачи.
Методы исследования и оборудование: 
Язык программирования: Python 3.10
Среда разработки: PyCharm Professional
Хостинг: Oracle Corporation
Исправление ошибок: При попытке соединения функции для построения графиков с основой бота возникла проблема с работой программы. Она постоянно останавливалась с ошибкой. Из текста ошибки стало ясно, что она была связана с особенностями получения сообщений в библиотеке. В процессе поиска решения этой проблемы я зашел на Github разработчика библиотеки telebot, где нашел параметр threated, отвечающий за алгоритм обработки запросов ботом. Изменив параметр threated на False удалось исправить эту ошибку. 
Результаты: В результате работы над проектом был создан телеграм-бот, который может строить графики разных функций, а также менять их внешний вид. Программа прошла несколько этапов тестирования, в ходе которых были обнаружены и быстро исправлены некоторые недостатки. В настоящее время программа запущена на хостинге и работает круглосуточно.
Сравнение с аналогами: На современном рынке есть аналоги только в виде сайтов или отдельных приложений. В связи с этим, работа с ними может быть не очень быстрой и простой, на сайтах есть рекламные баннеры, а специальные приложения нужно загружать. Использование для работы проекта мессенджера Telegram обеспечивает удобное взаимодействие с ботом на любом устройстве.
Перспективы проекта: Написанный бот может быть полезным инструментом для бизнеса, особенно при анализе данных. Предполагается дальнейшее совершенствование и развитие проекта: расширение функционала, например, возможность изменять параметры цвета и толщины линий, чтобы сделать анализ более удобным.
