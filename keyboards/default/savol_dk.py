from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

savol_ck = ReplyKeyboardMarkup(resize_keyboard=True)
savol_ck.insert('Аёллар')
savol_ck.insert('Эркаклар')
savol_ck.add('🏡 Бош меню')

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
