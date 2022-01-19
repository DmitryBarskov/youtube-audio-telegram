from environs import Env


ENV = Env()
ENV.read_env()

TELEGRAM_API_TOKEN = ENV('TELEGRAM_API_TOKEN')
PORT = ENV.int('PORT', 8443)
print("PORT:", PORT)
PY_ENV = ENV('PY_ENV', 'production')
HOST = ENV('HOST', None)
