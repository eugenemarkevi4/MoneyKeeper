from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, Message, user
from aiogram.utils import executor
from aiogram import Bot
import os
from pathlib import Path

bot = Bot('951470832:AAGcrJd-mMgL6foDRnaoUJMypZxrYLopRdE')
dp = Dispatcher(bot)



# @dp.message_handler(content_types=ContentType.DOCUMENT)
# async def get_photo(message: Message):
#     path_to_download = Path().joinpath("images")
#     path_to_download.mkdir(parents=True, exist_ok=True)
#     path_to_download = path_to_download.joinpath(message.document.file_name)
#     file_name = message.document.file_name
#     await message.document.download(destination_file=path_to_download)
#     await message.answer(f"Документ был загружен: images/{file_name}")


@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    # file = message.photo[-1].file_id
    # print(file_id) # этот идентификатор нужно где-то сохранить
    # await bot.send_photo(message.chat.id, file_id)
    await message.photo[-1].download('../images/')

if __name__ == '__main__':
    executor.start_polling(dp)