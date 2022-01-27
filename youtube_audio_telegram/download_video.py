import logging

from io import BytesIO
from pytube import YouTube


def download_video(link: str) -> BytesIO:
    logging.info(f'Downloading {link}')
    video = YouTube(link)
    audio = video.streams.get_audio_only()
    buffer = BytesIO()
    audio.stream_to_buffer(buffer)
    return (
        buffer,
        {
            'duration': video.length,
            'channel': video.author,
            'title': video.title
        }
    )
