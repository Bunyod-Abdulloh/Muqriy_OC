from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

iqro_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🏡 Бош меню")
		],
		[
			KeyboardButton("1-сон"),
			KeyboardButton("2-сон"),
			KeyboardButton("3-сон"),
			KeyboardButton("4-сон"),
		],
		[
			KeyboardButton("5-сон"),
			KeyboardButton("6-сон"),
			KeyboardButton("7-сон"),
			KeyboardButton("8-сон"),
		],
		[
			KeyboardButton("9-сон"),
			KeyboardButton("10-сон"),
			KeyboardButton("11-сон"),
			KeyboardButton("12-сон"),
		],
		[
			KeyboardButton("13-сон"),
			KeyboardButton("14-сон"),
			KeyboardButton("15-сон"),
			KeyboardButton("16-сон"),
		],
		[
			KeyboardButton("17-сон"),
			KeyboardButton("18-сон"),
			KeyboardButton("19-сон"),
			KeyboardButton("20-сон"),
		],
		[
			KeyboardButton("21-сон"),
			KeyboardButton("22-сон"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)