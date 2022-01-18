from telegram.ext import (Updater)

from environment_variables import (HOST, PORT, TELEGRAM_API_TOKEN)


def start_bot(updater: Updater):
    updater.start_webhook(
        listen="0.0.0.0", port=PORT, url_path=TELEGRAM_API_TOKEN
    )
    updater.bot.setWebhook(HOST + '/' + TELEGRAM_API_TOKEN)
