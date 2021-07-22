update.callback_query.message.edit_reply_markup(
    reply_markup=reply_markup,
    *args,
    **kwargs
)

        context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=artesania_keyboard())