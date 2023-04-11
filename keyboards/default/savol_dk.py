from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

savol_dk = ReplyKeyboardMarkup(resize_keyboard=True)
savol_dk.insert('Аёллар')
savol_dk.insert('Эркаклар')
savol_dk.add('🏡 Бош меню')

yes_no = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Ҳа",
                callback_data="yes"
            ),
            InlineKeyboardButton(
                text="♻️Йўқ қайта",
                callback_data="no_again"
            )
        ]
    ]
)
