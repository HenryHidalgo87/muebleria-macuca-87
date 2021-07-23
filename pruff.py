#!/usr/bin/en python3
# -*- coding: utf-8 -*
import telegram
import os, sys                # Basic python libraries
import os.path as path 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply , ChatAction
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext, RegexHandler

INPUT_BUTTON, ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA, SALIDA = range(8) 

INPUT_BUTTON = 0

def start(update, context):
    update.message.reply_text(
        text='Hola Bienvenido al Taller de Santi\n\nSelecciona / para la lista de comandos o usa el boton Menu',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Menu', callback_data='menu'),
            InlineKeyboardButton(text='Sobre el Autor', url='https://t.me/henryhidalgo870')]
        ])
    )

def INPUT_BUTTON(update, context):  
    query = update.callback_query
    update.message.reply_text(
        text='Elige la Opcion Deseada:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Artesania", callback_data='artesania'),
             InlineKeyboardButton(text="Carpinteria", callback_data='carpinteria')],
            [InlineKeyboardButton(text="Decoraciones", callback_data='decoracion'),
             InlineKeyboardButton(text="Muebleria", callback_data='muebleria')],
            [InlineKeyboardButton(text="Tapiceria", callback_data='tapiceria'),
             InlineKeyboardButton(text="Salida", callback_data='salida')]
        ])
    )
    

def menu_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Elige la Opcion Deseada:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Artesania", callback_data='artesania'),
            InlineKeyboardButton(text="Carpinteria", callback_data='carpinteria')],
            [InlineKeyboardButton(text="Decoraciones", callback_data='decoracion'),
            InlineKeyboardButton(text="Muebleria", callback_data='muebleria')],
            [InlineKeyboardButton(text="Tapiceria", callback_data='tapiceria'),
            InlineKeyboardButton(text="Salida", callback_data='salida')]
        ])
    )
    return ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA


def muebleria_command_handler(update, context):
    update.message.reply_text(
        text='Elige el modelo:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
            InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
            [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
            InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
            [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
            InlineKeyboardButton("Puff Redondos", callback_data='66')],
            [InlineKeyboardButton("Salida", callback_data='salida')]
        ])
                    
    )
    return INPUT_BUTTON
    
def muebleria_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Hola de Nuevo',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Modelo Camagueyano", callback_data='cmg'),
            InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
            [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
            InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
            [InlineKeyboardButton("Puff Cuadrados", callback_data='55'),
            InlineKeyboardButton("Puff Redondos", callback_data='66')],
            [InlineKeyboardButton("Salida", callback_data='salida')]
        ])
    )
    return MUEBLERIA

def cmg_callback_handler(update, context, chat, self, IMG_2097):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Esto es un Camagueyano',
    )
    chat.send_photo(
        photo=open('../multimedia/IMG_2097.jpg', 'rb')
    )

def send_puff_c(update, context):
    query = update.callback_query
    query.answer()
    if query == "55":
        bot.send_photo(cid, open('../multimedia/IMG_2097.jpg', 'rb'),
                       reply_markup=hideBoard)  # send file and hide keyboard, after image is sent

def salida_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Nos vemos la proxima vez'
    )
    return ConversationHandler.END

# def send_puff_c(bot, update, context):
#     query = update.callback_query_id
#     query.answer()
#     photo=open('./multimedia/IMG_2097.jpg', 'rb')
#     chat_id = update.message.chat_id
#     bot.send_photo(chat_id=chat_id, photo=open)


if __name__ == "__main__":
    updater = Updater(token='', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    #dp.add_handler(CommandHandler('menu', INPUT_BUTTON))
    # dp.add_handler(CommandHandler('muebleria', muebleria_command_handler))

    #dp.add_handler(CallbackQueryHandler(pattern='menu', callback=menu_callback_handler))
    # dp.add_handler(CallbackQueryHandler(pattern='muebleria', callback=muebleria_callback_handler))
    # dp.add_handler(CallbackQueryHandler(pattern='cmg', callback=cmg_callback_handler))
    # dp.add_handler(CallbackQueryHandler(pattern='55', callback=send_puff_c))
    # dp.add_handler(CallbackQueryHandler(pattern='salida', callback=salida_callback_handler))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='menu', callback=menu_callback_handler)
        ],

        states={
            #ARTESANIA: [RegexHandler('^(Si|No)$', artesania)],
            #CARPINTERIA: [RegexHandler('^(Si|No)$', carpinteria)],
            #COSTURA: [RegexHandler('^(Si|No)$', costura)],
            #DECORACION: [RegexHandler('^(Si|No)$', decoracion)],
            #MUEBLERIA: [RegexHandler('^(Si|No)$', muebleria_callback_handler)],
            #TAPICERIA:[RegexHandler('^(Si|No)$', tapiceria)],
            #MUEBLERIA: [CallbackQueryHandler(pattern='muebleria', callback=muebleria_callback_handler)]
            INPUT_BUTTON: [RegexHandler(
                '^(Artesania|Carpinteria|Costura|Decoracion|Muebleria|Tapiceria)$',
                menu_callback_handler)],
        },

        fallbacks=[CommandHandler('start', start)]
    ))

    
    updater.start_polling()
    updater.idle()