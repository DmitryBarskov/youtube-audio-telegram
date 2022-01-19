import __init__

import re
import io
import random

from pytube import YouTube
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from environment_variables import (TELEGRAM_API_TOKEN, PORT)
from __init__ import start_bot

YT_PATTERN = r'((https?://)?(youtu\.be/\w{11}|(www\.)?youtube\.com/watch\?v=\w{11}))'


def format_video_link(link: str) -> str:
    return f"[This]({link}) is a youtube video"


def youtube_video(update: Update, context: CallbackContext):
    matches = re.findall(YT_PATTERN, update.message.text)

    yt_links = map(lambda match: match[0], matches)
    for link in yt_links:
        buffer = io.BytesIO()
        video = YouTube(link)
        audio = video.streams.get_audio_only()
        audio.stream_to_buffer(buffer)
        context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=buffer.getvalue(),
            reply_to_message_id=update.message.message_id,
            duration=video.length,
            performer=video.author,
            title=video.title
        )


def random_emoji() -> str:
    return random.choice('😎🥰❤️😉😘😍😊☺️🙂📺😋😚')


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
