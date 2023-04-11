from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from keyboards.default.qurantalimi_dk import quran_m

from loader import dp

# QUR'ON TA'LIMI HANDLER BOSHI

quran_dict = {1:{'v':'BAACAgIAAxkBAAEEveJipRIAARCKYYFHgnucEppwl5oVkLYAAs0ZAAJw0uBLuWE-bEWRZ9okBA','a':'CQACAgIAAxkBAAEGSHpitVeUZQrSKDqpaiPE2hVyKUieQgACbxgAAs9QqUl3VYytehJITCkE','c':'Қуръони Каримни 6 ёки 3 йилда ёдлаш услублари\n\n<a href=\'https://youtu.be/hzcGYGylvZU\'>Youtube орқали кўриш</a>','da':'BQACAgIAAxkBAAEHWTZizhijJllUDw6mo6Rum67Nx96oowACsRsAAjDk4EvE25CFNrRrlykE','db':'BQACAgIAAxkBAAEHWThizhiyrRvkLLugbRRCo7JBHZ0ZhwACshsAAjDk4Euy6hqFDbWB9ikE'}}
quran_talim_dict = {2:{'v':'BAACAgIAAxkBAAEG0NJiwL0IkgZuVl3QNhwZWYkdKr-kRAAC_BsAAtzq6UjX-EQ3HgZV8ykE','a':'CQACAgIAAxkBAAEG0NRiwL5I5Ex86z7O9hn62VqPHdSEnAACwR4AAhEoCUq2fOONTTQF8CkE','c':'Қуръон ёдлашдаги самарали услублар \n\n«Ҳилол-Нашр» нашриётида бўлиб ўтган хатмонадан\n\n21.05.2022'},3:{'v':'BAACAgIAAxkBAAEDyXlinZwg-kUlf7Su4zdoWwz1H2u49wACQBkAAh-E6EhubsmNFxO6ZiQE', 'a':'CQACAgIAAxkBAAEEv0lipU44QZyESmsq_TT6_SI8xqrg7QACDRwAAtXkKUloDO8yt3gllyQE', 'c':'Талабаларга Қуръони Каримни ёдлаш бўйича кўрсатмалар\n\n<a href=\'https://www.youtube.com/watch?v=9MjieFp4lGw\'>Youtube орқали кўриш</a>'},4:{'v':'BAACAgIAAxkBAAEDzNtincYC9fiM3KCNPvLinbJYUanUeAACIQkAAjzi2UgYURrii4lfuiQE','c':'Қуръонга ошно қалбар учун "Мен ҳам қори бўламан" кўрсатуви\n\nЮртимизнинг таниқли Қуръон ходимлари билан суҳбатлар, синовдан ўтган услублар, Қуръон ёдлашнинг энг осон ва самарали усулларини тақдим этувчи лойиҳа <a href=\'https://t.me/muallim_media\'>Muallim media</a> каналида! \n\nИлк меҳмонимиз Қуръони карим ходими ҲАСАНХОН ЯҲЁ АБДУЛМАЖИД \n\n1-қисм\n\n<a href=\'https://youtu.be/QpFM8pRZc2E\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/MuaIIimMedia/\'>Facebook</a> | <a href=\'https://www.instagram.com/muallimmedia/\'>Instagram</a> | <a href=\'https://t.me/muallim_media\'>Telegram</a> | <a href=\'https://www.youtube.com/c/muallimmedia\'>Youtube</a>'},5:{'v':'BAACAgIAAxkBAAEDzM9incUPwX0weqQl86m3O_KcEfMhLAAClQoAAncFIEleyGV3X1uPtiQE','c':'Қуръонга ошно қалбар учун "Мен ҳам қори бўламан" кўрсатуви\n\nЮртимизнинг таниқли Қуръон ходимлари билан суҳбатлар, синовдан ўтган услублар, Қуръон ёдлашнинг энг осон ва самарали усулларини тақдим этувчи лойиҳа <a href=\'https://t.me/muallim_media\'>Muallim media</a> каналида! \n\nИлк меҳмонимиз Қуръони карим ходими ҲАСАНХОН ЯҲЁ АБДУЛМАЖИД \n\n2-қисм\n\n<a href=\'https://youtu.be/LTF5qryDUj4\'>Youtube орқали кўриш</a>\n\n<a href=\'https://www.facebook.com/MuaIIimMedia/\'>Facebook</a> | <a href=\'https://www.instagram.com/muallimmedia/\'>Instagram</a> | <a href=\'https://t.me/muallim_media\'>Telegram</a> | <a href=\'https://www.youtube.com/c/muallimmedia\'>Youtube</a>'},6:{'v':'BAACAgIAAxkBAAEDzP9incevaxBbE4Tx16Zi1GJYpu6JnQACRAgAAiLCiUtoWQXsUSeNPyQE','c':'Қуръони каримни ёдлаш бўйича усул ва муҳим тавсиялар.'}}
quranuzcap = "\n\n<a href='https://www.facebook.com/hazratim.uz'>Facebook</a> | <a href='https://www.instagram.com/hazratim_uz/'>Instagram</a> | <a href='https://t.me/joinchat/AAAAAFki3TLL4WCIyXw22g'>Telegram</a> | <a href='https://www.youtube.com/watch?v=eCMD_cufc3A&list=PLt7pLJiSp2TAZrqP789st_tz8xK72IhjP'>Youtube</a>"

@dp.message_handler(text="📖 Қуръон таълими (тавсиялар)")
async def qurantalim(msg: types.Message, state:FSMContext):
	await msg.answer("📖 Қуръон таълими", reply_markup=quran_m)
	await state.set_state("q")

@dp.message_handler(text="🎬 Видео", state="q")
async def quran(msg: types.Message, state:FSMContext):
	await msg.answer_video(video=quran_dict[1]['v'],caption=quran_dict[1]['c'])
	await msg.answer_document(document=quran_dict[1]['da'],caption=quran_dict[1]['c'])
	await msg.answer_document(document=quran_dict[1]['db'],caption=quran_dict[1]['c'])
	for qulf, kalit in quran_talim_dict.items():
		await msg.answer_video(video=kalit['v'],caption=kalit['c'] + quranuzcap)
	await state.set_state("q")

@dp.message_handler(text="🎧 Ayдиo", state="q")
async def quran(msg: types.Message, state:FSMContext):
	for qulf, kalit in quran_dict.items():
		await msg.answer_audio(audio=kalit['a'], caption=kalit['c'])
	for qulf, kalit in quran_talim_dict.items():
		try:
			if kalit['a']:
				await msg.answer_audio(audio=kalit['a'], caption=kalit['c'])
		except:
			pass
	await state.set_state("q")

# QUR'ON TA'LIMI HANDLER OXIRI

