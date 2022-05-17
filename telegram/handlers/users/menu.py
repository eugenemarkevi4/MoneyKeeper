from aiogram import types
from aiogram.dispatcher.filters import Command

from telegram.keyboards.default.menu import main_menu
from telegram.loader import dp

# from filters import IsPrivate
# from utils.misc import rate_limit


# @rate_limit(limit=15, key="/start")
@dp.message_handler(Command("menu"))
async def command_start(message: types.Message):
    await message.answer(f"Ты в главном меню 👇", reply_markup=main_menu)

@dp.message_handler(text="🏠 Главное меню")
async def command_start(message: types.Message):
    await message.answer(f"Ты в главном меню 👇", reply_markup=main_menu)