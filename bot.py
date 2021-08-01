import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ChatAction, ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    callbackqueryhandler,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
MUEB, CARP, THREE, FOUR, CMG, SJ2, SM3, MCUD, PC, PR, BOTLL,BAN, BANQ, BARR, BJM, CAM, CLT, CUN, REP, MES, SILL, JCOM, BALANC, SILLP = range(24)


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""

    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
   
    keyboard = [
        [
            InlineKeyboardButton("Muebles", callback_data=str(MUEB)),
            InlineKeyboardButton("Carpinteria", callback_data=str(CARP)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
  
    update.message.reply_text("Bienvenidos a Muebleria Macuca 87", reply_markup=reply_markup)
    
    return FIRST


def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    
    query = update.callback_query
   
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Muebles", callback_data=str(MUEB)),
            InlineKeyboardButton("Carpinteria", callback_data=str(CARP)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    query.edit_message_text(text="Bienvenidos a Muebleria Macuca 87", reply_markup=reply_markup)
    return FIRST


def mueb(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton("Modelo Camagueyano", callback_data=str(CMG)),
            InlineKeyboardButton("Modelo S.J 2Plazas", callback_data=str(SJ2))],
            [InlineKeyboardButton("Modelo Semi Comico 3Plazas", callback_data=str(SM3)),
            InlineKeyboardButton("Modelo Cuadrados", callback_data=str(MCUD))],
            [InlineKeyboardButton("Modelo Puff Cuadraros", callback_data=str(PC)),
            InlineKeyboardButton("Modelo Puff Redondos", callback_data=str(PR))],
            [InlineKeyboardButton("Salir", callback_data=str(THREE))],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    query.message.reply_text(text="En hora buena, ahora escoja uno de estos modelos", reply_markup=reply_markup)
    return FIRST


def carp(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Botelleros", callback_data=str(BOTLL)),
        InlineKeyboardButton("Bancos", callback_data=str(BAN))],
        [InlineKeyboardButton("Banquetas", callback_data=str(BANQ)),
        InlineKeyboardButton("Barras", callback_data=str(BARR))],
        [InlineKeyboardButton("Bajos de Mesetas", callback_data=str(BJM)),
        InlineKeyboardButton("Camas", callback_data=str(CAM))],
        [InlineKeyboardButton("Closet", callback_data=str(CLT)),
        InlineKeyboardButton("Cunas", callback_data=str(CUN))],
        [InlineKeyboardButton("Repisas", callback_data=str(REP)),
        InlineKeyboardButton("Mesas", callback_data=str(MES))],
        [InlineKeyboardButton("Sillas", callback_data=str(SILL)),
        InlineKeyboardButton("Juegos de comedor", callback_data=str(JCOM))],
        [InlineKeyboardButton("Sillones", callback_data=str(BALANC)),
        InlineKeyboardButton("Sillas  de Playa", callback_data=str(SILLP))],
        [InlineKeyboardButton("Salir", callback_data=str(THREE))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="En hora buena, que desea encargar", reply_markup=reply_markup
    )
    return FIRST


def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Menu Principal", callback_data=str(MUEB)),
            InlineKeyboardButton("Salir del Bot", callback_data=str(CARP)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Que le gustaria?", reply_markup=reply_markup
    )
    return SECOND


def four(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("2", callback_data=str(CARP)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Fourth CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    
    return FIRST


def cmg(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(MUEB)),
        ]
]

    chat_id=update.effective_chat.id

    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.UPLOAD_PHOTO),
    
    return FIRST

def sj2(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(MUEB)),
        ]
    ]
    chat_id=update.effective_chat.id

    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.UPLOAD_PHOTO)
   

    query.bot.send_photo(chat_id = chat_id , photo=open('multimedia/But-SJ-Damasco-Gris.jpg', 'rb'),
                             caption="Modelo: SJ\n\n"
                                     "Numero de Plazas: Cuatro (1 Sofa de 2 Plazas y 2 Butacas)\n\n"
                                     "Material de Tapiceria: Damasco-Pana-Vinil\n\n"
                                     "Nota: Modelo adaptado para salas pequenas",
                             reply_markup = InlineKeyboardMarkup(main_menu)),
    
    return FIRST



def sm3(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(MUEB)),
        ]
    ]
    chat_id=update.effective_chat.id

    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.UPLOAD_PHOTO)
   

    query.bot.send_photo(chat_id = chat_id , photo=open('multimedia/Sofa-SC-3P-Pana-Carmelita.jpg', 'rb'),
                             caption="Modelo: Semi-Comico\n\n"
                                     "Numero de Plazas: Cinco (1 Sofa de 3 Plazas y 2 Butacas)\n\n"
                                     "Material de Tapiceria: Damasco-Pana-Vinil",
                             reply_markup = InlineKeyboardMarkup(main_menu)),
    return FIRST

