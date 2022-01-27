import __init__

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from environment_variables import TELEGRAM_API_TOKEN, PORT
from __init__ import start_bot
from parse_links import parse_links, YT_PATTERN
from emoji import sad_emoji, random_emoji
from download_video import download_video


def youtube_video(update: Update, context: CallbackContext):
    yt_links = parse_links(update.message.text)

    welcome_message = context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.message.message_id,
        text="Downloading video(s) " + ", ".join(yt_links)
    )
    try:
        for link in yt_links:
            buffer, info = download_video(link)
            context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=buffer.getvalue(),
                reply_to_message_id=update.message.message_id,
                duration=info['duration'],
                performer=info['channel'],
                title=info['title']
            )
    except Exception as e:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            reply_to_message_id=update.message.message_id,
            text="Sorry, can't download videos now " + sad_emoji() + "\n" + str(e)
        )
    finally:
        welcome_message.delete(timeout=5)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, send me a video from youtube! " + random_emoji()
    )


def main():
    updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(YT_PATTERN), youtube_video))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, start))

    start_bot(updater)


if __name__ == '__main__':
    main()
