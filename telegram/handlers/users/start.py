from aiogram import types

from telegram.keyboards.default.menu import main_menu
from telegram.loader import dp, bot

# from filters import IsPrivate
# from utils.misc import rate_limit


# @rate_limit(limit=15, key="/start")
from telegramtest.utils.db_api.schemas import user


@dp.message_handler(text="/start")
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name} 👋 \n"
                         f"Я твой бот помощник в ведении личных финансов 💰 \n")
    await message.answer(f"Выбери пункт меню, чтобы начать работу 👇", reply_markup=main_menu)

