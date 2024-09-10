from aiogram.types.bot_command import BotCommand
from loader import bot

async def set_default_commands():
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Botni ishga tushurish"),
            BotCommand(command="help", description="Yordam"),
        ]
    )
