import logging
from bot.data.config import ADMINS
from bot.loader import bot


async def on_startup_notify():
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi 🤖✅")
        except Exception as err:
            logging.exception(err)
