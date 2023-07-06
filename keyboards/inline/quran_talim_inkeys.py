from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

quran_tanishuv_audio = {'1 - 5': [261, 262, 263, 264, 265], '6 - 10': [266, 267, 268, 269, 270, 271],
                        '11 - 15': [272, 273, 274, 275, 276], '16 - 20': [277, 278, 279, 280, 281],
                        '21 - 26': [282, 283, 284, 285, 286, 287]}

quran_tanishuv_video = {1: [234], 2: [235], 3: [236], 4: [237], 5: [238], 6: [239], 7: [240], 8: [241], 9: [242, 243],
                        10: [244], 11: [245], 12: [246], 13: [247], 14: [248], 15: [249], 16: [250], 17: [251],
                        18: [252], 19: [253], 20: [254], 21: [255], 22: [256], 23: [257], 24: [258], 25: [259],
                        26: [260]}


async def quran_talimi_keys(audio=False, video=False):
    markup = InlineKeyboardMarkup(row_width=5)
    if audio:
        for key in quran_tanishuv_audio.keys():
            markup.insert(InlineKeyboardButton(text=key, callback_data=key))
    elif video:
        for key in quran_tanishuv_video.keys():
            markup.insert(InlineKeyboardButton(text=str(key), callback_data=str(key)))
    markup.add(InlineKeyboardButton(text='⬅ Ортга', callback_data='ortga'))
    return markup


iqro_keys = {1: [393], 2: [394, 395], 3: [396, 397], 4: [398, 399], 5: [400, 401], 6: [402, 403], 7: [404, 405],
             8: [406, 407], 9: [408, 409], 10: [410, 411], 11: [412, 413], 12: [414, 415], 13: [416, 417],
             14: [418, 419], 15: [420, 421], 16: [422, 423], 17: [424, 425], 18: [426, 427], 19: [428, 429],
             20: [430, 431], 21: [432, 433], 22: [434, 435]}


async def iqro_inkeys():
    markup = InlineKeyboardMarkup(row_width=5)
    for key in iqro_keys.keys():
        markup.insert(InlineKeyboardButton(text=str(key), callback_data=str(key)))
    markup.add(InlineKeyboardButton(text='⬅ Ортга', callback_data='ortga'))
    return markup


on_kecha_all = InlineKeyboardMarkup(row_width=1)
on_kecha_all.insert(InlineKeyboardButton(text='Биринчи босқич', callback_data='bir_bos'))
on_kecha_all.insert(InlineKeyboardButton(text='Иккинчи босқич', callback_data='ikki_bos'))
on_kecha_all.insert(InlineKeyboardButton(text='Учинчи босқич', callback_data='uch_bos'))

on_kecha_bir = {'Анонс': [323], 'Муқаддима': [324], 1: [325, 326], 2: [327, 328], 3: [329, 330], 4: [331, 332],
                5: [333, 334], 'Вазифаларни бажариш бўйича тавсиялар': [335], 6: [336, 337], 7: [338, 339],
                8: [340, 341], 9: [342, 343], 10: [344, 345], 'Савол - жавоблар': [346]}



# bir = []
# ikki = []
# for n in range(1, 6):
#     bir.append(n)
#
# for n in range(336, 346):
#     ikki.append(n)
#
# dic = {}
#
# for i in range(0, len(bir)):
#     dic[bir[i]] = ikki[i]
#
# print(bir)
# print(ikki)
