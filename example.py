import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Приветственное сообщение")

@bot.message_handler(content_types=["text"])
def send_message(message):

    #bot.send_message(message.chat.id, message.text)
    if "привет" in message.text.lower() or "хола" in message.text.lower():
        bot.send_message(message.chat.id, "howdy" )
    elif "one" in message.text.lower() or "two" in message.text.lower():
        bot.send_message(message.chat.id, "one or two")
    else:
        bot.send_message(message.chat.id, "fuck you")





bot.polling( none_stop = True)
