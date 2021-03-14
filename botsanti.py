#!/usr/bin/en python3
# -*- coding: utf-8 -*
import telegram
import os, sys                # Basic python libraries
import os.path as path 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler

INPUT_TEXT = 0

#variables
ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA, SALIDA = range(7) 

def start(update, context):
  
    keyboard = [[InlineKeyboardButton("Artesania", callback_data='1'),
                 InlineKeyboardButton("Carpinteria", callback_data='2')],
                [InlineKeyboardButton("Costura", callback_data='3'),
                 InlineKeyboardButton("Decoraciones", callback_data='4')],
                [InlineKeyboardButton("Muebleria", callback_data='5'),
                 InlineKeyboardButton("Tapiceria", callback_data='6')],
                [InlineKeyboardButton("Salida", callback_data='7')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text='Hola, bienvenido a Muebleria Santi\n\nUsa los Comandos para interactuar con el Bot',
                              reply_markup=reply_markup)              

def muebleria(update, context):
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='1'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='2')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='3'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='4')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='5'),
                 InlineKeyboardButton("Puff Redondos", callback_data='6')],
                [InlineKeyboardButton("Salida", callback_data='7')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text='Elige el modelo:',
                              reply_markup=reply_markup)


def button(update, context):

    # if value =="1":
    #     requests.post('https://api.telegram.org/bot<1630057239:AAEZpaEWBKkyVOwQRf9pwHwZBmJmFIJ-VLI>/sendPhoto',
    #           files={'photo': (<ARCHIVO>, open(<ARCHIVO>, 'rb'))},
    #           data={'chat_id': <CHAT_ID>, 'caption': <TEXT>})



if __name__ == "__main__":
    updater = Updater(token='1630057239:AAEZpaEWBKkyVOwQRf9pwHwZBmJmFIJ-VLI', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    #dp.add_handler(CommandHandler('muebleria', muebleria))

    

    updater.start_polling()
    updater.idle()


