from aiogram import types
from loader import dp
from states.data import Edit
from keyboards.inline.qversein import keyingi, next_callback
from keyboards.default.qversedk import lugat

@dp.callback_query_handler(next_callback.filter(get='oldingi'), state=Edit.a)
async def bool(call: types.CallbackQuery, callback_data: dict):
	info = callback_data["info"].split("_")


	oyat = str(int(info[1]) - 1)
	if len(oyat) == 2:
		oyat = "0" + oyat

	elif len(oyat) == 1:
		oyat = "00" + oyat

	photo_link = f"https://www.everyayah.com/data/images_png/{int(info[0])}_{int(info[1])-1}.png"
	await call.message.edit_reply_markup()
	await call.message.answer_photo(photo=photo_link)

	audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{info[0]}{oyat}.mp3"
	# if info[1] == "145" and info[0] == "001":
	# 	await call.message.answer_audio(audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE",
	# 	                                reply_markup=await keyingi(f'{info[0]}_{oyat}'))
	# else:
	await call.message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{info[0]}_{oyat}'))

	await Edit.a.set()

@dp.callback_query_handler(next_callback.filter(get='oldingi'), state=Edit.b)
async def bool(call: types.CallbackQuery, callback_data: dict):
	info = callback_data["info"].split("_")

	oyat = str(int(info[1]) - 1)
	if len(oyat) == 2:
		oyat = "0" + oyat

	elif len(oyat) == 1:
		oyat = "00" + oyat

	photo_link = f"https://www.everyayah.com/data/images_png/{int(info[0])}_{int(info[1])-1}.png"
	await call.message.edit_reply_markup()

	await call.message.answer_photo(photo=photo_link)

	audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{info[0]}{oyat}.mp3"

	# if info[1] == "145" and info[0] == "001":
	# 	await call.message.answer_audio(
	# 		audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE")
	# else:
	await call.message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{info[0]}_{oyat}'))

	await Edit.b.set()

@dp.callback_query_handler(next_callback.filter(get='oldingi'), state=Edit.d)
async def bool(call: types.CallbackQuery, callback_data: dict):
	info = callback_data["info"].split("_")


	oyat = str(int(info[1]) - 1)
	if len(oyat) == 2:
		oyat = "0" + oyat

	elif len(oyat) == 1:
		oyat = "00" + oyat

	photo_link = f"https://www.everyayah.com/data/images_png/{int(info[0])}_{int(info[1])-1}.png"
	await call.message.edit_reply_markup()

	await call.message.answer_photo(photo=photo_link)

	audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{info[0]}{oyat}.mp3"
	#
	# if info[1] == "145" and info[0] == "001":
	# 	await call.message.answer_audio(
	# 		audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE")
	# else:
	await call.message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{info[0]}_{oyat}'))

	await Edit.d.set()

@dp.callback_query_handler(next_callback.filter(get='keyingi'), state=Edit.a)
async def bool(call: types.CallbackQuery, callback_data: dict):
	info = callback_data["info"].split("_")


	oyat = str(int(info[1]) + 1)
	if len(oyat) == 2:
		oyat = "0" + oyat

	elif len(oyat) == 1:
		oyat = "00" + oyat

	photo_link = f"https://www.everyayah.com/data/images_png/{int(info[0])}_{int(info[1])+1}.png"
	await call.message.edit_reply_markup()

	await call.message.answer_photo(photo=photo_link)

	audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{info[0]}{oyat}.mp3"

	# if info[1] == "145" and info[0] == "001":
	# 	await call.message.answer_audio(
	# 		audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE",
	# 		reply_markup=await keyingi(f'{info[0]}_{oyat}'))
	# else:
	await call.message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{info[0]}_{oyat}'))

	await Edit.a.set()

@dp.callback_query_handler(next_callback.filter(get='keyingi'), state=Edit.b)
async def bool(call: types.CallbackQuery, callback_data: dict):
	info = callback_data["info"].split("_")


	oyat = str(int(info[1]) + 1)
	if len(oyat) == 2:
		oyat = "0" + oyat

	elif len(oyat) == 1:
		oyat = "00" + oyat

	photo_link = f"https://www.everyayah.com/data/images_png/{int(info[0])}_{int(info[1])+1}.png"
	await call.message.edit_reply_markup()

	await call.message.answer_photo(photo=photo_link)

	audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{info[0]}{oyat}.mp3"

	# if info[1] == "145" and info[0] == "001":
	# 	await call.message.answer_audio(
	# 		audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE")
	# else:
	await call.message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{info[0]}_{oyat}'))

	await Edit.b.set()

@dp.callback_query_handler(next_callback.filter(get='keyingi'), state=Edit.d)
async def bool(call: types.CallbackQuery, callback_data: dict):
	info = callback_data["info"].split("_")


	oyat = str(int(info[1]) + 1)
	if len(oyat) == 2:
		oyat = "0" + oyat

	elif len(oyat) == 1:
		oyat = "00" + oyat

	photo_link = f"https://www.everyayah.com/data/images_png/{int(info[0])}_{int(info[1])+1}.png"
	await call.message.edit_reply_markup()

	await call.message.answer_photo(photo=photo_link)

	audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{info[0]}{oyat}.mp3"

	# if info[1] == "145" and info[0] == "001":
	# 	await call.message.answer_audio(
	# 		audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE")
	# else:
	await call.message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{info[0]}_{oyat}'))

	await Edit.d.set()






