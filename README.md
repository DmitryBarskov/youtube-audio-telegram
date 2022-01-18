# youtube-audio-telegram
Youtube Audio Download bot for Telegram

## Deploy

### To Heroku

```bash
heroku create
heroku config:set TELEGRAM_API_TOKEN=...
heroku config:set PY_ENV=PRODUCTION

heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python

git push heroku main
```
