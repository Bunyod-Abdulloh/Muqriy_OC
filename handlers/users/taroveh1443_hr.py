from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from aiogram.dispatcher import FSMContext
from keyboards.default.taroveh1443_dk import t1443_m, t1443_av
from keyboards.default.start_dk import main_keyboard

from loader import dp, bot

@dp.message_handler(text = "📌 Таровеҳ намози 1443")
async def t1443m(msg:types.Message, state:FSMContext):
	await msg.answer("📌 Таровеҳ намози 1443", reply_markup=t1443_m)
	await state.set_state("t1443_m")

@dp.message_handler(state="t1443_m")
async def t1443mav(msg:types.Message, state:FSMContext):
	if msg.text == "🎬 Bидеo":
		await msg.answer("🎬 Bидеo",
		                 reply_markup=t1443_av)
		await state.set_state("t1443_v")

	if msg.text == "🎧 Aудиo":
		await msg.answer("🎧 Aудиo",
		                 reply_markup=t1443_av)
		await state.set_state("t1443_a")

islomuz = "\n\n<a href='https://www.facebook.com/hazratim.uz'>Facebook</a> | <a href='https://www.instagram.com/hazratim_uz/'>Instagram</a> | " \
          "<a href='https://t.me/joinchat/AAAAAFki3TLL4WCIyXw22g'>Telegram</a> | <a href='https://bit.ly/325lh5G'>Youtube</a>"

c1 = "«Шайх Муҳаммад Содиқ Муҳаммад Юсуф» жомеъ масжидида таровеҳ намозининг биринчи куни.\n\nФотиҳа сурасининг 1-оятидан Бақара сурасининг 141-оятигача." \
     "\n\nХатми Қуръонга масжид имом ноиби Ҳасанхон Яҳё Абдулмажид ва Муҳаммад Саид Усмон қорилар ўтиб беришади\n\n<a href='https://youtu.be/wYmzx8-IVl4'>Youtube орқали кўриш</a>",\
     "2-кун | Бақара сурасининг 142-оятидан 252-оятигача | 02.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/jfpjpGROCZ8'>Youtube орқали кўриш</a>",\
     "3-кун | Бақара сурасининг 253-оятидан Оли Имрон сураси 91-оятигача | 03.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/fQmsccU9KQc'>Youtube орқали кўриш</a>",\

c2 = "4-кун | Оли Имрон сурасининг 92-оятидан Нисо сурасининг 23-оятигача | 04.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/k7BMiyRA9UE'>Youtube орқали кўриш</a>",\
     "5-кун | Нисо сурасининг 24-оятидан 147-оятигача | 04.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/oRoThS0B9PE'>Youtube орқали кўриш</a>",\
     "6-кун | Нисо сурасининг 148-оятидан Моида сурасининг 81-оятигача | 06.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://www.youtube.com/watch?v=M80EektXtuo'>Youtube орқали кўриш</a>"

c3 = "7-кун | Моида сурасининг 82-оятидан Анʼом сурасининг 110-оятигача | 07.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/OEbihBX0pAU'>Youtube орқали кўриш</a>",\
     "8-кун | Анʼом сурасининг 111-оятидан Аъроф сурасининг 87-оятигача | 08.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/5KFSffX5li0'>Youtube орқали кўриш</a>",\
     "9-кун | Аъроф сурасининг 88-оятидан Анфол сурасининг 40-оятигача | 09.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/wlrLeL0yrPA'>Youtube орқали кўриш</a>"

c4 = "10-кун | Анфол сурасининг 41-оятидан Тавба сурасининг 93-оятигача | 10.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/MCYs8s4vlzo'>Youtube орқали кўриш</a>",\
     "11-кун | Тавба сурасининг 94-оятидан Юнус сурасининг 109-оятигача | 11.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/lnxWPnI9l4U'>Youtube орқали кўриш</a>",\
     "12-кун | Ҳуд сурасининг 1-оятидан Юсуф сурасининг 52-оятигача | 12.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/89dVC2UJurg'>Youtube орқали кўриш</a>"

c5 = "13-кун | Юсуф сурасининг 53-оятидан Иброҳим сурасининг 52-оятигача | 13.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/WmipbCuVMBg'>Youtube орқали кўриш</a>",\
     "14-кун | Ҳижр сурасининг 1-оятидан Наҳл сурасининг 128-оятигача | 14.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/xux9zGA2F7I'>Youtube орқали кўриш</a>",\
     "15-кун | Исро сурасининг 1-оятидан Каҳф сурасининг 74-оятигача | 15.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/5FZRDT_FRLQ'>Youtube орқали кўриш</a>"

c6 = "16-кун | Каҳф сурасининг 75-оятидан Тоҳа сурасининг 135-оятигача\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/I4cTCR8__Lg'>Youtube орқали кўриш</a>",\
     "17-кун | Анбиё сурасининг 1-оятидан Ҳаж сурасининг 78-оятигача | 17.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/ReqKSjAXo-M'>Youtube орқали кўриш</a>",\
     "18-кун | Муъминун сурасининг 1-оятидан Фурқон сурасининг 20-оятигача | 18.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/ETtb4Nq5Phw'>Youtube орқали кўриш</a>"

