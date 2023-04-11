from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

m_list = ['1-5 cонлар','6-10 cонлар','11-15 cонлар','16-20 cонлар',
		  '21-25 cонлар','26-29 cонлар']

sh_list = ['1-5 атрлар','6-10 атрлар','11-15 атрлар','16-18 атрлар','Дуо']

m1_5 = list(range(577,582))
m6_10 = list(range(582,587))
m11_15 = list(range(587,592))
m16_20 = list(range(592,597))
m21_25 = list(range(597,604))
m26_29 = list(range(604,609))

m01_5 = list(range(1119,1124))
m06_10 = list(range(1124,1129))
m011_15 = list(range(1129,1134))
m016_20 = list(range(1134,1139))
m021_25 = list(range(1139,1146))
m026_29 = list(range(1146,1151))

sh1_5 = list(range(980,985))
sh6_10 = list(range(985,990))
sh11_15 = list(range(990,995))
sh16_18 = list(range(995,998))
duo = list(range(998,999))

m1_dict = {}
m2_dict = {}
sh_dict = {}

m1 = [m1_5,m6_10,m11_15,m16_20,m21_25,m26_29]
m2 = [m01_5,m06_10,m011_15,m016_20,m021_25,m026_29]
sh = [sh1_5,sh6_10,sh11_15,sh16_18,duo]

for i in range(0, len(m_list)):
	m1_dict[m_list[i]] = m1[i]

for i in range(0, len(m_list)):
	m2_dict[m_list[i]] = m2[i]

for i in range(0, len(sh_list)):
	sh_dict[sh_list[i]] = sh[i]

async def mbm_dk():
	mbm_k = ReplyKeyboardMarkup(row_width=2,
							   resize_keyboard=True,
							   one_time_keyboard=True)
	mbm_k.add("🏡 Бош меню")
	mbm_k.add("🎧 Ayдио")
	mbm_k.insert("🎬 Bидeо")
	mbm_k.add("Мавлиди Шариф")

	return mbm_k

async def m1_dk():
	m1_k = ReplyKeyboardMarkup(row_width=2,
							   resize_keyboard=True,
							   one_time_keyboard=True)
	m1_k.add("⏮ Олдинги")
	m1_k.insert("🏡 Бош меню")
	m1_k.add("1-5 cонлар")
	for n in m_list:
		if n == '1-5 cонлар':
			pass
		else:
			m1_k.insert(n)

	return m1_k

async def sharif_dk():
	sh_dk = ReplyKeyboardMarkup(row_width=2,
								resize_keyboard=True,
								one_time_keyboard=True)
	sh_dk.add("⏮ Олдинги")
	sh_dk.insert("🏡 Бош меню")
	sh_dk.add('1-5 атрлар')
	for n in sh_list:
		if n == '1-5 атрлар':
			pass
		else:
			sh_dk.insert(n)

	return sh_dk