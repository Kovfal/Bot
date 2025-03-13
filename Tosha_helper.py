import telebot
import config
from telebot import types

Tosha = telebot.TeleBot(config.token())


@Tosha.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать цены на услуги")
    btn2 = types.KeyboardButton("Записаться")
    btn3 = types.KeyboardButton("Приобрести средства для ухода")
    markup.add(btn1, btn2, btn3)
    Tosha.send_message(message.chat.id, text="Приветствую, {0.first_name}! Я бот-консультант для записи, пожалуйста, выберите интересующую Вас категорию.".format(message.from_user), reply_markup=markup)

@Tosha.message_handler(content_types=['text'])
def start(message):
    if (message.text == "Узнать цены на услуги"):
        Tosha.send_message(message.chat.id, text=config.PRIS.format(message.from_user))
    elif (message.text == "Записаться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Окрашивание")
        button2 = types.KeyboardButton("Стрижка")
        button3 = types.KeyboardButton("Мытье головы")
        button4 = types.KeyboardButton("Консультация")
        button5 = types.KeyboardButton("Назад")
        markup.add(button1, button2, button3, button4, button5)
        Tosha.send_message(message.chat.id, "Выберите услугу".format(message.from_user), reply_markup=markup)

    elif (message.text == "Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Узнать цены на услуги")
        btn2 = types.KeyboardButton("Записаться")
        btn3 = types.KeyboardButton("Приобрести средства для ухода")
        markup.add(btn1, btn2, btn3)
        Tosha.send_message(message.chat.id, text="Вы вернулись в главное меню.".format(message.from_user), reply_markup=markup)

    elif (message.text == 'Приобрести средства для ухода'):
        Tosha.send_message(message.chat.id, "В работе!!!")

Tosha.polling(none_stop=True, interval=0)
