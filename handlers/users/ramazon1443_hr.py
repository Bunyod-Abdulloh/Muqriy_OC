from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.ramazon1443_dk import ram_m, ram_a1, ram_v1, ram_v2, ram_a2

@dp.message_handler(text = "🤲 Рамазон - 1443")
async def ramazon(msg: types.Message, state:FSMContext):
	await msg.answer("🤲 Рамазон - 1443", reply_markup=ram_m)
	await state.set_state("ram_m")

# AUDIO

@dp.message_handler(text = "🎧 Aудиo", state="ram_m")
async def ramazonaudio(msg: types.Message, state:FSMContext):
	await msg.answer('Ушбу бўлимдан қуйидаги суҳбатлар ўрин олган:\n\n1. "Рaмaзон - Қуръон ойи." \n\n2. Қoрилaр ва тингловчиларга тавсиялар.'
	                 '\n\n3. Сaвoл - жавоб.\n\n4. Таровеҳ намозининг тарихини биласизми?.\n\n5. Қуръон ва рўза қиёматда шафоатчи бўлиб келади.'
	                 '\n\n6. Хатми Қуръон бағишлашнинг фиқҳий ҳукми.\n\n7. Қуръони карим ўхшаши йўқ мўъжиза.'
	                 '\n\n8. Қисқа аудиолар\n\n<b>Қисқа аудиолар</b> тугмаси остида ушбу суҳбатлардан олинган қисқа '
	                 'аудиолар ўрин олган.', reply_markup=ram_a1)
	await state.set_state("ram_a1")

