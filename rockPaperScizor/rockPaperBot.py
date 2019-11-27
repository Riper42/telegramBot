import telebot
import os
from random import randint

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет" + message.chat.first_name +  "не хочешь поиграть в камень-ножницы-бумага?", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower == "да":
        bot.send_message(message.chat.id, 'Begin', reply_markup=keyboard)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
   
    rock = "Камень 🗻"
    paper = "Бумага 📄"
    scisor = "Ножницы ✂"
    key_rock = telebot.types.KeyboardButton(text = rock)
    key_paper = telebot.types.KeyboardButton(text = paper)
    key_scisor = telebot.types.KeyboardButton(text = scisor)
    
    keyboard.add(key_rock, key_scisor,key_paper)
    enemy = randint(1,3)
    if enemy == 1:
        enemy = rock
    elif enemy == 2:
        enemy = paper
    elif enemy == 3:
        enemy = scisor
    else:
        print("error")

    #if message.text == "Камень":
    #    bot.send_message(message.chat.id,"1" ,reply_markup=keyboard)
    #elif message.text == "Ножницы":
    #    bot.send_message(message.chat.id,"2" ,reply_markup=keyboard)
    #elif message.text == "Бумага":
    #    bot.send_message(message.chat.id,"3" ,reply_markup=keyboard)

    if enemy == message.text:
        bot.send_message(message.chat.id, "Ничья:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    elif enemy == rock and message.text == scisor:
        bot.send_message(message.chat.id, "Вы проиграли:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    elif enemy == rock and message.text == paper:
        bot.send_message(message.chat.id, "Вы выиграли:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    elif enemy == scisor and message.text == rock:
        bot.send_message(message.chat.id, "Вы выиграли:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    elif enemy == scisor and message.text == paper:
        bot.send_message(message.chat.id, "Вы проиграли:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    elif enemy == paper and message.text == rock:
        bot.send_message(message.chat.id, "Вы проиграли:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    elif enemy == paper and message.text == scisor:
        bot.send_message(message.chat.id, "Вы выиграли:\nСоперник(" + enemy + ") Вы(" + message.text + ")",reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Сделайте свой выбор👇", reply_markup=keyboard)
    print(message.chat.first_name + ": " + message.text + "\n" + "Raspberry: " + enemy + "\n\n\n" )


bot.polling( none_stop = True )
