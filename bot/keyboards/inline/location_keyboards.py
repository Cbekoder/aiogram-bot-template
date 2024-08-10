from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.get_locations import locations

builder = InlineKeyboardBuilder()

for location in locations.keys():
    builder.button(text=f"{location}", callback_data=f"set_location:{location}")

send_location = InlineKeyboardMarkup(inline_keyboard=builder.export())
