import logging

from environment_variables import PY_ENV

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

__version__ = '0.1.0'

if PY_ENV.upper() == 'PRODUCTION':
    logging.info('Loading production environment')
    from production import start_bot
else:
    logging.info('Loading development environment')
    from development import start_bot
