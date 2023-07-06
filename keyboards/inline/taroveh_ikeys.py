from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


taroveh_1444 = InlineKeyboardMarkup(row_width=4)
for n in range(1, 28):
    taroveh_1444.insert(InlineKeyboardButton(text=f'{n}-kun', callback_data=f'{n}_kun'))
taroveh_1444.add(InlineKeyboardButton(text='Ortga', callback_data='taroveh_ortga'))
