from aiogram.types import Message, CallbackQuery
from keyboards.default.muqriyverse_buttons import suralar_keyboard, suralar_dict, suralar_default_keys, suralar_default
from keyboards.inline.muqriyverse import muqriyverse_link
from aiogram.dispatcher import FSMContext
from loader import dp, bot

CHANNEL_ID = -1001758167153

state1 = 'state1'
state2 = 'state2'

@dp.message_handler(text = 'salom')
async def muqriyverse(msg:Message):
	await msg.answer(msg.text, reply_markup=suralar_default_keys)

@dp.message_handler(text = suralar_default, state="*")
async def suralar_default_func(msg:Message, state:FSMContext):
	await msg.answer(msg.text, reply_markup=suralar_keyboard)
	await state.set_state(state1)

@dp.callback_query_handler(state=state1)
async def muqriyquran(call:CallbackQuery, state:FSMContext):
	oyat_soni = suralar_dict[call.data]['oyat_soni']
	toliq = suralar_dict[call.data]['toliq']
	arxiv = suralar_dict[call.data]['zip']
	link= suralar_dict[call.data]['link']
	await state.update_data({'data':call.data})
	await bot.copy_message(chat_id=call.from_user.id,from_chat_id=CHANNEL_ID,message_id=toliq, reply_markup=await muqriyverse_link(link))
	await bot.copy_message(chat_id=call.from_user.id,from_chat_id=CHANNEL_ID,message_id=arxiv)
	await call.message.answer(f'Оят тартиб рақамини киритинг: (1 - {oyat_soni} гача)')
	await call.message.delete()
	await state.set_state(state2)

@dp.message_handler(state=state2)
async def fotiha(msg:Message, state:FSMContext):

	data = await state.get_data()
	calldata = data['data']
	oyat_soni = suralar_dict[calldata]['oyat_soni']

	if msg.text.isdigit():
		if int(msg.text) <= int(oyat_soni):
			screen = suralar_dict[calldata]['screen'][msg.text]
			audio = suralar_dict[calldata]['audio'][msg.text]
			if calldata == 'fotiha':
				basmala_screen = suralar_dict[calldata]['screen']['basmala']
				basmala_audio = suralar_dict[calldata]['audio']['basmala']

				if msg.text == '1':
					await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL_ID, message_id=basmala_screen)
					await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL_ID, message_id=basmala_audio)
					await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL_ID, message_id=screen)
					await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL_ID, message_id=audio)
				else:
					await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL_ID, message_id=screen)
					await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL_ID, message_id=audio)
			else:
				await bot.copy_message(chat_id=msg.from_user.id,from_chat_id=CHANNEL_ID,message_id=screen)
				await bot.copy_message(chat_id=msg.from_user.id,from_chat_id=CHANNEL_ID,message_id=audio)
		else:
			await msg.answer(f'Илтимос, фақат {oyat_soni} гача бўлган рақамлардан киритинг:')
	else:
		await msg.answer('Илтимос, фақат рақам киритинг:')