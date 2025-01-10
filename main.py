from config import *
from logic import *
import telebot
from telebot import types
from datetime import datetime
import schedule
import time
import threading
from pytz import timezone

bot = telebot.TeleBot(TOKEN)
mata = []
domz = []
novv = []
raspiska = {"понедельник": "2024-12-13_20-58-03.png", "вторник": "2024-12-13_20-58-0.png", "среда": "2024-12-13_20-58-01.png", "четверг": "2024-12-13_20-58-02.png", "пятница": "2024-12-13_20-58-00.png"}
raspisanie = Rasptsania(raspiska=raspiska)
markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn2 = types.KeyboardButton('/расписание')
btn1 = types.KeyboardButton('/журнал')
btn3 = types.KeyboardButton('/дз')
btn4 = types.KeyboardButton('/новости')
markup.add(btn2, btn1, btn3, btn4)
a = "0"
# создаём клавиатуру
    
# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Здравствуйте! Я бот для класса.""", reply_markup=markup)
    del mata[:]

        

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """Привет, нажимай на кнопки снизу для выбора :)""", reply_markup=markup)

@bot.message_handler(commands=['журнал'])
def send_welcome(message):
    tup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn4 = types.KeyboardButton('не смогу прийти')
    btn5 = types.KeyboardButton('журнал кто не придёт')
    btn9 = types.KeyboardButton('назад')
    tup.add(btn4,btn5,btn9)
    bot.send_message(message.chat.id, 'Выберете причину:', reply_markup=tup)

@bot.message_handler(commands=['дз'])
def send(message):
    dz = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn14 = types.KeyboardButton('всё дз')
    btn13 = types.KeyboardButton('руководство по дз')
    btn9 = types.KeyboardButton('назад')
    dz.add(btn14,btn13,btn9)
    bot.reply_to(message, 'Выберайте:', reply_markup=dz)
@bot.message_handler(commands=['добавить_дз'])
def send(message):
    if message.from_user.username == 'Semen_Akzamov' or 'Lyubovnik81' or 'naaastiks52' or 'mila_9027':
        zapros = message.text.split(maxsplit=1)[1]
        domz.append(zapros)
        bot.reply_to(message, "Вы успешно добавили дз!", reply_markup=markup)
    else:
        bot.reply_to(message, "У вас недостаточно прав!", reply_markup=markup)
@bot.message_handler(commands=['новости'])
def send(message):
    nv = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn14 = types.KeyboardButton('все новости')
    btn13 = types.KeyboardButton('руководство по новостям')
    btn9 = types.KeyboardButton('назад')
    nv.add(btn14,btn13,btn9)
    bot.reply_to(message, 'Выберайте:', reply_markup=nv)
@bot.message_handler(commands=['добавить_нв'])
def send(message):
    if message.from_user.username == 'Semen_Akzamov' or 'Lyubovnik81' or 'naaastiks52' or 'mila_9027':
        zapros = message.text.split(maxsplit=1)[1]
        novv.append(zapros)
        bot.reply_to(message, "Вы успешно добавили нв!", reply_markup=markup)
    else:
        bot.reply_to(message, "У вас недостаточно прав!", reply_markup=markup)
@bot.message_handler(commands=['clear_dz'])
def send(message):
    if message.from_user.username == 'Semen_Akzamov' or 'Lyubovnik81' or 'naaastiks52' or 'mila_9027':
        del domz[:]
    else:
        bot.reply_to(message, "У вас недостаточно прав!", reply_markup=markup)
    bot.reply_to(message, "Вы успешно удалили дз!", reply_markup=markup)
@bot.message_handler(commands=['расписание'])
def send_ras(message):
    mar = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn3 = types.KeyboardButton('понедельник')
    btn4 = types.KeyboardButton('вторник')
    btn5 = types.KeyboardButton('среда')
    btn6 = types.KeyboardButton('четверг')
    btn7 = types.KeyboardButton('пятница')
    btn8 = types.KeyboardButton('всё расписание')
    btn10 = types.KeyboardButton('расписание звонков')
    btn9 = types.KeyboardButton('назад')
    mar.add(btn3,btn4,btn5,btn6,btn7,btn8,btn10,btn9)
    bot.send_message(message.chat.id, 'Выберите вид:', reply_markup=mar)
