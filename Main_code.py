# pip install aiogram 
import telebot
import asyncio
from gtts import gTTS
from aiogram import Bot, Dispatcher, types
#from playsound import playsound

token = "Место для вашего токена"
#language = 'ru'

bot = telebot.TeleBot(token)
#dp = Dispatcher(bot)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Напиши мне текст и я переведу его в аудио!".format(message.from_user))

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/eng - озвучка на английском языке\n/rus - озвучка на русском языке")

@bot.message_handler(commands=['rus'])
def start(message):
    bot.send_message(message.chat.id, "Напиши текст, я сделаю аудио на русском")
    
@bot.message_handler(content_types = ['text'])
def send_songs(message):
    text_val = message.text
    obj = gTTS(text = text_val, lang='ru', slow = False)
    obj.save('Расположение сохраненного файла')

    audio = open('Расположение сохраненного файла', 'rb')
    bot.send_voice(message.chat.id, voice=audio)
#    audio.close()

bot.polling (none_stop = True)       # отправка запроса на сервер
