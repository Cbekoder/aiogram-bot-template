import asyncio
import logging
import sys

import handlers, filters
from utils.on_start.notify_admins import on_startup_notify
from utils.on_start.set_bot_commands import set_default_commands
from loader import bot, dp


async def on_startup(dispatcher):
    await set_default_commands()
    await on_startup_notify()


async def main() -> None:
    # await dp.emit_startup(on_startup(dp))
    # await on_startup(dp)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
