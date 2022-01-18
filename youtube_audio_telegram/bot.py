from telegram import Update
from telegram.ext import (Updater, CallbackContext, CommandHandler)

from __init__ import TELEGRAM_API_TOKEN

updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

updater.dispatcher.add_handler(start_handler)

updater.start_polling()
