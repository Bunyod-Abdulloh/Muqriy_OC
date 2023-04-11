from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

video_dict = {1: 7, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7: 13, 8: 14, 9: 15, 10: 16, 11: 17, 12: 18, 13: 19, 14: 20,
              15: 21, 16: 22, 17: 23, 18: 24, 19: 25, 20: 26, 21: 27, 22: 28, 23: 29, 24: 30, 25: 31}

audio_dict = {'1 - 5': [2, 3, 4, 5, 6], '6 - 10': [7, 8, 9, 10, 11], '11 - 15': [12, 13, 14, 15, 16],
              '16 - 20': [17, 18, 19, 20, 21], '21 - 25': [22, 23, 24, 25, 26]}


async def juma_suhbatlari_keys(audio=False, video=False):
    markup = InlineKeyboardMarkup(row_width=5)
    if audio:
        for key, value in audio_dict.items():
            markup.insert(InlineKeyboardButton(text=key, callback_data=key))
    elif video:
        for key, value in video_dict.items():
            markup.insert(InlineKeyboardButton(text=str(key), callback_data=str(key)))
    markup.add(InlineKeyboardButton(text='⬅ Ортга', callback_data='juma_back'))
    return markup

back_menyu_keys = InlineKeyboardMarkup(row_width=2)
back_menyu_keys.insert(InlineKeyboardButton(text='⬅ Ортга', callback_data='juma_back'))
