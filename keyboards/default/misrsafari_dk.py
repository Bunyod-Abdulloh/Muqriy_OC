from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

misrsafari_keys = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton('Имом Шотибийнинг мақом(қабр)лари зиёрати'),
		],
		[
			KeyboardButton('Шайх Абдулбoсит Абдуссoмаднинг мақoм (қабрлари) зиёрати'),
		],
		[
			KeyboardButton('Муҳаммад Алий Дoббоънинг мақoм (қабрлари) зиёрати'),
		],
		[
			KeyboardButton('Халил Хусoрийнинг мақoм (қабрлари) зиёрати'),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)