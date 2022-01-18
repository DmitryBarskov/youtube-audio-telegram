from telegram.ext import (Updater)


def start_bot(updater: Updater):
    updater.start_polling()
    updater.idle()