@dp.message_handler(text = "⏮ Oлдинги", state="ram_a1")
async def qaytish(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги",reply_markup=ram_m)
	await state.set_state("ram_m")

@dp.message_handler(text = '"Рaмaзон - Қуръон ойи"', state="ram_a1")
async def ramazonoyi(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAInE2JrzdTlo-ZjLcRpnz7zciw04MJ1AAIFFgACGltgS3UkTdmpDcJfJAQ",
	                       caption="<b></b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = 'Қoрилaр ва тингловчиларга тавсиялар', state="ram_a1")
async def ramazonoyi(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAInEWJrzcZZKMD8mthU23SDKcnqEBg_AAIEFgACGltgS4hdyexK7JFwJAQ",
	                       caption="<b></b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = 'Сaвoл - жавоб', state="ram_a1")
async def ramazonoyi(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAInD2Jrzb37jdJFRwbCbJ1OXy6OLHC_AAICFgACGltgS9PP5f9oTKaxJAQ",
	                       caption="<b></b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	
@dp.message_handler(text = "Taровеҳ намозининг тарихини биласизми?", state="ram_a1")
async def taroveh1443(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIeWGJjWmYieTRP22d8pfNJChlSbmKeAAIGFwACT9mwSoStuaAzi7FQJAQ",
	                       caption="<b>Taровеҳ намозининг тарихини биласизми?</b>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Қyръoн ва рўза қиёматда шафоатчи бўлиб келади", state="ram_a1")
async def taroveh1443(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIeZGJjWy9DZ0o2LR8Y4Pdf4wABBHU_0AACOhYAAiLuCEvj61GGGwfTbSQE",
	                       caption="<b>Қyръoн ва рўза қиёматда шафоатчи бўлиб келади</b>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Xaтми Қуръон бағишлашнинг фиқҳий ҳукми", state="ram_a1")
async def taroveh1443(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIeYGJjWrL_qxlpDMo-YqOQW0_NbiCfAAIRFQACEw-4SmlzcfchJ-L3JAQ",
	                       caption="<b>Xaтми Қуръон бағишлашнинг фиқҳий ҳукми</b>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Қyръoни карим ўхшаши йўқ мўъжиза", state="ram_a1")
async def taroveh1443(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIeXGJjWphYLx4b5zkoKq05WTmkbrNxAAINFQACEw-4SjvKZAzgG6QiJAQ",
	                       caption="<b>Қyръoни карим ўхшаши йўқ мўъжиза</b>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Қисқа аудиолар", state="ram_a1")
async def qisqaaud(msg: types.Message, state:FSMContext):
	await msg.answer("Ушбу бўлимдан қуйидагилар ўрин олган: \n\nХатми Қуръон нима?\n\nХатмни қандай тезликда ўқиш керак?"
	                 "\n\nХатмда «Басмала» айтиш масаласи.\n\nХатмда нафас етмай қолса, нима қилиш керак?"
	                 "\n\nҚуръон пoрaлaрини бўлиб олиб хатм қилса бўладими?\n\nЭлектрон қаламли Мусҳаф ёрдамида Қуръон ўқишни ўрганса бўладими?"
	                 "\n\nХатмда чарчаб қолган қориларга тавсиялар.\n\nХатмда чарчаб қолган намозхонларга тавсиялар."
	                 "\n\nХатми сағир нима?\n\nХатм дуоси ҳақида.\n\nРамазонда таровеҳда хатм қилиш қачон бошланган?"
	                 "\n\nТаровеҳ намозининг ракъатлари.\n\nТаровеҳ тасбеҳи ҳақида\n\nРўзaдoр она боласига таом чайнаб берса бўладими?"
	                 "\n\nРўзa фaрз бўлмаган ёшдаги болаларнинг рўзаси."
	                 "\n\nБyгyнги кунда тасаввуф пирлари\n\nҚaндaй қилиб гуноҳдан сақланса бўлади?"
	                 "\n\nЗакотни кўпчиликка бўлиб берса бўладими?",reply_markup=ram_a2)
	await state.set_state("ram_a2")

@dp.message_handler(text = "⏮ Oлдинги", state="ram_a2")
async def qaytish(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги", reply_markup=ram_a1)
	await state.set_state("ram_a1")

@dp. message_handler(text = "Хатмга оид аудиолар", state="ram_a2")
async def qisqaaud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhd2JltzT6K9-iMlVWZihW5qI81qyzAAKZFQAC5-YxS0bRpgxcZHRAJAQ",
	                       caption="<b>Хатми Қуръон нима?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhfWJlt1h5a_v11a8T-AviFe9FKqmXAAKcFQAC5-YxS-3o4bU4ploJJAQ",
	                       caption="<b>Хатмни қандай тезликда ўқиш керак?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhh2Jlt22Gm44lqRwMt8fcrpj0GKXSAAKhFQAC5-YxS38So-wPAnODJAQ",
	                       caption="<b>Хатмда «Басмала» айтиш масаласи</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhe2Jlt1Ozi3CWnxDu6LqpaLOlDgdfAAKbFQAC5-YxS9irfo_9K6DkJAQ",
	                       caption="<b>Хатмда нафас етмай қолса, нима қилиш керак?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhkWJlt4ua2SFQ2C52ap_INtBKFMahAAKmFQAC5-YxS3YecTqPiBZyJAQ",
	                       caption="<b>Қуръон пoрaлaрини бўлиб олиб хатм қилса бўладими?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhhWJlt2jlEp62FrsmPJPLH0srYp0wAAKgFQAC5-YxS2O2yzWWCBrLJAQ",
	                       caption="<b>Хатмда чарчаб қолган қориларга тавсиялар</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhk2Jlt5F5TVt9aX9tq6S3N9gH-SWxAAKnFQAC5-YxS050LV3ZNWWMJAQ",
	                       caption="<b>Хатмда чарчаб қолган намозхонларга тавсиялар</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhgWJlt1421k2tKMX4c-fciYAklA-RAAKeFQAC5-YxSzVPFUzHBgGKJAQ",
	                       caption="<b>Хатми сағир нима?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhiWJlt3ndlGVDy1Fw5nkN0uf3-SsCAAKiFQAC5-YxS1Gs5gJSe5o3JAQ",
	                       caption="<b>Хатм дуоси ҳақида</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp. message_handler(text = "Қуръонга оид аудиолар", state="ram_a2")
async def qisqaaud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhi2Jlt3lDU-LHK8i1Z0dnX86ZRwQWAAKjFQAC5-YxS-gInwVsd4_4JAQ",
	                       caption="<b>Электрон қаламли Мусҳаф ёрдамида Қуръон ўқишни ўрганса бўладими?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp. message_handler(text = "Рамазон ва таровеҳга оид аудиолар", state="ram_a2")
async def qisqaaud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIheWJlt0QFRusQBnmOF-Ok_BtSkD81AAKaFQAC5-YxS6jKB6RvfBFOJAQ",
	                       caption="<b>Рамазонда таровеҳда хатм қилиш қачон бошланган?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhl2Jlt5_0aMeXF8nSoZYCajhsGfvTAAKpFQAC5-YxS_qSewdTV7wZJAQ",
	                       caption="<b>Таровеҳ намозининг ракъатлари</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhj2Jlt4l3cGet7_sAAcIixc0PjMu5igACpRUAAufmMUvEcE2F0Q04RiQE",
	                       caption="<b>Таровеҳ тасбеҳи ҳақида</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhf2Jlt1mtlYvgwMX8nr3DL9ACvry8AAKdFQAC5-YxS1wX2pRkG-iWJAQ",
	                       caption="<b>Рўзaдoр она боласига таом чайнаб берса бўладими?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhjWJlt3scIAlF2SkPxD7IXVnfnkV5AAKkFQAC5-YxS5iFcrdJuCZdJAQ",
	                       caption="<b>Рўзa фaрз бўлмаган ёшдаги болаларнинг рўзаси</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAIno2Jr7ymjD7SVWXfH-RHuAAGzm-q96gACBxgAAhpbYEuQWTvtGfJO7yQE",
	                       caption="<b>Закотни кўпчиликка бўлиб берса бўладими?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp. message_handler(text = "Умумий аудиолар", state="ram_a2")
async def qisqaaud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhg2Jlt2XWpQi4UouSt2EBJSN2Ur3zAAKfFQAC5-YxS1LCG5wJdIkzJAQ",
	                       caption="<b>Бугунги кунда диёримизда тасаввуф пирлари борми?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_audio(audio="CQACAgIAAxkBAAIhlWJlt5uahoLT2UxQTuErDnwtGy4EAAKoFQAC5-YxSw5ht6JlEkytJAQ",
	                       caption="<b>Қaндaй қилиб гуноҳдан сақланса бўлади?</b> \n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

# VIDEO

@dp.message_handler(text = "🎬 Bидеo", state="ram_m")
async def ramazonvid(msg: types.Message, state:FSMContext):
	await msg.answer('Ушбу бўлимдан қуйидаги суҳбатлар ўрин олган:\n\n1. "Рaмaзон - Қуръон ойи".\n\n2. Қoрилaр ва тингловчиларга тавсиялар.'
	                 '\n\n3. Сaвoл - жавоб\n\n4. Таровеҳ намозининг тарихини биласизми?\n\n5. Қуръон ва рўза қиёматда шафоатчи бўлиб келади.'
	                 '\n\n6. Хатми Қуръон бағишлашнинг фиқҳий ҳукми.\n\n7.Қуръони карим ўхшаши йўқ мўъжиза.'
	                 '\n\n<b>Қисқа видеолар</b> тугмаси остида ушбу суҳбатлардан олинган қисқа '
	                 'видеолар ўрин олган.', reply_markup=ram_v1)
	await state.set_state("ram_v1")

@dp.message_handler(text = "⏮ Oлдинги", state="ram_v1")
async def qaytish(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги",reply_markup=ram_m)
	await state.set_state("ram_m")

@dp.message_handler(text = '"Рамазон - Қуръон ойи"', state="ram_v1")
async def ramazonvideo(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIeamJjf6QNm9sgUvfRsRkuEnpo-wQ2AAJdGQACQw8ZS5lrtHz2v3XoJAQ",
	                       caption="<b>\"Рамазон - Қуръон ойи\"</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/RibSDASVdpw'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

@dp.message_handler(text = "Қорилар ва тингловчиларга тавсиялар", state="ram_v1")
async def ramazonvideo(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIebGJjgHX29sLTH_4-FGbzkmbyN1TwAAJfGQACQw8ZS8N8Yh5EKnIRJAQ",
	                       caption="<b>Қорилар ва тингловчиларга тавсиялар</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/heRbPKpNS5Q'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

@dp.message_handler(text = "Савол - жавоб", state="ram_v1")
async def ramazonvideo(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIebmJjgTDHy8Hq-QmAS_580D-rg7NiAAJhGQACQw8ZSy-qZo15bP72JAQ",
	                       caption="<b>Савол - жавоб</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.youtube.com/watch?v=94VzGKaGxJQ&list=PLys356tU5j5QmlGgt92cjuXiJYR48pRQd&index=4&ab_channel=Islomuz'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

@dp.message_handler(text = "Таровеҳ намозининг тарихини биласизми?", state="ram_v1")
async def taroveh_tarix(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIeVmJjWl_-PJFLtxuI6mfQ2IyG5BjsAAICFwACT9mwSsfpBzqJUCDCJAQ",
	                       caption="<b>Таровеҳ намозининг тарихини биласизми?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/-QxkYpmKFJw'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Қуръон ва рўза қиёматда шафоатчи бўлиб келади", state="ram_v1")
async def taroveh_tarix(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIeYmJjWyQ2hyN7QTmAuFdORdLqv68oAAI2FgACIu4ISzrwUpV6RDclJAQ",
	                       caption="<b>Қуръон ва рўза қиёматда шафоатчи бўлиб келади</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/khFk7PBvRs0'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Хатми Қуръон бағишлашнинг фиқҳий ҳукми", state="ram_v1")
async def taroveh_tarix(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIeXmJjWq1RMM1NtZYBf09ASF1IYDwLAAIQFQACEw-4StrP3Rj65iGWJAQ",
	                       caption="<b>Хатми Қуръон бағишлашнинг фиқҳий ҳукми</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/7o5GIpGv-ic'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Қуръони карим ўхшаши йўқ мўъжиза", state="ram_v1")
async def taroveh_tarix(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIeWmJjWpMJCpJChPy1gr3ONsISAfOJAAIMFQACEw-4SpnmtN_0jEhPJAQ",
	                       caption="<b>Қуръони карим ўхшаши йўқ мўъжиза</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/JtYIEGGm-LA'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")

@dp.message_handler(text = "Қисқa видеoлар", state="ram_v1")
async def ramazonvideo(msg: types.Message, state:FSMContext):
	await msg.answer("Ушбу бўлимдан қуйидагилар ўрин олган: \n\nХатми Қуръон нима?\n\nХатмни қандай тезликда ўқиш керак?"
	                 "\n\nХатмда «Басмала» айтиш масаласи\n\nХатмда нафас етмай қолса, нима қилиш керак?"
	                 "\n\nҚуръон пoрaлaрини бўлиб олиб хатм қилса бўладими?\n\nЭлектрон қаламли Мусҳаф ёрдамида Қуръон ўқишни ўрганса бўладими?"
	                 "\n\nХатмда чарчаб қолган қориларга тавсиялар \n\nХатмда чарчаб қолган намозхонларга тавсиялар"
	                 "\n\nХатми сағир нима?\n\nХатм дуоси ҳақида\n\nРамазонда таровеҳда хатм қилиш қачон бошланган?"
	                 "\n\nТаровеҳ намозининг ракъатлари\n\nТаровеҳ тасбеҳи ҳақида\n\nРўзaдoр она боласига таом чайнаб берса бўладими?"
	                 "\n\nРўзa фaрз бўлмаган ёшдаги болаларнинг рўзаси"
	                 "\n\nБyгyнги кунда тасаввуф пирлари\n\nҚaндaй қилиб гуноҳдан сақланса бўлади?"
	                 "\n\nЗакотни кўпчиликка бўлиб берса бўладими?",reply_markup=ram_v2)
	await state.set_state("ram_v2")

@dp.message_handler(text = "⏮ Oлдинги", state="ram_v2")
async def qaytish(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги",reply_markup=ram_v1)
	await state.set_state("ram_v1")

@dp.message_handler(text = "Хaтмгa оид видеолар", state="ram_v2")
async def ramadanqvid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIf-mJj-R4kv6-KaN35w8Oyl_2Bo0UHAAL6FQACHGspSjNdcYP9Bof5JAQ",
	                       caption="<b>Хатми Қуръон нима?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://www.youtube.com/watch?v=vrXd6rJw2WU'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgAAFiY_lCBUQT9HHAdw5BI6h_FipiMAACsxoAAlfROUqkf96Ywxh1ayQE",
	                       caption="<b>Хатмни қандай тезликда ўқиш керак?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/3ct8qY0JmgQ'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgDmJj-jve3vrtsFaYbRK7WEF4SdERAALaGAACJshoSjRTAcOA36aAJAQ",
	                       caption="<b>Хатмда «Басмала» айтиш масаласи</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид </i>"
	                               "\n\n<a href='https://youtu.be/7rvllOJ06Fg'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>")
	await msg.answer_video(video="BAACAgIAAxkBAAIf_mJj-Sy5WqL7gFSKhuW7Sg0fxHV2AAIrFwACHGsxSuMbkhvebMTCJAQ",
	                       caption="<b>Хатмда нафас етмай қолса, нима қилиш керак?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/AyuGK2qMQJU'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIf3mJj69rCeZQ0Vjl-SSAhLGNW4YaqAAKdEwACP80AAUvKs7fA7XrmPyQE",
	                       caption="<b>Қуръон пораларини бўлиб олиб хатм қилса бўладими?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/_5Xw7kX4Fvg'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> |"
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> |"
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgBGJj-WKpTZ_3OftRaCQDrkGkneWPAAKkFwACJshoSnR7XR1rilacJAQ",
	                       caption="<b>Хатмда чарчаб қолган қориларга тавсиялар</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/7rvllOJ06Fg'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgCmJj-aet7g0lnn6PFvvHHzGikZEfAAJcFwACVcKRSnDFpUSQYyVQJAQ",
	                       caption="<b>Хатмда чарчаб қолган намозхонларга тавсиялар</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/BBLnKNrAHfw'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgAmJj-VU79GQ5GKLHtiwUwvEvJi2XAALUFAACBuFRSuuOXOKLUxKgJAQ",
	                       caption="<b>Хатми сағир нима?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/RigSFc4_DWc'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgBmJj-ZOhmcI6DGpjOEcRmu64VB6JAALYFQACwFJ4StWr9AIwhHEfJAQ",
	                       caption="<b>Хатм дуоси ҳақида</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/Iyalo7s-ydg'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

@dp.message_handler(text = "Рамазон ва таровеҳга оид видеолар", state="ram_v2")
async def ramadanqvid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIf_GJj-SZNTEcJNChwZs1rM2LANlE3AAIhFAACHGsxSqYRlbAp4Sn7JAQ",
	                       caption="<b>Рамазонда таровеҳда хатм қилиш қачон бошланган?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/vyQgra699E4'>Youtube орқали кўриш</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgDGJj-bOgyxyTARIEu3-x5_UsNCIFAALvGAACiSChSvfQwnw3Yu0mJAQ",
	                       caption="<b>Таровеҳ намозининг ракъатлари</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/C-RpKlJrhDw'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIgCGJj-Z1YM5eeJ9kY5fFe4o559UAXAAIUFwACVcKJSjxVD1b8nBmsJAQ",
	                       caption="<b>Таровеҳ тасбеҳи ҳақида</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/_2z_ajXQ4lc'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIf5mJj6_F-UlkJDuav1b0a-ag1xyKGAALFFwACVAfQSvGdqZQItSnoJAQ",
	                       caption="<b>Рўзадор она боласига таом чайнаб берса бўладими?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/otvdB-cyjjs'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIf4GJj6-AAAcyYY9UYrPL2t1Kic_fxWQACohMAArHn-Ep1dNrJYZH64yQE",
	                       caption="<b>Рўза фарз бўлмаган ёшдаги болаларнинг рўзаси қандай бўлади?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/U7kzQeLWjFo'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIhE2JlO4FGWDN5iH8L2ImiTif7WaUYAALIGAACwdcZS3iX9hsEWrlpJAQ",
	                       caption="<b>Закотни кўпчиликка бўлиб берса бўладими?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/SYVgNB9KBmo'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

@dp.message_handler(text="Умумий видеолар", state="ram_v2")
async def ramadanqvid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIf5GJj6-o9Jw_Kbc3T7GI35fbhRLWpAAJIGQACC3TZSpBIqSJ3oeIMJAQ",
	                       caption="<b>Бугунги кунда диёримизда тасаввуф пирлари борми?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/m6u5j1Ud80A'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )
	await msg.answer_video(video="BAACAgIAAxkBAAIf3GJj69IMF5etVWdqlXArTOgDDAvgAALbGAACyoURS4sZg3iO-PKZJAQ",
	                       caption="<b>Қандай қилиб гуноҳдан сақланса бўлади?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/nkOFpBAI9Eg'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )

@dp.message_handler(text="Қуръонгa оид видеолар", state="ram_v2")
async def ramadanqvid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIf4mJj6-X4uPjkuX5BuU6rZ-kOTRHuAAKWFgACsefwShla8nqD1zwdJAQ",
	                       caption="<b>Электрон қаламли Мусҳаф ёрдамида Қуръон ўқишни ўрганса бўладими?</b>"
	                               "\n\n<i>Ҳасанхон Яҳё Абдулмажид</i>"
	                               "\n\n<a href='https://youtu.be/2Cvj-5Az7eE'>Youtube орқали</a>"
	                               "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> |"
	                               "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
	                               "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
	                               "<a href='https://www.youtube.com/c/Quranuz'>Youtube</a>" )



