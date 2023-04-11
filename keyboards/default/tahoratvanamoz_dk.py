from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

na = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🏡 Бош меню"),
			KeyboardButton("Таҳорат"),
		],
		[
			KeyboardButton("Биринчи ракъат. Ният"),
		],
		[
			KeyboardButton("Такбири таҳрима"),
			KeyboardButton("Қиём"),
			KeyboardButton("Рукуъ"),
		],
		[
			KeyboardButton("Рукуъдан туриш"),
			KeyboardButton("Cажда"),
		],
		[
			KeyboardButton("Жалса - саждадан туриш"),
		],
		[
			KeyboardButton("Caждa"),
			KeyboardButton("Иккинчи ракъат"),
		],
		[
			KeyboardButton("Қаъда"),
			KeyboardButton("Салом"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)