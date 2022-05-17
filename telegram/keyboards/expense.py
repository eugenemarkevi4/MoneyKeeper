from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

expense_category = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Еда")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

bank_account = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tinkoff Bank EM")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

expense_tag = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="tag")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

expense_final = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💸 Добавить расход")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

note_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="нет")
        ],
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)