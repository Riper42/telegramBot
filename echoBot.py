import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Приветственное сообщение")

@bot.message_handler(content_types=["text"])
def send_message(message):

    #bot.send_message(message.chat.id, message.text)
    if message.text == "Hi":
        bot.send_message(message.chat.id, "howdy" )





bot.polling( none_stop = True)
