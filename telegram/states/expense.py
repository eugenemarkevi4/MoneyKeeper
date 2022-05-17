from aiogram.dispatcher.filters.state import StatesGroup, State


class expense(StatesGroup):
    name_expense = State()
    category_expense = State()
    summ_expense = State()
    tag_expense = State()
    account = State()
    notes = State()
