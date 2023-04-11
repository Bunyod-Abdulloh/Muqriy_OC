from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

istiloh_sharh_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton("Мусҳаф истилоҳлари шарҳи (1-қисм)"), #hammasi o'zbek kirillda
		],
		[
			KeyboardButton("Мусҳаф истилоҳлари шарҳи (2-қисм)"),
		],
		[
			KeyboardButton("Мусҳаф истилоҳлари шарҳи (3-қисм)"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

istiloh_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("⏮ Oлдинги"),
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton("Суҳбатнинг тўлиқ шакли")
		],
		[
			KeyboardButton("Суҳбатнинг қисмларга бўлинган шакли")
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)
