import asyncio

from data import config
from telegram.utils.db_api.db_gino import db
from telegram.utils.db_api import quick_commands as commands

async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_expense(3, 'Dear', 1, 1, 'wegwe', 'CNFD', 1520, 3, 1)
    await commands.add_expense(4, 'Twoo', 1, 1, 'wegwerhe', 'CNFD', 1520, 4, 1)

    expenses = await commands.select_all_expense()
    print(expenses)

    count = await commands.count_expenses()
    print(count)

    expense = await commands.select_expense(1)
    print(expense)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())