from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

next_callback = CallbackData('def', 'info', 'get')

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Обунани текшириш", callback_data='check_subs')
    ]]
)

async def keyingi(oyat, tek=False):
    keyingi_button = InlineKeyboardMarkup()
    info = oyat.split("_")

    if info[1] != "001":
        keyingi_button.insert(InlineKeyboardButton(text="⏪ Олдинги оят", callback_data=next_callback.new(info=oyat, get="oldingi")))

    if tek == False:
        keyingi_button.insert(InlineKeyboardButton(text="Кейинги оят ⏩",  callback_data=next_callback.new(info=oyat, get="keyingi")))
    return keyingi_button