c7 = "19-кун | Фурқон сурасининг 21-оятидан Намл сурасининг 55-оятигача | 19.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/cA8D9hiygHw'>Youtube орқали кўриш</a>",\
     "20-кун | Қосос сурасининг 1-оятидан Рум сурасининг 60-оятигача | 20.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/VqS6HJ_4_x8'>Youtube орқали кўриш</a>",\
     "21-кун | Луқмон сурасининг 1-оятидан Фотир сурасининг 45-оятигача | 21.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/McH6xckJnUs'>Youtube орқали кўриш</a>"

c8 = "22-кун | Ясин сурасининг 1-оятидан Зумар сурасининг 75-оятигача | 22.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/_dpPisxcZoo'>Youtube орқали кўриш</a>",\
     "23-кун | Ғофир сурасининг 1-оятидан Зухруф сурасининг 89-оятигача | 23.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/AAB6KgZheGQ'>Youtube орқали кўриш</a>",\
     "24-кун | Духон сурасининг 1-оятидан Тур сурасининг 49-оятигача | 24.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/3tDfV78TUVs'>Youtube орқали кўриш</a>"

c9 = "25-кун | Тур сурасининг 1-оятидан Софф сурасининг 14-оятигача | 25.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/VQDoIM2-E7g'>Youtube орқали кўриш</a>",\
     "26-кун | Талоқ сурасининг 1-оятидан Буруж сурасининг 22-оятигача | 26.04.2022\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/Tke-MJSf_7I'>Youtube орқали кўриш</a>",\
     "Хатми Қуръонга марҳабо! | 27-кун | Қадр кечаси | Буруж сурасидан Ан-Нас сурасигача\n\nҚорилар:\nҲасанхон қори Яҳё Абдулмажид\nМуҳаммад Саййид Муҳаммад Айюб ўғли\n\n<a href='https://youtu.be/nVZUiTr7aLM'>Youtube орқали кўриш</a>"

hasanalmuqriyid = -1001705654629 # kanal id si

@dp.message_handler(state="t1443_v")
async def send_messages(message: types.Message, state:FSMContext):
	if message.text == "1 - 3 кунлар":

		id1 = 2 # kanaldagi fayllarning id raqamlari
		id2 = 4
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c1[n - 2]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "4 - 6 кунлар":
		id1 = 5
		id2 = 7
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c2[n - 5]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "7 - 9 кунлар":
		id1 = 8
		id2 = 10
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c3[n - 8]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "10 - 12 кунлар":
		id1 = 11
		id2 = 13
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c4[n - 11]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "13 - 15 кунлар":
		id1 = 14
		id2 = 16
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c5[n - 14]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "16 - 18 кунлар":
		id1 = 17
		id2 = 19
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c6[n - 17]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "19 - 21 кунлар":
		id1 = 20
		id2 = 22
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c7[n - 20]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "22 - 24 кунлар":
		id1 = 23
		id2 = 25
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c8[n - 23]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "25 - 27 кунлар":
		id1 = 26
		id2 = 28
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c9[n - 26]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	elif message.text == "⏮ Oлдинги":
		await message.answer("⏮ Oлдинги",
		                     reply_markup=t1443_m)
		await state.set_state("t1443_m")

@dp.message_handler(state="t1443_a")
async def send_messages(message: types.Message, state:FSMContext):
	if message.text == "1 - 3 кунлар":
		id1 = 31
		id2 = 33
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c1[n - 31]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "4 - 6 кунлар":
		id1 = 34
		id2 = 36
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c2[n - 34]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "7 - 9 кунлар":
		id1 = 37
		id2 = 39
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c3[n - 37]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "10 - 12 кунлар":
		id1 = 40
		id2 = 42
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c4[n - 40]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "13 - 15 кунлар":
		id1 = 43
		id2 = 45
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c5[n - 43]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "16 - 18 кунлар":
		id1 = 46
		id2 = 48
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c6[n - 46]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "19 - 21 кунлар":
		id1 = 49
		id2 = 51
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c7[n - 49]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "22 - 24 кунлар":
		id1 = 52
		id2 = 54
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c8[n - 52]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	if message.text == "25 - 27 кунлар":
		id1 = 55
		id2 = 57
		for n in range(id1, id2 + 1):
			try:
				await bot.copy_message(chat_id=message.from_user.id,
				                       from_chat_id=hasanalmuqriyid,
				                       message_id=n,
				                       caption=f"{c9[n - 55]} {islomuz}")
			except Exception as err:
				await message.answer(err)

	elif message.text == "⏮ Oлдинги":
		await message.answer("⏮ Oлдинги",
		                     reply_markup=t1443_m)
		await state.set_state("t1443_m")