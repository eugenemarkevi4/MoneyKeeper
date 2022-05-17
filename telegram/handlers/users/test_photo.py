

from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from aiogram import Bot

from aiogram.types.file import File

import os

@dp.message_handler(content_types=ContentType.PHOTO)
async def photos(message: Message):
    file = await bot.get_file(user.photo_id)



# @dp.message_handler(content_types=ContentType.PHOTO)
# async def photo_id(message: Message):
#     file = await bot.get_file(message.photo[-1].file_id)
#     print(file)




# @dp.message_handler(content_types=ContentType.PHOTO)
# async def photo_handler(message: Message):
#     file_info = await bot.getFile(message.photo[-1].file_id)
#     await message.photo[-1].download(file_info.file_path.split('images/')[1])  # ++



# @dp.message_handler(text="/photo")
# async def send_photo(message: Message):
#     chat_id = message.from_user.id
#
#     await dp.bot.send_photo(chat_id=chat_id, photo='')