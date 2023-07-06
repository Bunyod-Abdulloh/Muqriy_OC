from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

toshshahar_suhbat_video = {'1': '1151', '2': '1152', '3': '1153', '4': '1154', '5': ' 1155', '6': ' 1156', '7': ' 1157',
                           '8': '1158', '9': '1159', '10': '1160', '11': '1161', '12': '1162', '13': '1163',
                           '14': '1164', '15': '1165', '16': '1166', '17': '1167', '18': '1168'}

toshshahar_suhbat_audio = {'1': '1169', '2': '1170', '3': '1171', '4': '1172', '5': '1173', '6': '1174', '7': '1175',
                           '8': '1176', '9': '1177', '10': '1178', '11': '1179', '12': '1180', '13': '1181',
                           '14': '1182', '15': '1183', '16': '1184', '17': '1185', '18': '1186'}

tort_suhbat_video = {'1': '855', '2': '856', '3': '857', '4': '858', '5': '859', '6': '1885', '7': '1886', '8': '2019',
                     '9':'2021', '10':'2022', '11': '2025', '12': '2027', '13': '2030', '14': '2032'}

tort_suhbat_audio = {'1': '850', '2': '851', '3': '852', '4': '853', '5': '854', '6': '2018', '7': '2017', '8': '2020',
                     '9':'2023', '10':'2024', '11': '2026', '12': '2028', '13': '2031', '14': '2033'}


async def ilm_suhbat_inkeys(back=False, torttoplam=False, toshshahar_one=False):
    markup = InlineKeyboardMarkup(row_width=6)
    if back:
        markup.insert(InlineKeyboardButton(text='⬅ Ортга', callback_data='back_tash_suh1'))
    elif toshshahar_one:
        for key in toshshahar_suhbat_audio.keys():
            markup.insert(InlineKeyboardButton(text=key, callback_data=key))
        markup.add(InlineKeyboardButton(text='⬅ Ортга', callback_data='back_tash_suh2'))
    elif torttoplam:
        for key in tort_suhbat_video.keys():
            markup.insert(InlineKeyboardButton(text=key, callback_data=key))
        markup.add(InlineKeyboardButton(text='⬅ Ортга', callback_data='back_tash_suh2'))
    return markup
