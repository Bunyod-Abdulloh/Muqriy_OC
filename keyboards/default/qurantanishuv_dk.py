from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tanishuv_aud_vid_keys = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏡 Бош меню"),
        ],
        [
            KeyboardButton(text = "🎧 Аудио"), #ҳамма шрифт ўзбек кириллда
            KeyboardButton(text = "🎞 Видео"), #ҳамма шрифт ўзбек кириллда
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

tanishuv_aud_keys = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏮ Oлдинги"),
            KeyboardButton(text="🏡 Бош меню"),
        ],
        [
            KeyboardButton(text = "1-5 суҳбатлар"),
            KeyboardButton(text = "6-10 суҳбатлар"),
        ],
        [
            KeyboardButton(text = "11-15 суҳбатлар"),
            KeyboardButton(text="16-20 суҳбатлар"),
        ],
        [
          KeyboardButton(text="21-25 суҳбатлар"),
        ],
        [
            KeyboardButton(text="26-суҳбaт"), #y harfi lotin yozuvida
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

tanishuv_keys = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏮ Oлдинги"),
            KeyboardButton(text="🏡 Бош меню"),
        ],
        [
            KeyboardButton(text="1-суҳбат"), #hamma harf lotinda
            KeyboardButton(text="2-суҳбат"),
            KeyboardButton(text="3-суҳбат"),
        ],
        [
            KeyboardButton(text="4-суҳбат"),
            KeyboardButton(text="5-суҳбат"),
            KeyboardButton(text="6-суҳбат"),
            KeyboardButton(text="7-суҳбат"),
        ],
        [
            KeyboardButton(text="8-суҳбат"),
            KeyboardButton(text="9-суҳбат"),
            KeyboardButton(text="10-суҳбат"),
        ],
        [
            KeyboardButton(text="11-суҳбат"),
            KeyboardButton(text="12-суҳбат"),
            KeyboardButton(text="13-суҳбат"),
        ],
        [
            KeyboardButton(text="14-суҳбат"),
            KeyboardButton(text="15-суҳбат"),
            KeyboardButton(text="16-суҳбат"),
            KeyboardButton(text="17-суҳбат"),
        ],
        [
            KeyboardButton(text="18-суҳбат"),
            KeyboardButton(text="19-суҳбат"),
            KeyboardButton(text="20-суҳбат"),
        ],
        [
            KeyboardButton(text="21-суҳбат"),
            KeyboardButton(text="22-суҳбат"),
            KeyboardButton(text="23-суҳбат"),
            KeyboardButton(text="24-суҳбат"),
        ],
        [
            KeyboardButton(text="25-суҳбат"),
            KeyboardButton(text="26-суҳбат"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

