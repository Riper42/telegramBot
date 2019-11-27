import telebot
import time
import os
import random
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Привет " + message.chat.first_name + "\nКак у тебя дела?")

@bot.message_handler(content_types=['text'])
def send_message(message):
    #####################################
    if message.text == message.text:    #
        print(message.chat.first_name + ":" + message.text)             #
       # print(message.chat)             #
    #####################################
    if "привет" in message.text.lower() or "hi" in message.text.lower() or "hello" in message.text.lower() or "howdy" in message.text.lower():
        bot.send_message(message.chat.id, "Привет " + message.chat.first_name+ "\nКак у тебя дела?")

    elif "норм" in message.text.lower() or "хорош" in message.text.lower() or "отлично" in message.text.lower() or "плохо" in message.text.lower():
        smile = ""
        if "норм" in message.text.lower():
            smile = "🙂"
        elif "хорош" in message.text.lower():
            smile = random.randint(0,2)
            if smile == 1:
                smile = "😄"
            elif smile == 0:
                smile = "😆"
            elif smile == 2:
                smile = "☺"
        elif "отлично" in message.text.lower():
            smile = "😊"
        elif "плохо" in message.text.lower():
            smile = random.randint(0,1)
            if smile == 1:
                smile = "😞"
            elif smile == 0:
                smile = "😔"

        bot.send_message(message.chat.id, "Если у вас " + message.text + " значит и у меня " + message.text + str(smile))
    elif "фото" in message.text.lower():
        bot.send_message(message.chat.id, message.chat.photo + "Фото ")

    elif "какдела" in message.text.lower():
        bot.send_message(message.chat.id, "Зависит от вас, а у вас как дела?")
###/////
    elif "спокойнойночи" in message.text.lower() and time.strftime("%H") >= "21" and time.strftime("%H") < 4 or "добройночи" in message.text.lower() and time.strftime("%H") >= "21":
###/////
        bot.send_message(message.chat.id, "И тебе спокойной ночи " + message.chat.first_name + " 😘❤")

    elif message.text.lower() == "спокойной ночи" and time.strftime("%H") < "21":
        bot.send_message(message.chat.id, "Чего так рано?\nСейчас же только " + time.strftime("%H:%M"))
    elif message.text.lower() == "сколько сейчас время" or message.text.lower() == "сколько сейчас время?" or message.text.lower() == "сколько время?" or message.text.lower() == "сколько время" or  message.text.lower() == "время":
        bot.send_message(message.chat.id, time.strftime("%H:%M"))
###Данная часть кода нужна для работы с data файлом для дальнейших модификаций данного бота~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #  elif message.text == "Update":
  #      os.system("rm -rf data.txt && > data.txt")
  #      bot.send_message(message.chat.id, "data.txt успешно обновлен")

   # elif message.text == "Случайное число" or message.text == "случайное число" or message.text == "Пришли случайное число" or message.text == "пришли случайное число" or message.text == "Рандомное число" or message.text == "random" or message.text == "Random" or message.text == "рандомное число" or message.text == "Пришли рандомное число" or message.text == "пришли рандомное число":
      #  bot.send_message(message.chat.id, "Введите до какого числа")
    #elif message.text == message.text:
     #   int2 = int(message.text)
        #bot.send_message(message.chat.id, int1)
      #  bot.send_message(message.chat.id, random.randint(1, int2))


    else:
        os.system("echo " + str(time.strftime("%H:%M  %x     ")) + "[" + str(message.chat.first_name) + ": " + str(message.text) + "] >> data.txt")
        bot.send_message(message.chat.id, "Я не знаю как отреагировать на это сообщение, данные о вас и сообщении занесены в базу данных, для дальнейшего подифицирования данного бота.\nЗа подробной информацией пишите @tmeeeeeeeeeeee он ваc прокансультирует)")



bot.polling( none_stop = True )
