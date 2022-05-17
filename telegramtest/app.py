from telegram.loader import db

async def on_startup(dp):

    import telegram.filters
    telegram.filters.setup(dp)
    import middlewares
    middlewares.setup(dp)

    from utils.db_api.db_gino import on_startup
    print("Подключение к PostgreSQL")
    await on_startup(dp)

    print("Удаление базы данных")
    await db.gino.drop_all()

    print("Создание таблиц")
    await db.gino.create_all()

    print("Готово")

    from telegram.utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from telegram.utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

if __name__ == '__main__':
    from aiogram import executor
    from telegram.handlers import dp

    executor.start_polling(dp, on_startup=on_startup)