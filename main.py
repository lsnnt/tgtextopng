import telebot
import requests
from env import TOKEN

# Token for the bot
bot = telebot.TeleBot(TOKEN)
def latex_to_png(code, file):
    response = requests.get('https://latex.codecogs.com/png.latex?\dpi{300} \large %s' % code)
    with open(file, 'wb') as f:
    	f.write(response.content)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! Send me a LaTeX code and I will convert it to a PNG image.")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    latex_to_png(message.text, 'latex.png')
    photo = open('latex.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    # photo.close()

bot.polling()

# Path: requirements.txt
