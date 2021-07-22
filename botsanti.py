#!/usr/bin/en python3
# -*- coding: utf-8 -*
import telegram
import os, sys                # Basic python libraries
import os.path as path 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext

INPUT_TEXT = 0

#variables
ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA, SALIDA = range(7) 

def start(update, context):
    main_menu = [[InlineKeyboardButton("Artesania", callback_data='artesania'),
                 InlineKeyboardButton("Carpinteria", callback_data='carpiteria')],
                [InlineKeyboardButton("Costura", callback_data='costura'),
                 InlineKeyboardButton("Decoraciones", callback_data='decoraciones')],
                [InlineKeyboardButton("Muebleria", callback_data='muebleria'),
                 InlineKeyboardButton("Tapiceria", callback_data='tapiceria')],
                [InlineKeyboardButton("Salida", callback_data='salida')]]
    reply_markup = InlineKeyboardMarkup(main_menu)
    update.message.reply_text(text='Hola, bienvenido a Muebleria Santi\n\nUsa "/" para interactuar con los Comandos o use los Botones del Bot',
                              reply_markup=reply_markup)   
    #return MUEBLERIA       

def menu_actions(update, context):
    query = update.callback_query
    if query.data =='artesania':
        menu_1 = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
                  [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')]]
        reply_markup = InlineKeyboardMarkup(menu_1)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text='Choose the option:',
                              reply_markup=reply_markup)

    elif query.data == 'muebleria':
        m_muebleria = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
        reply_markup = InlineKeyboardMarkup(m_muebleria)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text='Elige el modelo:',
                              reply_markup=reply_markup)
        print(query.data)

def muebleria(update, context):
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text='Elige el modelo:',
                              reply_markup=reply_markup)
    #return start


# def muebleria_callback(update, context):
#     query = update.callback_query
#     if query.data == 'MUEBLERIA':
#         a = muebleria
#         print(a)


if __name__ == "__main__":
    updater = Updater(token='1630057239:AAGno5APPSjhkE8_S4AV56EpUAH51CTCQVY', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('muebleria', muebleria))

    #dp.add_handler(CallbackQueryHandler(muebleria, pattern='muebleria' + str(MUEBLERIA) + '$'))

    dp.add_handler(CallbackQueryHandler(menu_actions, pattern='menu_actions'))
    dp.add_handler(CallbackQueryHandler(menu_actions, pattern='muebleria'))

    

    updater.start_polling(allowed_updates=[])
    updater.idle()


