import telebot
import os

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello nigga")

@bot.message_handler(content_types=["text", "video"])
def send_message_video(message):
    if True:
        video = open('YVideo/a.mp4', 'rb')
        os.system("cd /data/data/com.termux/files/home/backup/dev/py/teleBot/download_videoYoutube_bot/YVideo && youtube-dl " + message.text)
        os.system("rename -o YVideo/* a.mp4 YVideo/*")
        os.system("cd ..")
        bot.send_message_video(message.chat.id, video)
        os.system("rm -rf YVideo/*")


bot.polling( none_stop = True )
