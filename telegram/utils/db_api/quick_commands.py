from asyncpg import UniqueViolationError

from telegram.utils.db_api.db_gino import db
from telegram.utils.db_api.schemas.expense import Expense


async def add_expense(name_expenses: str, account_id: int, category_expenses_id: int, img: str, note: str, status: str, summ_expenses: float, tag_id: int, user_id: int):
    try:
        expense = Expense(name_expenses=name_expenses, account_id=account_id, category_expenses_id=category_expenses_id, img=img, note=note, status=status, summ_expenses=summ_expenses, tag_id=tag_id, user_id=user_id)
        await expense.create()
    except UniqueViolationError:
        print("Запись о расходе не добавлена")

async def select_all_expense():
    expenses = await Expense.query.gino.all()
    return expenses

async def count_expenses():
    count = await db.func.count(Expense.id).gino.scalar()
    return count

async def select_expense(id):
    expense = await Expense.query.where(Expense.id == id).gino.first()
    return expense

# async def add_expense(user_id: int, first_name: str, last_name: str, username: str, referral_id: int, status: str, balance: int):
#     try:
#         expense = Expense(user_id=user_id, first_name=first_name, last_name=last_name, username=username, referral_id=referral_id, status=status, balance=balance)
#         await expense.create()
#     except UniqueViolationError:
#         print("Запись о расходе не добавлена")
#
# async def select_all_expense():
#     expenses = await Expense.query.gino.all()
#     return expenses
#
# async def count_expenses():
#     count = await db.func.count(Expense.user_id).gino.scalar()
#     return count
#
# async def select_expense(user_id):
#     expense = await Expense.query.where(Expense.user_id == user_id).gino.first()
#     return expense