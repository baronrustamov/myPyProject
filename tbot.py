# -*- coding: cp1251 -*-

import random
import telebot
from telebot import types

bot = telebot.TeleBot('251180362:AAG2Y1VTSazHOoEFhFmJVpnhvnc5GiqEQq0')

#keyboard1 = telebot.types.ReplyKeyboardMarkup()
#keyboard1.row('������', '����', '� ���� �����')

# ��������� ��� ��� �����������
first = ["������� � ��������� ���� ��� ����� ���������.","����������� ���� ��� ����, ����� �������� �� ������ ��������!","������ ���������, ������� ����� ����� �������� �� ���� ���������� ���������.","������ ����� ��� ����, ����� ������ ����� ��������� ��� ����������� �� �������.","������������ ���� ��� ����, ����� ����������� � ������������� ������."]
second = ["�� �������, ��� ���� � ���� ������ ����� �� �������� ���","���� ������� �� �����, ������� ��������� ���","��, ��� ������� ������� ��������� ��������� ���, ������ ������� ���","���� � ��� ������ ���, �������� �������� ��","�������, ��� ����� �����������, � ������ ��� � ������� ��� ����� ��������� ������ ���"]
second_add = ["��������� � �������� � ��������.","������ � ������� �������, ������� ����� ��� �������� �������� ������.","���� � ��� ��������, ����� � ������ �������� ������ �������.","������� ������� � �������� ��, ������� �� �� �������� �����.","�����, ����� �� ���������� ���� � ��������� ������ � ����� ������."]
third = ["���� ����� ����� �������� ��� ��������, �� ������� �� ������� �� �����.","������, ��� ����� ���������� ������ �����������, ������� ��������� ���� ���� ���������� ����.","���� ���� �� �� ������� ��������� ������� ������������� ��������, �� ���� �� �������� ���� �� �����.","�� ����� ������� �������� ������ � ������� �� ����� �����, ����� ��� ������ ������.","���� ��������� ���������� �� ���� � �������� �������, � ����� ��� ������� ������� ��� �������� �������."] # �����, ������� �������� ��������� � ������������ �� @

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # ���� �������� �������
    if message.text == "������":
        #����� �����������
        bot.send_message(message.from_user.id, "������, ������ � �������� ���� �������� �� �������.")
        # ������� ������
        keyboard = types.InlineKeyboardMarkup()
        # �� ������� ������� ����� � ���������� ��� ������� ����� �������
        key_oven = types.InlineKeyboardButton(text='����', callback_data='zodiac')
        # � ��������� ������ �� �����
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='�����', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='��������', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='���', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='���', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='����', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='����', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='��������', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='�������', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='�������', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='�������', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='����', callback_data='zodiac')
        keyboard.add(key_ryby)
        # ���������� ��� ������ ����� � ����� ��������� � ������
        bot.send_message(message.from_user.id, text='������ ���� ���� �������', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "������ ������")
    else: bot.send_message(message.from_user.id, "� ���� �� �������. ������ /help.")
    # ���������� ������� �� ������

# ���������� ������� �� ������
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # ���� ������ �� ���� �� 12 ������ � ������� ��������
    if call.data == "zodiac":
        #��������� ��������
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # ���������� ����� � ��������
        bot.send_message(call.message.chat.id, msg)

print("Starting bot")

'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '������, �� ������� ��� /start', reply_markup=keyboard)
    print('start message ok')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '������':
        bot.send_message(message.chat.id, '������, ��� ���������')
    elif message.text.lower() == '����':
        bot.send_message(message.chat.id, '������, ���������')
    elif message.text.lower() == '� ���� �����':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
'''

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

#bot.polling(none_stop=True, interval=0)
bot.polling()