import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Привет я бот который анонимно присылает сообщение моему хозяйну @tmeeeeeeeeeeee ты можешь задать любой вопрос😉")

@bot.message_handler(content_types=["text"])
def send_message(message):

    #bot.send_message(message.chat.id, message.text)
    if message.text == message.text:
        bot.send_message(message.chat.id, "Ваше сообщение было анонимно отправлено @tmeeeeeeeeeeee")
        bot.send_message(611175832, "Аноним: " + message.text)





bot.polling( none_stop = True )