@bot.message_handler(commands=['ban'])
def baning(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if message.from_user.username == 'Semen_Akzamov':
            bot.ban_chat_member(message.chat.id, user_id)
        else:
            bot.send_message(message.chat.id, 'У вас нет прав!')
    else:
        bot.send_message(message.chat.id, 'Вы должны ответить на чьёто сообщение!')
@bot.message_handler(commands=['unban'])
def baning(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if message.from_user.username == 'Semen_Akzamov':
            bot.unban_chat_member(message.chat.id, user_id)
        else:
            bot.send_message(message.chat.id, 'У вас нет прав!')
    else:
        bot.send_message(message.chat.id, 'Вы должны ответить на чьёто сообщение!')
@bot.message_handler(commands=['myt'])
def baning(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(message.chat.id, user_id).status
        if user_status == 'administrator' or user_status == 'creator' or message.from_user.username == 'Semen_Akzamov':
            duration = 60 # Значение по умолчанию - 1 минута
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
            bot.restrict_chat_member(message.chat.id, user_id, until_date=time.time()+duration*60)
        else:
            bot.send_message(message.chat.id, 'У вас нет прав!')
    else:
        bot.send_message(message.chat.id, 'Вы должны ответить на чьёто сообщение!')


@bot.message_handler(content_types="text")
def message_reply(message):
    zapros = message.text
    user = message.from_user.username
    user_id = message.from_user.id
    if zapros=="назад":
        bot.send_message(message.chat.id, "Назад", reply_markup=markup)
    elif zapros=="понедельник":
        photo = open(raspisanie.open_raspisanea(day=zapros), 'rb')
        bot.send_photo(user_id, photo, reply_markup=markup)
    elif zapros=="вторник":
        photo = open(raspisanie.open_raspisanea(day=zapros), 'rb')
        bot.send_photo(user_id, photo, reply_markup=markup)
    elif zapros=="среда":
        photo = open(raspisanie.open_raspisanea(day=zapros), 'rb')
        bot.send_photo(user_id, photo, reply_markup=markup)
    elif zapros=="четверг":
        photo = open(raspisanie.open_raspisanea(day=zapros), 'rb')
        bot.send_photo(user_id, photo, reply_markup=markup)
    elif zapros=="пятница":
        photo = open(raspisanie.open_raspisanea(day=zapros), 'rb')
        bot.send_photo(user_id, photo, reply_markup=markup)
    elif zapros=="всё расписание":
        photo = open("2024-12-13_21-19-53.png", 'rb')
        bot.send_photo(message, photo, reply_markup=markup)
    elif zapros=="расписание звонков":
        photo = open("2024-12-16_22-23-29.png", 'rb')
        bot.send_photo(message, photo, reply_markup=markup)
    elif zapros=="не смогу прийти":
        mata.append(user)
        bot.send_message(user_id, "Молодец что сообщил :)", reply_markup=markup)
    elif zapros=="руководство по дз":
        bot.send_message(user_id, "Напишите команду - /добавить_дз, а после напишите дз на урок примерно вот так - /добавить_дз русский упр...", reply_markup=markup)
    elif zapros=="руководство по новостям":
        bot.send_message(user_id, "Напишите команду - /добавить_нв, а после напишите новости примерно вот так - /добавить_нв завтро утренник...", reply_markup=markup)
    if zapros=="журнал кто не придёт":
        if mata == []:
            bot.send_message(message.chat.id, 'В журнале никого пока нет.')
        else:
            bot.send_message(message.chat.id, '\n'.join(map(str, mata)))
    elif zapros=="всё дз":
        if domz == []:
            bot.send_message(message.chat.id, 'Дз нету или его ещё не добавили.')
        else:
            bot.send_message(message.chat.id, '\n'.join(map(str, domz)))
    elif zapros=="все новости":
        if novv == []:
            bot.send_message(message.chat.id, 'Новостей нету или их ещё не добавили.')
        else:
            bot.send_message(message.chat.id, '\n'.join(map(str, novv)))
    

def week_day(chat_id='-1002345184942'):
    while True:
        now = datetime.now()
        today = datetime.today()
        week = datetime.isoweekday(today)
        if now.hour == 15 and now.minute == 0 and now.second == 0:
            today = datetime.today()
            week = datetime.isoweekday(today)
            td = {1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 7: 'понедельник', 5: 'понедельник'}
            photo = open(raspisanie.open_raspisanea(day=td[week]), 'rb')
            bot.send_photo(chat_id, photo, reply_markup=markup)
            bot.send_message(chat_id, 'Как ваши дела?')
        if week == 7 and now.hour == 23 and now.minute == 0 and now.second == 0:
            del novv[:]
            print('дел')
if __name__ == "__main__":
    thread = threading.Thread(target=week_day)
    thread.start()
    bot.polling(none_stop=True)   