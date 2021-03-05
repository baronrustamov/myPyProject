# -*- coding: cp1251 -*-

"""
VladScript
Telegram Bot
Server info
"""

import socket
import hashlib
import os
import time
import calendar  # module of python to provide useful fucntions related to calendar
import datetime  # module of python to get the date and time
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen, ssl, socket
from time import strftime

import random
import telebot
from telebot import types

class Getip:
	def __init__(self):
		wan_ip = self.get_wan_ip()
		lan_ip = self.get_local_ip()
	def get_wan_ip(self):
			w_ip = urlopen('http://ipecho.net/plain').read().decode('utf-8')
			#print("External IP: ", w_ip)
			self.wan_ip = w_ip
			#return w_ip
	def get_local_ip(self):
		try:
			l_ip = (socket.gethostbyname(socket.gethostname()))
			#print("Internal IP: ", l_ip)
			self.lan_ip = l_ip
		except:
			#res.configure(text='Unkown Error', fg='#red')
			self.lan_ip = 'none'

class ServerHealthCheck():
    SHCLog = ""
    def __init__(self, base_url, port, tcp):
        self.base_url = base_url
        self.ip_now = self.obtain_ip()
        self.port = port
        self.tcp = tcp
        self.url_path = self.tcp + "://" + base_url
        self.ping_host()
        #self.obtain_http_info()
        #self.obtain_cert_info()

    def obtain_ip(self):
        print("\n"+"__LOOKUP____________________________________________")
        self.SHCLog = "_____________________LOOKUP_______________________________"+"\n"
        currnet_ip = socket.gethostbyname(self.base_url)
        print("ip: " + currnet_ip)
        self.SHCLog = self.SHCLog + "ip: " + currnet_ip + "\n"
        print("FQDN: " + socket.getfqdn(self.base_url))
        self.SHCLog = self.SHCLog + "FQDN: " + socket.getfqdn(self.base_url) + "\n"
        distinct_ips = []
        # 0,0,0,0  is for (family, type, proto, canonname, sockaddr)
        socket_info = socket.getaddrinfo(self.base_url, 0, 0, 0, 0)
        for result in socket_info:
            ns_ip = result[4][0]
            if distinct_ips.count(ns_ip) == 0:
                distinct_ips.append(ns_ip)
                print(ns_ip)
        distinct_ips = list(set(distinct_ips))
        return currnet_ip

    def ping_host(self):
    # ping reesult
        print("\n" + "__PING INFO____________________________________________")
        self.SHCLog = self.SHCLog + ("\n" + "_____________________PING INFO____________________________________________" + "\n")
        self.SHCLog = self.SHCLog + "Pinging: " + self.ip_now + "\n"
        response = os.system("ping -n 2 " + self.ip_now)
        self.SHCLog = self.SHCLog + "/n"
    #OLD# response = os.system("ping -c 1 " + self.ip_now)
        # and then check the response...
        if response == 0:
            print("\n" + "Server " + self.base_url + ": is up ")
            self.SHCLog = self.SHCLog + "server " + self.base_url + ": is UP " + "\n"
        else:
            print("\n" + "Server " + self.base_url + ": is DOWN !!!")
            self.SHCLog = self.SHCLog + "server " + self.base_url + ": is DOWN !!!" + "\n"

class PrintToConsole():
    def __init__(self, printdata, color):
        self.printdata = printdata
        self.color = color
        self.printincolor()
        print(self.printoutput)
    def printincolor(self):
        if self.color == 'red':
            self.printoutput = bcolors.FAIL + self.printdata + bcolors.ENDC
        else:
            if self.color == 'green':
                self.printoutput = bcolors.OKGREEN + self.printdata + bcolors.ENDC
            else:
                self.printoutput = self.printdata

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() #this statement returns an integer corresponding to the day of the week
    return (calendar.day_name[born]) #this statement returns the corresponding day name to the integer generated in the previous statement


#WhatDay
date = '03 03 2021' #this is the input date
PrintToConsole("Today is: " + findDay(date), "green") # here we print the final output after calling the fucntion findday
#CurrentTime
timestring = strftime('%H:%M:%S %p')
PrintToConsole("Current Time is: " + timestring, "green")

bot = telebot.TeleBot('251180362:AAG2Y1VTSazHOoEFhFmJVpnhvnc5GiqEQq0')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Я тебя люблю')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Помощь', 'Нет', 'Да')

'''
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        #Пишем приветствие
        bot.send_message(message.from_user.id, "Привет.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else: bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        #Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
'''

print("Starting bot")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, "Today is: " + date)
    bot.send_message(message.chat.id, "Current Time is: " + timestring, reply_markup=keyboard1)
    print('start message ok')

@bot.message_handler(commands=['hi'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    print('help message ok')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        print('msg Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
        print('msg Пока')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
        print('msg Love')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)
#bot.polling()