from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💸 Добавить расход")
        ],
        [
            KeyboardButton(text="💰 Добавить доход")
        ],
        [
            KeyboardButton(text="💵 Перевод между счетами")
        ],
        [
            KeyboardButton(text="🏦 Мой капитал")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)