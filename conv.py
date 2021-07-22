#!/usr/bin/en python3
# -*- coding: utf-8 -*
import telegram
import os, sys                # Basic python libraries
import os.path as path 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext, RegexHandler

# # Stages
# FIRST, SECOND = range(2)
# # Callback data
# ONE, TWO, THREE, FOUR = range(4)
MENU, ARTESANIA, CARPINTERIA, COSTURA, DECORACION, MUEBLERIA, TAPICERIA, SALIDA = range(8) 

############################### Bot ############################################
def start(update, context) -> None:
    update.message.reply_text(main_menu_message(),
                        reply_markup=main_menu_keyboard())

def main_menu(update, context: CallbackContext) -> None:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())


def main_menu_reply(update, context):
    query = update.callback_query
    if query.data == 'artesania':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=artesania_keyboard())
    if '1' == '11':
        reply_keyboard = [['Si', 'No']]
        update.message.reply_text(
            '¿Has probado Arch?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                             one_time_keyboard=True))
    elif query.data == 'carpinteria':
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

    elif query.data == 'costura':
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

    elif query.data == 'decoracion':
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

    elif query.data == 'muebleria':
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

    elif query.data == 'tapiceria':
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())
    else:
         context.bot.edit_message_text(chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         text='Please try again, we make typing errors sometimes \U0001F624' , disable_web_page_preview = 0)              
    

def artesania(update, context: CallbackContext) -> None:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=muebleria_menu_message(),
                        reply_markup=artesania_keyboard())

def artesania_reply(update, context):
    query = update.callback_query
    if query.data == '11':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

def carpinteria(update, context: CallbackContext) -> None:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=muebleria_menu_message(),
                        reply_markup=muebleria_keyboard())

def carpinteria_reply(update, context):
    query = update.callback_query
    if query.data == '11':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

def costura(update, context: CallbackContext) -> None:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=muebleria_menu_message(),
                        reply_markup=muebleria_keyboard())

def costura_reply(update, context):
    query = update.callback_query
    if query.data == '11':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

def decoracion(update, context: CallbackContext) -> None:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=muebleria_menu_message(),
                        reply_markup=muebleria_keyboard())

def decoracion_reply(update, context):
    query = update.callback_query
    if query.data == '11':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())

def muebleria(update, context: CallbackContext) -> int:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=muebleria_menu_message(),
                        reply_markup=muebleria_keyboard())

def muebleria_reply(update, context) -> int:
    query = update.callback_query
    if query.data == '11':
      user = update.message.from_user
      photo_file = update.message.photo[-1].get_file()
      photo_file.download('user_photo.jpg')
      update.message.reply_text(
        'Gracias por elejir este modelo.')

    return LOCATION

def tapiceria(update, context: CallbackContext) -> None:
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=muebleria_menu_message(),
                        reply_markup=muebleria_keyboard())

def tapiceria_reply(update, context):
    query = update.callback_query
    if query.data == '11':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=muebleria_keyboard())








# and so on for every callback_data option
def muebleria(context, update) -> None:
  pass

def second_submenu(context, update) -> None:
  pass









############################ Keyboards #########################################
def main_menu_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("Artesania", callback_data='artesania'),
                 InlineKeyboardButton("Carpinteria", callback_data='carpinteria')],
                [InlineKeyboardButton("Costura", callback_data='costura'),
                 InlineKeyboardButton("Decoraciones", callback_data='decoracion')],
                [InlineKeyboardButton("Muebleria", callback_data='muebleria'),
                 InlineKeyboardButton("Tapiceria", callback_data='tapiceria')],
                [InlineKeyboardButton("Salida", callback_data='salida')]]
    return InlineKeyboardMarkup(keyboard)

def artesania_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("1", callback_data='11'),
                 InlineKeyboardButton("2", callback_data='22')],
                [InlineKeyboardButton("3", callback_data='33'),
                 InlineKeyboardButton("4", callback_data='44')],
                [InlineKeyboardButton("5", callback_data='55'),
                 InlineKeyboardButton("6", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    return InlineKeyboardMarkup(keyboard)

def carpinteria_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    return InlineKeyboardMarkup(keyboard)

def costura_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    return InlineKeyboardMarkup(keyboard)

def decoracion_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    return InlineKeyboardMarkup(keyboard)

def muebleria_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    return InlineKeyboardMarkup(keyboard)

def tapiceria_keyboard() -> None:
    keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
    return InlineKeyboardMarkup(keyboard)





############################# Messages #########################################
def main_menu_message() -> None:
    return 'Hola, bienvenido a Muebleria Santi\n\nUsa "/" para interactuar con los Comandos o use los Botones del Bot'

def muebleria_menu_message() -> None:
  return 'Elige el modelo:'






























############################# Handlers #########################################


if __name__ == "__main__":
    updater = Updater(token='1630057239:AAGno5APPSjhkE8_S4AV56EpUAH51CTCQVY', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('main_menu', main_menu))

    dp.add_handler(CommandHandler('artesania', artesania))

    dp.add_handler(CommandHandler('carpinteria', carpinteria))

    dp.add_handler(CommandHandler('costura', costura))

    dp.add_handler(CommandHandler('decoracion', decoracion))

    dp.add_handler(CommandHandler('muebleria', muebleria))

    dp.add_handler(CommandHandler('tapiceria', tapiceria))


    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    # dp.add_menu_handler = ConversationHandler(
    #      entry_points=[CommandHandler('start', start)],
    #      states={
    #            MENU: [RegexHandler(
    #              '^(Artesania|Carpinteria|Costura|Decoracion|Muebleria|Tapiceria)$',
    #             main_menu)],
    #             ARTESANIA: [RegexHandler('^(Si|No)$', artesania)],
    #             CARPINTERIA: [RegexHandler('^(Si|No)$', carpinteria)],
    #             COSTURA: [RegexHandler('^(Si|No)$', costura)],
    #             DECORACION: [RegexHandler('^(Si|No)$', decoracion)],
    #             MUEBLERIA: [RegexHandler('^(Si|No)$', muebleria)],
    #             TAPICERIA:[RegexHandler('^(Si|No)$', tapiceria)],
    #             },
    #      fallbacks=[CommandHandler('start', start)],
    # )
    dp.add_handler(CallbackQueryHandler(main_menu_reply))
    dp.add_handler(CallbackQueryHandler(artesania, pattern='artesania'))
    dp.add_handler(CallbackQueryHandler(carpinteria, pattern='carpinteria'))
    dp.add_handler(CallbackQueryHandler(costura, pattern='costura'))
    dp.add_handler(CallbackQueryHandler(decoracion, pattern='decoracion'))
    dp.add_handler(CallbackQueryHandler(muebleria, pattern='muebleria'))
    dp.add_handler(CallbackQueryHandler(tapiceria, pattern='tapiceria'))
    #dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    #dp.add_handler(CallbackQueryHandler(first_submenu,
                                                    #pattern='m1_1'))
    #dp.add_handler(CallbackQueryHandler(second_submenu,
                                                    #pattern='m2_1'))
    

    updater.start_polling(allowed_updates=[])
    updater.idle()

