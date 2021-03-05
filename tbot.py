import telebot

bot = telebot.TeleBot('251180362:AAG2Y1VTSazHOoEFhFmJVpnhvnc5GiqEQq0')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()