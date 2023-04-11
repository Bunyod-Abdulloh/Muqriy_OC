from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

nang_umum_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🏡 Бош меню"),
		],
		[
			KeyboardButton("🎧 Аyдиo"),
			KeyboardButton("🎬 Bидeo"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

nang_aud_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("⏮ Oлдинги"),
			KeyboardButton("🏡 Бош меню"),
		],
		[
			KeyboardButton("1-3 суҳбатлар"),
			KeyboardButton("4-6 суҳбатлар"),
			KeyboardButton("7-9 суҳбатлар"),
		],
		[
			KeyboardButton("10-12 суҳбатлар"),
			KeyboardButton("13-15 суҳбатлар"),
			KeyboardButton("16 - суҳбат"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

nang_vid_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("⏮ Oлдинги"),
			KeyboardButton("🏡 Бош меню"),
		],
		[
			KeyboardButton("1-cyҳбат"),
			KeyboardButton("2-cyҳбат"),
			KeyboardButton("3-cyҳбат"),
			KeyboardButton("4-cyҳбат"),
		],
		[
			KeyboardButton("5-cyҳбат"),
			KeyboardButton("6-cyҳбат"),
			KeyboardButton("7-cyҳбат"),
			KeyboardButton("8-cyҳбат"),
		],
		[
			KeyboardButton("9-cyҳбат"),
			KeyboardButton("10-cyҳбат"),
			KeyboardButton("11-cyҳбат"),
		],
		[
			KeyboardButton("12-cyҳбат"),
			KeyboardButton("13-cyҳбат"),
			KeyboardButton("14-cyҳбат"),
		],
		[
			KeyboardButton("15-cyҳбат"),
			KeyboardButton("16-cyҳбат"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)