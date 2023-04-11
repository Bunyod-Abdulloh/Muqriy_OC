from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

quran_m = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🏡 Бош меню"),
		],
		[
			KeyboardButton("🎧 Ayдиo"),
			KeyboardButton("🎬 Видео"),

		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

