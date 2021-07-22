import telegram
import os, sys                # Basic python libraries
import os.path as path 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler, CallbackContext

#variables
MENU, ARTESANIA, CARPINTERIA, COSTURA, DECORACIONES, MUEBLERIA, TAPICERIA, SALIDA = range(8) 

def start(update: Update, _: CallbackContext) -> int:
    reply_keyboard = [['start']]

    update.message.reply_text(
        'Hola, bienvenido a Muebleria Santi\n\n'
        'Usa "/" para interactuar con los Comandos o use los Botones del Bot',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return MENU

def muebleria(update, context: CallbackContext)-> None:
    keyboard = [
                [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadraros", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('BE MY GIRL OK?', reply_markup=reply_markup)

def muebleria_reply(update, context):
    query = update.callback_query
    if query.data == 'yes':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='\U0001F46B\U0001F49D', disable_web_page_preview = 0)
    else:
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Please try again, we make typing errors sometimes \U0001F624' , disable_web_page_preview = 0)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    persistence = PicklePersistence(filename='conversationbot')
    updater = Updater("TOKEN", persistence=persistence)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [
                MessageHandler(
                    Filters.regex('^(Age|Favourite colour|Number of siblings)$'), regular_choice
                ),
                MessageHandler(Filters.regex('^Something else...$'), custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
        name="my_conversation",
        persistent=True,
    )

    dispatcher.add_handler(conv_handler)

    show_data_handler = CommandHandler('show_data', show_data)
    dispatcher.add_handler(show_data_handler)
    dp.add_handler(CallbackQueryHandler(confession_reply))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
