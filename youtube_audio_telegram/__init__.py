import logging

from environs import Env

env = Env()
env.read_env()
TELEGRAM_API_TOKEN = env('TELEGRAM_API_TOKEN')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

__version__ = '0.1.0'
