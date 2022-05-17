from aiogram import types
from aiogram.dispatcher import FSMContext

from telegram.utils.db_api import quick_commands as commands

from telegram.keyboards.expense import expense_category, expense_tag, bank_account, expense_final, note_kb
from telegram.states.expense import expense
from telegram.loader import dp

@dp.message_handler(text="💸 Добавить расход")
async def name_expense(message: types.Message):
    await message.answer(f"Введи название покупки \n")
    await expense.name_expense.set()

@dp.message_handler(state=expense.name_expense)
async def category_expense(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name_expense=answer)
    await message.answer("Выбери категорию расхода", reply_markup=expense_category)
    await expense.category_expense.set()

@dp.message_handler(state=expense.category_expense)
async def summ_expense(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(category_expense=answer)
    await message.answer("Введи сумму расхода")
    await expense.summ_expense.set()

# @dp.message_handler(state=expense.summ_expense)
# async def account(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     await state.update_data(summ_expense=answer)
#     await message.answer("Выбери счет списания", reply_markup=bank_account)
#     await expense.account.set()
#     if message.text == "Cash":
#         account = int(1)
#     elif message.text == "Tinkoff Bank EM":
#         account = int(2)


@dp.message_handler(state=expense.summ_expense)
async def account(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(summ_expense=answer)
    await message.answer("Выбери счет списания", reply_markup=bank_account)
    await expense.account.set()


@dp.message_handler(state=expense.account)
async def tag_expense(message: types.Message, state: FSMContext):
    answer = message.text

    if message.text == "Tinkoff Bank EM":
        answer = 1

    print(answer)

    await state.update_data(account=answer)
    await message.answer("Выбери тэг", reply_markup=expense_tag)
    await expense.tag_expense.set()

@dp.message_handler(state=expense.tag_expense)
async def notes(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(tag_expense=answer)
    await message.answer("Введи заметку по покупке", reply_markup=note_kb)
    await expense.notes.set()

@dp.message_handler(state=expense.notes)
async def expense_done(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(notes=answer)
    data = await state.get_data()
    name_expense = data.get("name_expense")
    category_expense = data.get("category_expense")
    summ_expense = data.get("summ_expense")
    account = data.get("account")
    tag_expense = data.get("tag_expense")
    notes = data.get("notes")

    await commands.add_expense(name_expenses=name_expense,
                               account_id=account,
                               category_expenses_id=1,
                               img='none',
                               note=notes,
                               status='CNFD',
                               summ_expenses=float(summ_expense),
                               tag_id=3,
                               user_id=1)

    await message.answer(f"{message.from_user.first_name}, спасибо, все записал 👌 \n \n"
                         f"Наименование - {name_expense} \n"
                         f"Категория - {category_expense} \n"
                         f"Сумма - $ {summ_expense} \n"
                         f"Счет - {account} \n"
                         f"Тэг - {tag_expense} \n"
                         f"Заметка - {notes} \n", reply_markup=expense_final)

    await state.finish()