def mcud(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(MUEB)),
        ]
    ]
    chat_id=update.effective_chat.id

    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.UPLOAD_PHOTO)
   

    query.bot.send_photo(chat_id = chat_id , photo=open('multimedia/Sofa-Cuadrado-5P-1mesaE.jpg', 'rb'),
                             caption="Modelo: Cuadrados\n\n"
                                     "Numero de Plazas: Depende de Usted Cuantas Necesitas\n\n"
                                     "Nota: La Mesa de Esquina no cuenta como plaza\n\n"
                                     "Material de Tapiceria: Damasco-Pana-Vinil",
                             reply_markup = InlineKeyboardMarkup(main_menu)),
    return FIRST

def pc(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(MUEB)),
        ]
    ]
    chat_id=update.effective_chat.id

    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.UPLOAD_PHOTO)
   

    query.bot.send_photo(chat_id = chat_id , photo=open('multimedia/Puff Cuadrado Pana-Rojo.jpg', 'rb'),
                             caption="Modelo: Puff Cuadrado\n\n"
                                     "Dimensiones: Ancho-40cm Altura-40cm\n\n"
                                     "Material de Tapiceria: Damasco-Pana-Vinil",
                             reply_markup = InlineKeyboardMarkup(main_menu)),

    return FIRST

def pr(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(MUEB)),
        ]
    ]
    chat_id=update.effective_chat.id

    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.UPLOAD_PHOTO)
   

    query.bot.send_photo(chat_id = chat_id , photo=open('multimedia/Puff Redondo.jpg', 'rb'),
                             caption="Modelo: Puff Redondo\n\n"
                                     "Dimensiones: Ancho-40cm Altura-40cm\n\n"
                                     "Material de Tapiceria: Damasco-Pana-Vinil",
                             reply_markup = InlineKeyboardMarkup(main_menu)),
    return FIRST

def botll(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def ban(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def banq(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def barr(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def bjm(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def cam(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def botll(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def clt(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def cun(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def rep(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def mes(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def sill(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def jcom(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def balanc(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def sillp(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    main_menu = [
        [
            InlineKeyboardButton("Telegram Contacto", url="https://t.me/henryhidalgo870"),
            InlineKeyboardButton("Whatapps Contacto", url="https://wa.me/message/RQQ5OVTZO2ZQG1"),
            InlineKeyboardButton("⬅️ Regresar", callback_data=str(CARP)),
        ]
    ]
    chat_id=update.effective_chat.id
    reply_markup = InlineKeyboardMarkup(main_menu)
   
    query.message.reply_text(text="En estos momentos solo estamos tomamos pedidos, pongase en contacto con nosotros", reply_markup=reply_markup)
   
    return FIRST

def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Hasta la proxima vez!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    
    updater = Updater("")

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(mueb, pattern='^' + str(MUEB) + '$'),
                CallbackQueryHandler(carp, pattern='^' + str(CARP) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(cmg, pattern='^' + str(CMG) + '$'),
                CallbackQueryHandler(sj2, pattern='^' + str(SJ2) + '$'),
                CallbackQueryHandler(sm3, pattern='^' + str(SM3) + '$'),
                CallbackQueryHandler(mcud, pattern='^' + str(MCUD) + '$'),
                CallbackQueryHandler(pc, pattern='^' + str(PC) + '$'),
                CallbackQueryHandler(pr, pattern='^' + str(PR) + '$'),
                CallbackQueryHandler(botll, pattern='^' + str(BOTLL) + '$'),
                CallbackQueryHandler(ban, pattern='^' + str(BAN) + '$'),
                CallbackQueryHandler(banq, pattern='^' + str(BANQ) + '$'),
                CallbackQueryHandler(barr, pattern='^' + str(BARR) + '$'),
                CallbackQueryHandler(bjm, pattern='^' + str(BJM) + '$'),
                CallbackQueryHandler(cam, pattern='^' + str(CAM) + '$'),
                CallbackQueryHandler(clt, pattern='^' + str(CLT) + '$'),
                CallbackQueryHandler(cun, pattern='^' + str(CUN) + '$'),
                CallbackQueryHandler(rep, pattern='^' + str(REP) + '$'),
                CallbackQueryHandler(mes, pattern='^' + str(MES) + '$'),
                CallbackQueryHandler(sill, pattern='^' + str(SILL) + '$'),
                CallbackQueryHandler(jcom, pattern='^' + str(JCOM) + '$'),
                CallbackQueryHandler(balanc, pattern='^' + str(BALANC) + '$'),
                CallbackQueryHandler(sillp, pattern='^' + str(SILLP) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(MUEB) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(CARP) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )


    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()