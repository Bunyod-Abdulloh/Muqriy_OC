from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yes_no = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅  Ҳа",
                callback_data="yes"
            ),
            InlineKeyboardButton(
                text="♻  Йўқ қайтиш",
                callback_data="no_again"
            )
        ]
    ]
)

savol_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Аёллар'),
            KeyboardButton('Эркаклар'),
        ],
        [
            KeyboardButton('🏡 Бош меню'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)