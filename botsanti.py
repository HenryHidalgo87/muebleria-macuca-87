#!/usr/bin/en python3
# -*- coding: utf-8 -*
from telegram.ext import Updater, CommandHandler

def start(update, context):

    update.message.reply_text(
        text='Hola, bienvenido a muebleria Santi, qué deseas hacer?')

if __name__ == "__main__":
    updater = Updater(token='1630057239:AAEZpaEWBKkyVOwQRf9pwHwZBmJmFIJ-VLI', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


