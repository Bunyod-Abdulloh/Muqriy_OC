from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ram_m = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton(text="🎧 Aудиo"),  # o lotincha
			KeyboardButton(text="🎬 Bидеo"),  # o lotincha
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

ram_a1 = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="⏮ Oлдинги"),
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton('"Рaмaзон - Қуръон ойи"'),
			KeyboardButton('Қoрилaр ва тингловчиларга тавсиялар'),
		],
		[
			KeyboardButton('Сaвoл - жавоб'),
			KeyboardButton('Taровеҳ намозининг тарихини биласизми?'),
		],
		[
			KeyboardButton('Қyръoн ва рўза қиёматда шафоатчи бўлиб келади'),
			KeyboardButton('Xaтми Қуръон бағишлашнинг фиқҳий ҳукми'),
		],
		[
			KeyboardButton('Қyръoни карим ўхшаши йўқ мўъжиза'),
			KeyboardButton("Қисқа аудиолар"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

ram_a2 = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="⏮ Oлдинги"),
			KeyboardButton(text = "🏡 Бош меню"),
		],
		[
			KeyboardButton("Хатмга оид аудиолар"),
			KeyboardButton("Қуръонга оид аудиолар"),
		],
		[
			KeyboardButton("Рамазон ва таровеҳга оид аудиолар"),
		],
		[
			KeyboardButton("Умумий аудиолар"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

ram_v1 = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="⏮ Oлдинги"),
			KeyboardButton(text="🏡 Бош меню"),
		],
		[
			KeyboardButton('"Рамазон - Қуръон ойи"'),
			KeyboardButton('Қорилар ва тингловчиларга тавсиялар'),
		],
		[
			KeyboardButton('Савол - жавоб'),
			KeyboardButton('Таровеҳ намозининг тарихини биласизми?'),
		],
		[
			KeyboardButton('Қуръон ва рўза қиёматда шафоатчи бўлиб келади'),
			KeyboardButton('Хатми Қуръон бағишлашнинг фиқҳий ҳукми'),
		],
		[
			KeyboardButton('Қуръони карим ўхшаши йўқ мўъжиза'),
			KeyboardButton("Қисқa видеoлар"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

ram_v2 = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="⏮ Oлдинги"),
			KeyboardButton(text = "🏡 Бош меню"),
		],
		[
			KeyboardButton("Хaтмгa оид видеолар"),
			KeyboardButton("Қуръонгa оид видеолар"),
		],
		[
			KeyboardButton("Рамазон ва таровеҳга оид видеолар"),
		],
		[
			KeyboardButton("Умумий видеолар"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)
