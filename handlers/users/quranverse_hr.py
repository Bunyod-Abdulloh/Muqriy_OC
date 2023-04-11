from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.qversein import keyingi
from loader import dp, db
from states.data import Edit
from keyboards.default.qversedk import suralar38gacha, suralar76gacha, suralar114gacha, lugat
from keyboards.default.start_dk import main_keyboard

@dp.message_handler(text="🎧 \"Қуръони карим\" тиловати \n(таълим услубида)")
async def quranverse(msg: types.Message):
	await msg.answer("🎧 \"Қуръони карим\" тиловати \n(таълим услубида)",
					 reply_markup=await suralar38gacha())
	await Edit.a.set()

@dp.message_handler(state=Edit.a)
async def sura(message: types.Message, state: FSMContext):
	# if message.text == "📖 Йўриқнома":
	# 	await message.answer("📖 Йўриқнома\n\nhttps://telegra.ph/Quroni-Karim-talim-uslubida-12-10")
	if message.text == "🏡 Бош меню":
		await message.answer("🏡 Бош меню", reply_markup=main_keyboard)
		await state.reset_state(with_data=True)

	elif message.text == "Кейинги ⏭":
		await message.answer("Кейинги ⏭", reply_markup=await suralar76gacha())
		await Edit.b.set()

	elif message.text in lugat.keys():
		await message.answer_audio(audio=lugat[message.text]["audio"])
		await message.answer_document(document=lugat[message.text]["zip"])
		await message.answer(f"Оят тартиб рақамини киритинг: (1-{lugat[message.text]['oyat_soni']} гача)")
		await state.update_data({
			"sura": message.text
		})
		await Edit.a.set()

	elif message.text.isdigit() and len(message.text) < 4 :

		data = await state.get_data()
		sura = data["sura"]

		if int(message.text) > lugat[sura]['oyat_soni']:
			await message.answer(f"Оят тартиб рақамини киритинг: (1-{lugat[sura]['oyat_soni']} гача)")
			await Edit.a.set()
			return

		ind = str(list(lugat.keys()).index(sura)+1)
		oyat = message.text
		photo_link = f"https://www.everyayah.com/data/images_png/{ind}_{oyat}.png"
		tek = True

		if lugat[sura]['oyat_soni'] != int(message.text):
			tek = False

		if len(ind) == 2:
			ind = "0"  + str(ind)

		elif len(ind) == 1:
			ind = "00"  + str(ind)

		if len(message.text) == 2:
			oyat = "0" + message.text

		elif len(message.text) == 1:
			oyat = "00" + message.text

		await message.answer_photo(photo=photo_link)

		audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{ind}{oyat}.mp3"

		# if message.text == "145" and ind == "002":
		# 	await message.answer_audio(audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE",
		# 	                           reply_markup=await keyingi(f'{ind}_{oyat}', tek))
		# else:
		await message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{ind}_{oyat}', tek))

@dp.message_handler(state=Edit.b)
async def sura(message: types.Message, state: FSMContext):
	if message.text == "🏡 Бош меню":
		await message.answer("🏡 Бош меню", reply_markup=main_keyboard)
		await state.reset_state(with_data=True)

	elif message.text == "⏪ Олдинги":
		await message.answer("⏪ Олдинги", reply_markup=await suralar38gacha())
		await Edit.a.set()

	elif message.text == "Кейинги ⏭":
		await message.answer("Кейинги ⏭", reply_markup=await suralar114gacha())
		await Edit.d.set()


	elif message.text in lugat.keys():

		await message.answer_audio(audio=lugat[message.text]["audio"])

		await message.answer_document(document=lugat[message.text]["zip"])

		await message.answer(f"Оят тартиб рақамини киритинг: (1-{lugat[message.text]['oyat_soni']} гача)")

		await state.update_data({

			"sura": message.text

		})

		await Edit.b.set()


	elif message.text.isdigit() and len(message.text) < 4:

		data = await state.get_data()

		sura = data["sura"]

		if int(message.text) > lugat[sura]['oyat_soni']:
			await message.answer(f"Оят тартиб рақамини киритинг: (1-{lugat[sura]['oyat_soni']} гача)")

			await Edit.b.set()

			return

		ind = str(list(lugat.keys()).index(sura) + 1)

		oyat = message.text

		photo_link = f"https://www.everyayah.com/data/images_png/{ind}_{oyat}.png"

		tek = True

		if lugat[sura]['oyat_soni'] != int(message.text):
			tek = False

		if len(ind) == 2:

			ind = "0" + str(ind)


		elif len(ind) == 1:

			ind = "00" + str(ind)

		if len(message.text) == 2:

			oyat = "0" + message.text


		elif len(message.text) == 1:

			oyat = "00" + message.text

		audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{ind}{oyat}.mp3"

		# if message.text == "145" and ind == "002":
		#
		# 	await message.answer_audio(audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE")
		#
		# else:
		#
		await message.answer_photo(photo=photo_link)

		await message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{ind}_{oyat}', tek))

@dp.message_handler(state=Edit.d)
async def sura(message: types.Message, state: FSMContext):
	if message.text == "🏡 Бош меню":
		await message.answer("🏡 Бош меню", reply_markup=main_keyboard)
		await state.reset_state(with_data=True)

	elif message.text == "⏪ Олдинги":
		await message.answer("⏪ Олдинги", reply_markup=await suralar76gacha())
		await Edit.b.set()


	elif message.text in lugat.keys():

		await message.answer_audio(audio=lugat[message.text]["audio"])

		await message.answer_document(document=lugat[message.text]["zip"])

		await message.answer(f"Оят тартиб рақамини киритинг: (1-{lugat[message.text]['oyat_soni']} гача)")

		await state.update_data({

			"sura": message.text

		})

		await Edit.d.set()


	elif message.text.isdigit() and len(message.text) < 4:

		data = await state.get_data()

		sura = data["sura"]

		if int(message.text) > lugat[sura]['oyat_soni']:
			await message.answer(f"Оят тартиб рақамини киритинг: (1-{lugat[sura]['oyat_soni']} гача)")

			await Edit.d.set()

			return

		ind = str(list(lugat.keys()).index(sura) + 1)

		oyat = message.text

		photo_link = f"https://www.everyayah.com/data/images_png/{ind}_{oyat}.png"

		tek = True

		if lugat[sura]['oyat_soni'] != int(message.text):
			tek = False

		if len(ind) == 2:

			ind = "0" + str(ind)


		elif len(ind) == 1:

			ind = "00" + str(ind)

		if len(message.text) == 2:

			oyat = "0" + message.text


		elif len(message.text) == 1:

			oyat = "00" + message.text

		audio_link = f"https://www.everyayah.com/data/Husary_Muallim_128kbps/{ind}{oyat}.mp3"

		# if message.text == "145" and ind == "002":
		#
		# 	await message.answer_audio(audio="CQACAgIAAxkBAAEJ6fJjDWNWtaZSd8BdWd53y4ollzcl5AACnR4AAgtIcEgGW6QSaWV8dSkE")
		#
		# else:
		#
		await message.answer_photo(photo=photo_link)

		await message.answer_audio(audio=audio_link, reply_markup=await keyingi(f'{ind}_{oyat}', tek))
