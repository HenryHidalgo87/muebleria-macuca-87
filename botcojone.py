#!/usr/bin/en python3
# -*- coding: utf-8 -*
import telegram
import os, sys                # Basic python libraries
import os.path as path 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters,  CallbackQueryHandler
############################### Bot ############################################
def start(update, context) -> None:
    update.message.reply_text(main_menu_message(),
                        reply_markup=main_menu_keyboard())

def main_menu(context, update) -> None:
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(context, update) -> None:
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(context, update) -> None:
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(context, update) -> None:
  pass

def second_submenu(context, update) -> None:
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton("Artesania", callback_data='artesania'),
                 InlineKeyboardButton("Carpinteria", callback_data='carpiteria')],
                [InlineKeyboardButton("Costura", callback_data='costura'),
                 InlineKeyboardButton("Decoraciones", callback_data='decoraciones')],
                [InlineKeyboardButton("Muebleria", callback_data='muebleria'),
                 InlineKeyboardButton("Tapiceria", callback_data='tapiceria')],
                [InlineKeyboardButton("Salida", callback_data='salida')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton("Modelo Camagueyano", callback_data='11'),
                 InlineKeyboardButton("Modelo S.J 2Plazas", callback_data='22')],
                [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data='33'),
                 InlineKeyboardButton("Modelo Cuadrados", callback_data='44')],
                [InlineKeyboardButton("Puff Cuadrados", callback_data='55'),
                 InlineKeyboardButton("Puff Redondos", callback_data='66')],
                [InlineKeyboardButton("Salida", callback_data='77')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Hola, bienvenido a Muebleria Santi\n\nUsa "/" para interactuar con los Comandos o use los Botones del Bot'

def first_menu_message():
  return 'Elige el modelo:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

############################# Handlers #########################################
updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='muebleria'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

updater.start_polling()