from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

t1443_m = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton(text="🎧 Aудиo"),
			KeyboardButton(text="🎬 Bидеo"),
		],
	],
	resize_keyboard = True,
	one_time_keyboard = True
)

t1443_av = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="⏮ Oлдинги"),
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton("1 - 3 кунлар"),
			KeyboardButton("4 - 6 кунлар"),
			KeyboardButton("7 - 9 кунлар"),
		],
		[
			KeyboardButton("10 - 12 кунлар"),
			KeyboardButton("13 - 15 кунлар"),
			KeyboardButton("16 - 18 кунлар"),
		],
		[
			KeyboardButton("19 - 21 кунлар"),
			KeyboardButton("22 - 24 кунлар"),
			KeyboardButton("25 - 27 кунлар"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)