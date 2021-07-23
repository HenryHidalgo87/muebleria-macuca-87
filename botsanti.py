#!/usr/bin/en python3
# -*- coding: utf-8 -*
import telegram
import os, sys                # Basic python libraries
import os.path as path 
<<<<<<< HEAD
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext
=======
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply , ChatAction
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext, RegexHandler
>>>>>>> 4d96241fd6ce065ce9280b1613202f9ea5b742b5

MENU_COMMAND_HANDLER, ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA, SALIDA = range(8) 

MENU_COMMAND_HANDLER = 0

def start(update, context):
<<<<<<< HEAD
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
=======
    update.message.reply_text(
        text='Hola Bienvenido al Taller de Santi\n\nSelecciona / para la lista de comandos o usa el boton Menu',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Menu', callback_data='menu'),
            InlineKeyboardButton(text='Sobre el Autor', url='https://t.me/henryhidalgo870')]
        ])
    )
    return MENU_COMMAND_HANDLER
def menu_command_handler(update, context):
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
    return MENU_COMMAND_HANDLER

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
    return MENU_COMMAND_HANDLER

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
    return MENU_COMMAND_HANDLER
    
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
    query.chat.send_photo(
        photo=open('../multimedia/IMG_2097.jpg', 'rb')
    )

def salida_callback_handler(update, context):
    query = update.callback_query_id
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
>>>>>>> 4d96241fd6ce065ce9280b1613202f9ea5b742b5


if __name__ == "__main__":
    updater = Updater(token='1630057239:AAGno5APPSjhkE8_S4AV56EpUAH51CTCQVY', use_context=True)
<<<<<<< HEAD

=======
>>>>>>> 4d96241fd6ce065ce9280b1613202f9ea5b742b5
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('menu', menu_command_handler))
    dp.add_handler(CommandHandler('muebleria', muebleria_command_handler))

<<<<<<< HEAD
    dp.add_handler(CommandHandler('muebleria', muebleria))

    #dp.add_handler(CallbackQueryHandler(muebleria, pattern='muebleria' + str(MUEBLERIA) + '$'))

    dp.add_handler(CallbackQueryHandler(menu_actions, pattern='menu_actions'))
    dp.add_handler(CallbackQueryHandler(menu_actions, pattern='muebleria'))
=======
    dp.add_handler(CallbackQueryHandler(pattern='menu', callback=menu_callback_handler))
    dp.add_handler(CallbackQueryHandler(pattern='muebleria', callback=muebleria_callback_handler))
    dp.add_handler(CallbackQueryHandler(pattern='cmg', callback=cmg_callback_handler))
    dp.add_handler(CallbackQueryHandler(pattern='55', callback=send_puff_c))
    dp.add_handler(CallbackQueryHandler(pattern='salida', callback=salida_callback_handler))
>>>>>>> 4d96241fd6ce065ce9280b1613202f9ea5b742b5

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('start', start)
        ],

<<<<<<< HEAD
    updater.start_polling(allowed_updates=[])
    updater.idle()
=======
        states={
            MENU_COMMAND_HANDLER: [CallbackQueryHandler(pattern='menu', callback=menu_callback_handler)]
        },
>>>>>>> 4d96241fd6ce065ce9280b1613202f9ea5b742b5

        fallbacks=[CommandHandler('start', start)]
    ))

    
    updater.start_polling()
    updater.idle()
