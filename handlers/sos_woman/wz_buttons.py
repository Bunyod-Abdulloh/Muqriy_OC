from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import sdb


async def wbutton_one():
    user = await sdb.select_question_woman()
    markup = InlineKeyboardMarkup(row_width=2)
    for n in user:
        markup.insert(InlineKeyboardButton(text=f"{n[0]}", callback_data=f"{n[1]}"))
    return markup
