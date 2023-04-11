from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

qadamjolarumum = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🏡 Бош меню")
		],
		[
			KeyboardButton("🔈 Aудио"),
			KeyboardButton("🎞 Bидео"),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

qadamjolarvid = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("⏮ Олдинги"),
			KeyboardButton("🏡 Бош меню"),
		],
		[
			KeyboardButton('Умра сафарига борувчилар учун маслаҳатлар'),
		],
		[
			KeyboardButton('Уҳуд тоғи'),
			KeyboardButton('Эҳромга кириш ва умрага ният қилиш'),
		],
		[
			KeyboardButton('Савр тоғи'),
			KeyboardButton('Икки қиблали масжид'),
			KeyboardButton('Қизил тоғ'),
		],
		[
			KeyboardButton('Масжидул-ҳаромга киришдан олдин нималарни билиш керак?'),
			KeyboardButton('Масжидул-ҳаромдаги жоиз ва ножоиз амаллар'),
		],
		[
			KeyboardButton('Эҳромдан чиқишнинг шарти'),
			KeyboardButton('Сафо ва Марва'),
			KeyboardButton('Абдуллоҳ ибн Аббос розияллоҳу анҳунинг масжидлари'),
		],
		[
			KeyboardButton('Азақ қудуғи'),
			KeyboardButton('Жума масжиди'),
			KeyboardButton('Каъб ибн Ашраф қасри'),
		],
		[
			KeyboardButton('Ижоба масжиди'),
			KeyboardButton('Сажда масжиди'),
			KeyboardButton('Бану Соъида сақифаси'),
		],
		[
			KeyboardButton('Раҳмат тоғи'),
			KeyboardButton('Зубайдахоним қудуғи'),
			KeyboardButton('Мино водийси'),
		],
		[
			KeyboardButton('Қодамун набий'),
			KeyboardButton('Ғорс қудуғи'),
		],
		[
			KeyboardButton('Салмон Форсий қудуғи'),
			KeyboardButton('Ҳазрати Усмон қудуғи'),
		],
		[
			KeyboardButton('Расулуллоҳ ﷺ таваллуд топган уй')
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)

qadamjolaraud = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("⏮ Олдинги"),
			KeyboardButton("🏡 Бош меню"),
		],
		[
			KeyboardButton('1-4'),
			KeyboardButton('5-8'),
		],
		[
			KeyboardButton('9-12'),
			KeyboardButton('13-16'),
			KeyboardButton('17-20'),
		],
		[
			KeyboardButton('21-25'),
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True
)
