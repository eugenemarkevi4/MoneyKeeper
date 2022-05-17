from asyncpg import UniqueViolationError

from telegram.utils.db_api.db_gino import db
from telegram.utils.db_api.schemas.user import User


async def add_user(id: int, first_name: str, nick_name: str):
    try:
        user = User(id=id, first_name=first_name, nick_name=nick_name)
        await user.create()
    except UniqueViolationError:
        pass

async def select_all_users():
    users = await User.query.gino.all()
    return users

# async def select_user(id: int):
#     user = await User.query.where(User.id == id).gino.first()
#     return user

async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total

async def update_user_email(id, nick_name):
    user = await User.get(id)
    await user.update(nick_name=nick_name).apply()