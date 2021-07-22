import logging
from telegram import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Update, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, ConversationHandler




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)
updater = Updater(token="1630057239:AAEZpaEWBKkyVOwQRf9pwHwZBmJmFIJ-VLI", use_context=True)
dispatcher = updater.dispatcher

reply_keyboard = [
    ['🔖 Conversation'],
    ['help']
]

markup = ReplyKeyboardMarkup(reply_keyboard)

def panel_start(update, context):
    message = "Welcome to bot"
    update.effective_message.reply_text(message, reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    

def button_start_panel(update, context):

    if update.message.text =="🔖 Conversation":
        Message = "Please tell me something about yourself :"
        update.effective_message.reply_text(Message, reply_markup=ReplyKeyboardMarkup([["cancel"]], resize_keyboard=True))
    a = update.message.text
    print(a)

    if update.message.text == 'help':
        update.effective_message.reply_text('....')

    elif update.message.text == "cancel" :
        update.message.reply_text('📍', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))




button_start_panel_handler = MessageHandler(Filters.text & (~Filters.command), button_start_panel)
dispatcher.add_handler(button_start_panel_handler)

start_handler = CommandHandler("start", panel_start)
dispatcher.add_handler(start_handler)


updater.start_polling()
updater.idle()
