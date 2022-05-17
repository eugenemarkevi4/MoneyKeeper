import asyncio

from data import config
from telegram.utils.db_api import quick_commands
from telegram.utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)

    print("Добавляем пользователей")
    await quick_commands.add_user(1, "One", "testtt")
    await quick_commands.add_user(2, "Two", "sfdsdfh")
    await quick_commands.add_user(3, "Thre", "wetwet")
    await quick_commands.add_user(4, "For", "erywhwe")
    await quick_commands.add_user(5, "Five", "5436dsfh")
    print("Готово")

    users = await quick_commands.select_all_users()
    print(f"Получил всех пользователей: {users}")

    count_users = await quick_commands.count_users()
    print(f"Всего пользователей: {count_users}")

    # user = await quick_commands.select_user()
    # print(f"Получил пользователя: {user}")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())