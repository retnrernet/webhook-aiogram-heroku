import os


BOT_TOKEN = "1023713845:AAGZ-hHJbPfx8phFn53udo1wYVCxSVfOFH8"
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

HEROKU_APP_NAME = "petrjela"


# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))
