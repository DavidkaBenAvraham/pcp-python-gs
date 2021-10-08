
import config
import telebot
import os
import datetime
import main



bot = telebot.TeleBot('1346001134:AAFBJwqF9kFrOYgVLxJshtN6cQzwwB8mLBM')

#bot.delete_webhook()

print(bot.get_me())
''' @onla = -1001479849890 ]'''
chat = bot.get_chat('@onela')

print(f'''\tab chat - {chat} ''')
print(f''' bot.get_chat(-1001479849890) {bot.get_chat(-1001479849890)} ''')
print(f''' bot.send_message(-1001479849890 , 'test') - {bot.send_message(-1001479849890 , 'test')} ''')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['get_commands'])
def get_commands(message):
    print(message)
    commands = bot.get_my_commands(None,None)
    bot.reply_to(message, str(commands))

@bot.message_handler(commands=['get_last_order'])
def get_last_order(message):
    print(message)
    last_order = main.get_last_order_from_manoa()
    bot.reply_to(message, last_order)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text + '}I{')

bot.polling()