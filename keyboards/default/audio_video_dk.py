from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

allk = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏮ Олдинги"),
            KeyboardButton(text="🏡 Бош меню"),
        ],
        [
            KeyboardButton(text="🎧 Ayдиo"),
            KeyboardButton(text="🎬 Видео"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

alldk = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏡 Бош меню"),
        ],
        [
            KeyboardButton(text="🎧 Ayдиo"),
            KeyboardButton(text="🎬 Видео"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
