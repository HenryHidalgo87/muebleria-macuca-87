#!/usr/bin/en python3
# -*- coding: utf-8 -*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext

# Stages
FIRST, SECOND = range(2)
# Callback data
ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA = range(6)

def start(update: Updater, _: CallbackContext) -> None:

    keyboard = [[InlineKeyboardButton("Artesania", callback_data=str(ARTESANIA)),
                 InlineKeyboardButton("Carpinteria", callback_data=str(CARPINTERIA))],
                [InlineKeyboardButton("Costura", callback_data=str(COSTURA)),
                 InlineKeyboardButton("Decoraciones", callback_data=str(DECORACIONES))],
                [InlineKeyboardButton("Muebleria", callback_data=str(MUEBLERIA)),
                 InlineKeyboardButton("Tapiceria", callback_data=str(TAPICERIA))]]
                
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Hola, bienvenido a Muebleria Santi\n\nUsa / para interactuar con los Comandos o use los Botones del Bot", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

def start_over(update: Updater, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    keyboard = [[InlineKeyboardButton("Artesania", callback_data=str(ARTESANIA)),
                 InlineKeyboardButton("Carpinteria", callback_data=str(CARPINTERIA))],
                [InlineKeyboardButton("Costura", callback_data=str(COSTURA)),
                 InlineKeyboardButton("Decoraciones", callback_data=str(DECORACIONES))],
                [InlineKeyboardButton("Muebleria", callback_data=str(MUEBLERIA)),
                 InlineKeyboardButton("Tapiceria", callback_data=str(TAPICERIA))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Hola, bienvenido a Muebleria Santi\n\nUsa "/" para interactuar con los Comandos o use los Botones del Bot", reply_markup=reply_markup)
    return FIRST

def muebleria(update: Updater, _: CallbackContext) -> None:
#"""Show new choice of buttons"""
    query = update.callback_query
    if query.data == 'muebleria':
        keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data=str(CMG)),
                InlineKeyboardButton("Modelo S.J 2Plazas", callback_data=str(SJ2))],
            [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data=str(SC3)),
                InlineKeyboardButton("Modelo Cuadrados", callback_data=str(MC))],
            [InlineKeyboardButton("Puff Cuadraros", callback_data=str(PC)),
                InlineKeyboardButton("Puff Redondos", callback_data=str(PR))],
            [InlineKeyboardButton("Salida", callback_data=str())]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Bienvenido al departamento de muebleria, Elige un modelo para que pueda verlo:", reply_markup=reply_markup
        )
    #return FIRST

def end(update: Updater, _: CallbackContext) -> None:
    #"""Returns `ConversationHandler.END`, which tells the
    #ConversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Nos vemos la proxima vez!")
    return ConversationHandler.END

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                #CallbackQueryHandler(artesania, pattern='^' + str(ARTESANIA) + '$'),
                #CallbackQueryHandler(carpinteria, pattern='^' + str(CARPINTERIA) + '$'),
                #CallbackQueryHandler(costura, pattern='^' + str(COSTURA) + '$'),
                #CallbackQueryHandler(decoraciones, pattern='^' + str(DECORACIONES) + '$'),
                CallbackQueryHandler(muebleria, pattern='^' + str(MUEBLERIA) + '$'),
                #CallbackQueryHandler(tapiceria, pattern='^' + str(TAPICERIA) + '$')
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(MUEBLERIA) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(MUEBLERIA) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )
    dp = updater.dispatcher
 
    dispatcher.add_handler(conv_handler)

    dp.add_handler(CommandHandler('muebleria', muebleria))

    updater.dispatcher.add_handler(CallbackQueryHandler(muebleria))


    updater.start_polling()


    updater.idle()



if __name__ == '__main__':
    main()