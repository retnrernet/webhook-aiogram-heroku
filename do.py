''' Run a function by ado <func_name> '''


def set_hook():
    import asyncio
    from bot.settings import HEROKU_APP_NAME, WEBHOOK_URL, BOT_TOKEN
    from aiogram import Bot
    bot = Bot(token=BOT_TOKEN)



    asyncio.run(hook_set())
    bot.close()


def start():
    from bot.bot import main
    main()
