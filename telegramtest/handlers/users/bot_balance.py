from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivate
from loader import dp
from telegram.states import balance
from telegram.utils.db_api import quick_commands as commands

@dp.message_handler(IsPrivate(), text="/balance")
async def change_balance(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f"Ваш баланс - $ {user.balance}")

@dp.message_handler(IsPrivate(), text="/change_balance")
async def change_balance(message: types.Message):
    await message.answer("Введите сумму пополнения")
    await balance.amount.set()

@dp.message_handler(IsPrivate(), state=balance.amount)
async def change_balance(message: types.Message, state: FSMContext):
    answer = message.text
    check_balance = await commands.check_balance(user_id=message.from_user.id, amount=answer)
    if check_balance == "no money":
        await message.answer("Нет баблишка")
        await state.finish()
    elif check_balance:
        await message.answer("Баланс изменен")
        await state.finish()
    elif not check_balance:
        await message.answer("Некоректное число")
        await state.finish()
    else:
        await message.answer("Оштбка используйте старт")
        await state.finish()