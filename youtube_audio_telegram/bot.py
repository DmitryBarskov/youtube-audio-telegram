import __init__

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from environment_variables import (TELEGRAM_API_TOKEN, PORT)
from __init__ import start_bot

YT_PATTERN = r'(https?://)?(youtu\.be/\w{11}|(www\.)?youtube\.com/watch\?v=\w{11})'


def youtube_video(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="This is a youtube video"
    )


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


def main():
    updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(YT_PATTERN), youtube_video))

    start_bot(updater)


if __name__ == '__main__':
    main()
