from aiogram import types

from aiogram.dispatcher import FSMContext
from keyboards.default.mavlid_dk import mbm_dk,m1_dk,sharif_dk,m1_dict,m2_dict,sh_dict
from loader import dp,bot

CHANNEL_ID = -1001705654629

habar = "Қуйидаги тугмалардан бирини танланг:"

@dp.message_handler(text = "🔆 Мавлид", state="*")
async def mavlidumumiy(msg: types.Message, state:FSMContext):
	await msg.answer("🔆 Мавлид",
					 reply_markup = await mbm_dk())
	await state.set_state("mavlid_state")

@dp.message_handler(state="mavlid_state")
async def mavlidvideo(msg: types.Message, state:FSMContext):
	if msg.text == "🎧 Ayдио":
		await msg.answer(msg.text,
						 reply_markup = await m1_dk())
		await state.set_state('mavlid_audio')
	elif msg.text == "🎬 Bидeо":
		await msg.answer(msg.text,
						 reply_markup = await m1_dk())
		await state.set_state('mavlid_video')
	elif msg.text == 'Мавлиди Шариф':
		await msg.answer(msg.text,
						 reply_markup = await sharif_dk())
		await state.set_state('mavlid_sharif')
	else:
		await msg.answer(habar)

@dp.message_handler(state="mavlid_video")
async def mavlidv(msg: types.Message, state:FSMContext):
	if msg.text in m2_dict.keys():
		for n in m2_dict[msg.text]:
			await bot.copy_message(chat_id=msg.from_user.id,
								   from_chat_id=CHANNEL_ID,
								   message_id=n)
	elif msg.text == "⏮ Олдинги":
		await msg.answer(msg.text,
						 reply_markup = await mbm_dk())
		await state.set_state('mavlid_state')
	else:
		await msg.answer(habar)

@dp.message_handler(state="mavlid_audio")
async def mavlidvideo(msg: types.Message, state:FSMContext):
	if msg.text in m1_dict.keys():
		for n in m1_dict[msg.text]:
			await bot.copy_message(chat_id=msg.from_user.id,
								   from_chat_id=CHANNEL_ID,
								   message_id=n)
	elif msg.text == "⏮ Олдинги":
		await msg.answer(msg.text,
						 reply_markup = await mbm_dk())
		await state.set_state('mavlid_state')
	else:
		await msg.answer(habar)

@dp.message_handler(state="mavlid_sharif")
async def mavlidvideo(msg: types.Message, state:FSMContext):
	if msg.text in sh_dict.keys():
		for n in sh_dict[msg.text]:
			await bot.copy_message(chat_id=msg.from_user.id,
								   from_chat_id=CHANNEL_ID,
								   message_id=n)
	elif msg.text == "⏮ Олдинги":
		await msg.answer(msg.text,
						 reply_markup = await mbm_dk())
		await state.set_state('mavlid_state')
	else:
		await msg.answer(habar)