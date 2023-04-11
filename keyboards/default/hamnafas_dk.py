from aiogram.types import ReplyKeyboardMarkup

hamnafas_dklist = ["1-сон","2-сон","3-сон","4-сон","5-сон","6-сон","7-сон","8-сон","9-сон","10-сон"]
async def hamnafas_dk():
	hamnafas_dk = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)

	hamnafas_dk.add("🏡 Бош меню")
	hamnafas_dk.add("1-сон")
	for n in hamnafas_dklist:
		if n == "1-сон":
			pass
		else:
			hamnafas_dk.insert(n)

	return hamnafas_dk