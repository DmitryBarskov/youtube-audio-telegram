import random


def random_emoji() -> str:
    return random.choice([
        '😎', '🥰', '❤️', '😉', '😘', '😍', '😊', '☺️', '🙂',
        '📺', '😋', '😚'
    ])


def sad_emoji() -> str:
    return '🥺'
