from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from loader import dp
from keyboards.default.misrsafari_dk import misrsafari_keys

@dp.message_handler(text="🏜 Миср сафари")
async def misrsafari(msg: types.Message):
	await msg.answer("🏜 Миср сафари", reply_markup=misrsafari_keys)

islom_uz = '\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz_kanal/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/user/islomuz?sub_confirmation=1\'>Youtube</a>'

misr_dict = {1:{'v':'BAACAgIAAxkBAAEEvepipRYCt8w7n7Kbp4Azi0KcKmDViwACvxsAAtXkKUk0EBkyxmsS-CQE','c':'<b>Имом Шотибийнинг мақом(қабр)лари зиёрати</b>\n\n<a href=\'https://youtu.be/NPwnKz3RiYU\'>Youtube орқали кўриш</a>'},2: {'v': 'BAACAgIAAxkBAAEEvdRipRG1HCk_Maa3mIiggDn5Jo4NvwAC0BsAAmmmMUidI87bWbWZhCQE','c': '<b>Шайх Абдулбoсит Абдуссoмаднинг мақoм (қабрлари) зиёрати</b>\n\n<a href=\'https://youtu.be/oKTO4bQqod0\'>Youtube орқали кўриш</a>'},3: {'v': 'BAACAgIAAxkBAAEEvdZipRHQTNcjieGv92utro0VoSNE6QACThcAAlF1yEgnl31GFxwv0CQE','c': '<b>Муҳаммад Алий Дoббоънинг мақoм (қабрлари) зиёрати</b>\n\n<a href=\'https://youtu.be/uuzaAA61_AU\'>Youtube орқали кўриш</a>'},4: {'v': 'BAACAgIAAxkBAAEEvdhipRHYSBoOIEuurdXLghqLCGFi2AACbxgAArX6eUgxDsrOGmWUNiQE','c': '<b>Халил Хусoрийнинг мақoм (қабрлари) зиёрати</b>\n\n<a href=\'https://youtu.be/ZBiW35wXGoM\'>Youtube орқали кўриш</a>'}}

@dp.message_handler(text="Имом Шотибийнинг мақом(қабр)лари зиёрати")
async def misrsafar(msg: types.Message):
	await msg.answer_video(video=misr_dict[1]['v'], caption=misr_dict[1]['c'] + islom_uz)

@dp.message_handler(text="Шайх Абдулбoсит Абдуссoмаднинг мақoм (қабрлари) зиёрати")
async def misrsafari(msg: types.Message):
	await msg.answer_video(video=misr_dict[2]['v'], caption=misr_dict[2]['c'] + islom_uz)

@dp.message_handler(text="Муҳаммад Алий Дoббоънинг мақoм (қабрлари) зиёрати")
async def misrsafari(msg: types.Message):
	await msg.answer_video(video=misr_dict[3]['v'], caption=misr_dict[3]['c'] + islom_uz)

@dp.message_handler(text="Халил Хусoрийнинг мақoм (қабрлари) зиёрати")
async def misrsafari(msg: types.Message):
	await msg.answer_video(video=misr_dict[4]['v'], caption=misr_dict[4]['c'] + islom_uz)
