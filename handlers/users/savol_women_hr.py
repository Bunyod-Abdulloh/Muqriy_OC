from aiogram import types
from filters import TextReply, PhotoReply, AudioReply, VideoReply
from keyboards.default.savol_dk import yes_no
from aiogram.dispatcher import FSMContext
from handlers.users.savol_reply_functions_hr import text_reply_func, photo_reply_func, audio_reply_func, video_reply_func
from handlers.users.savol_get_and_send_functions_hr import text_func, photo_func, audio_func, video_func
from data.config import ID_WOMEN_GROUP
from loader import dp

@dp.message_handler(text="Аёллар", state="*")
async def ayollar_fa(msg: types.Message, state: FSMContext):
	await msg.answer("<b><i>Илтимос, эътибор қилинг! Биз фақат ботга оид саволларга жавоб берамиз!</i></b>"
					 "\n\nСаволингизни юборишингиз мумкин:")
	await state.set_state("get_text_w")

@dp.message_handler(content_types=['audio','video','photo','text'], state="get_text_w")
async def get_and_send_fa(msg: types.Message, state: FSMContext):
	if msg.text:
		amatn = msg.text
		await msg.answer("Саволингизни текширдингизми?\n"
						 "Юборасизми?",
						 reply_markup=yes_no
						 )
		await state.update_data(
			matn=amatn
		)
		await state.set_state("women_text")
	elif msg.photo:
		rasm = msg.photo[-1].file_id
		caption = msg.caption
		await msg.answer("Саволингизни текширдингизми?\n"
						 "Юборасизми?",
						 reply_markup=yes_no
						 )
		await state.update_data(
			rasm=rasm,
			caption=caption
		)
		await state.set_state("women_photo")
	elif msg.audio:
		audio = msg.audio.file_id
		caption = msg.caption
		await msg.answer("Саволингизни текширдингизми?\n"
						 "Юборасизми?",
						 reply_markup=yes_no
						 )
		await state.update_data(
			audio=audio,
			caption=caption
		)
		await state.set_state("women_audio")
	elif msg.video:
		video = msg.video.file_id
		caption = msg.caption
		await msg.answer("Саволингизни текширдингизми?\n"
						 "Юборасизми?",
						 reply_markup=yes_no
						 )
		await state.update_data(
			video=video,
			caption=caption
		)
		await state.set_state("women_video")

@dp.callback_query_handler(state="women_text")
async def state_text_fa(call: types.CallbackQuery, state: FSMContext):
	data = await state.get_data()

	await text_func(call, ID_WOMEN_GROUP, data)
	await state.finish()

	if call.data == "no_again":
		await call.message.answer(
			"Саволингизни қайта юборишингиз мумкин!"
		)
		await state.set_state("get_text_w")

@dp.callback_query_handler(state="women_photo")
async def state_photo_fa(call: types.CallbackQuery, state: FSMContext):
	data = await state.get_data()
	await photo_func(call, ID_WOMEN_GROUP, data)
	await state.finish()

	if call.data == "no_again":
		await call.message.answer(
			"Саволингизни қайта юборишингиз мумкин!"
		)
		await state.set_state("get_text_w")

@dp.callback_query_handler(state="women_audio")
async def state_audio_fa(call: types.CallbackQuery, state: FSMContext):
	data = await state.get_data()
	await audio_func(call, ID_WOMEN_GROUP, data)
	await state.finish()

	if call.data == "no_again":
		await call.message.answer(
			"Саволингизни қайта юборишингиз мумкин!"
		)
		await state.set_state("get_text_w")

@dp.callback_query_handler(state="women_video")
async def state_video_fa(call: types.CallbackQuery, state: FSMContext):
	data = await state.get_data()
	await video_func(call, ID_WOMEN_GROUP, data)
	await state.finish()

	if call.data == "no_again":
		await call.message.answer(
			"Саволингизни қайта юборишингиз мумкин!"
		)
		await state.set_state("get_text_w")

@dp.message_handler(TextReply(), chat_id=ID_WOMEN_GROUP, content_types=['audio', 'voice', 'video', 'text', 'photo'], state="*")
async def text_filter_fa(message: types.Message):
	await text_reply_func(message)

@dp.message_handler(PhotoReply(), chat_id=ID_WOMEN_GROUP, content_types=['voice', 'text', 'photo','audio','video'], state="*")
async def photo_filter_fa(message: types.Message):
	await photo_reply_func(message)

@dp.message_handler(AudioReply(), chat_id=ID_WOMEN_GROUP, content_types=['voice','text','photo','audio','video'], state="*")
async def audio_filter_fa(message: types.Message):
	await audio_reply_func(message)

@dp.message_handler(VideoReply(), chat_id=ID_WOMEN_GROUP, content_types=['voice', 'text', 'photo','audio','video'], state="*")
async def video_filter_fa(message: types.Message):
	await video_reply_func(message)