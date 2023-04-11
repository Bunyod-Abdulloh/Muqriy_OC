from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def muqriyverse_link(link):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(InlineKeyboardButton(text='Сура ҳақида',
                                       url=link))
    return markup