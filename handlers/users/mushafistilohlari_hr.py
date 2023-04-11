from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from  aiogram.dispatcher import FSMContext

from loader import dp

from keyboards.default.mushafistilohlari_dk import istiloh_sharh_keys, istiloh_keys

quranuz = "\n\n<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a> | <a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | <a href='https://t.me/joinchat/AAAAAEKXLiebTLCuRzZiHA'>Telegram</a> | <a href='https://www.youtube.com/quranuz?sub_confirmation=1'>Youtube</a>"

qisqa_dict = {1:{'v':'BAACAgIAAxkBAAIFnGI_5h_r7CBfd7u4uqsOL5CmmYdbAAJwBwACJMBYSMfegYhmIFN5IwQ','c':'<b>01. ЮРТИМИЗДА ЧОП ҚИЛИНГАН МУСҲАФЛАР ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/8398DzveitI\'>Youtube орқали кўриш</a>'},
              2:{'v':'BAACAgIAAxkBAAIFnmI_5iljKJ3BQi7jsFE2Wxy8x-6MAAKrBwACJMBYSP7a-nhmOSh4IwQ','c':'<b>02. ИМОМ ҲАФС ВА У КИШИНИНГ РИВОЯТЛАРИ ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/knCVYf_OS6o\'>Youtube орқали кўриш</a>'},
              3:{'v':'BAACAgIAAxkBAAIFoGI_5i3VLytIsIKxICqnHSB242M5AAK7BwACJMBYSNdQby6ILF3JIwQ','c':'<b>03. ИМОМ ОСИМ ВА У КИШИНИНГ УСТОЗЛАРИ ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/xZ3iR1csiaQ\'>Youtube орқали кўриш</a>'},
              4:{'v':'BAACAgIAAxkBAAIFomI_5jKsFS0z3Bx5EUwyPDwnDALaAAK8BwACJMBYSPLsBeyUpQTBIwQ','c':'<b>4. ҚИРОАТ, РИВОЯТ ВА ТАРИҚА ТУШУНЧАСИ</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/mQM0LTNmHYc\'>Youtube орқали кўриш</a>'},
              5:{'v':'BAACAgIAAxkBAAIFpGI_5jZzrNTxCcktWpTVjlG9L29zAAK9BwACJMBYSDqV1NluoIGQIwQ','c':'<b>5. БУГУНГИ КУНДА ҚАЙСИ ҚИРОАТЛАРДА МУСҲАФЛАР МАВЖУД?</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/OqlbcPouAlA\'>Youtube орқали кўриш</a>'},
              6:{'v':'BAACAgIAAxkBAAIFpmI_5jx06GC4w13dYjymiR1YSguaAAK_BwACJMBYSPsPvX3ba17WIwQ','c':'<b>6. МУСҲАФ РАСМИ ХАТИ ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/b81gebXRTfI\'>Youtube орқали кўриш</a>'},
              7:{'v':'BAACAgIAAxkBAAIFqGI_5kEQoI2DR1S1Nv9lqzUcYFqKAALCBwACJMBYSNpCf8-xC96_IwQ','c':'<b>7. МУСҲАФ ЗАВОБИТЛАРИ ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/Uvzk945lOc0\'>Youtube орқали кўриш</a>'},
              8:{'v':'BAACAgIAAxkBAAIFqmI_5kUJNYmgur-4eBUDZ0QZrANUAALFBwACJMBYSCy3EwlgsnFyIwQ','c':'<b>8. ҚУРЪОНИ КАРИМ ОЯТЛАРИНИНГ АДАДИ ВА ҚУРЪОНИ КАРИМНИНГ ТАҚСИМИ ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/i7Resdrgkl4\'>Youtube орқали кўриш</a>'},
              9:{'v':'BAACAgIAAxkBAAIFrGI_5kp8Sgd757OmoCszsLqIIMl_AALJBwACJMBYSGoS2MBP90K0IwQ','c':'<b>9. ВАҚФ‑ИБТИДО МАСАЛАСИ, САЖДА ОЯТЛАРИ ВА САКТА ЎРИНЛАРИ ҲАҚИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/LHECIsXx2_c\'>Youtube орқали кўриш</a>'},
              10:{'v':'BAACAgIAAxkBAAIFrmI_5k4AAbVRq3FzWp3hNYw3jtmZLgACywcAAiTAWEjFFnYSGeixWiME','c':'<b>10. ФОТИҲАДА БАСМАЛА МАСАЛАСИ</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/QRNxJbSO6a0\'>Youtube орқали кўриш</a>'},
              11:{'v':'BAACAgIAAxkBAAIFsGI_5lPaoiGy1Dc5RjQdO4KZqeXXAALOBwACJMBYSCdVm5cTyTGFIwQ','c':'<b>11. УСМОН ТОҲО ҲАҚЛАРИДА</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/lMxbKSgsDyU\'>Youtube орқали кўриш</a>'},
              12:{'v':'BAACAgIAAxkBAAIFsmI_5lj6KMnd3TbelBh6NBscU0RrAALPBwACJMBYSDG6ivaiZVzRIwQ','c':'<b>12. МУСҲАФ РАСМИ ХАТИ ТАВФИҚИЙМИ?</b>\n\n«Мусҳаф истилоҳлари шарҳи» туркум суҳбатларидан\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>\n\n<a href=\'https://youtu.be/AhnbC_w5U70\'>Youtube орқали кўриш</a>'}
              }

@dp.message_handler(text = "📑 Мусҳаф истилоҳлари шарҳи")
async def sharh_handler(msg: types.Message, state:FSMContext):
	await msg.answer("Ушбу суҳбатлар туркуми қуйидаги мавзуларни ўз ичига олади: "
	                 "\n\n1. ЮРТИМИЗДА ЧОП ҚИЛИНГАН МУСҲАФЛАР ҲАҚИДА"
	                 "\n\n2. ИМОМ ҲАФС ВА У КИШИНИНГ РИВОЯТЛАРИ ҲАҚИДА"
	                 "\n\n3. ИМОМ ОСИМ ВА У КИШИНИНГ УСТОЗЛАРИ ҲАҚИДА"
	                 "\n\n4. ҚИРОАТ, РИВОЯТ ВА ТАРИҚА ТУШУНЧАСИ"
	                 "\n\n5. БУГУНГИ КУНДА ҚАЙСИ ҚИРОАТЛАРДА МУСҲАФЛАР МАВЖУД?"
	                 "\n\n6. МУСҲАФ РАСМИ ХАТИ ҲАҚИДА"
	                 "\n\n7. МУСҲАФ ЗАВОБИТЛАРИ ҲАҚИДА"
	                 "\n\n8. ҚУРЪОНИ КАРИМ ОЯТЛАРИНИНГ АДАДИ ВА ҚУРЪОНИ КАРИМНИНГ ТАҚСИМИ ҲАҚИДА"
	                 "\n\n9. ВАҚФ‑ИБТИДО МАСАЛАСИ, САЖДА ОЯТЛАРИ ВА САКТА ЎРИНЛАРИ ҲАҚИДА"
	                 "\n\n10. ФОТИҲАДА БАСМАЛА МАСАЛАСИ"
	                 "\n\n11. УСМОН ТОҲО ҲАҚЛАРИДА"
	                 "\n\n12. МУСҲАФ РАСМИ ХАТИ ТАВФИҚИЙМИ?"
	                 "\n\nМУСҲАФ ИСТИЛОҲЛАРИ ШАРҲИ | 1-ҚИСМ"
	                 "\n\nМУСҲАФ ИСТИЛОҲЛАРИ ШАРҲИ | 2-ҚИСМ"
	                 "\n\nМУСҲАФ ИСТИЛОҲЛАРИ ШАРҲИ | 3-ҚИСМ", reply_markup=istiloh_sharh_keys)
	await state.set_state("ist")

@dp.message_handler(text = "Мусҳаф истилоҳлари шарҳи (1-қисм)", state="ist")
async def istiloh_bulingan(msg: types.Message, state:FSMContext):
	await msg.answer("Мусҳаф истилоҳлари шарҳи (1-қисм)", reply_markup=istiloh_keys)
	await state.set_state("ist1")

@dp.message_handler(text = "⏮ Oлдинги", state="ist1")
async def istiloh_birinchi(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги", reply_markup=istiloh_sharh_keys)
	await state.set_state("ist")

@dp.message_handler(text = "Суҳбатнинг қисмларга бўлинган шакли", state="ist1")
async def sharh_handler(msg: types.Message, state:FSMContext):
	for k,v in qisqa_dict.items():
		await msg.answer_video(video=v['v'], caption=v['c'] + quranuz)
		await state.set_state("ist")

@dp.message_handler(text = "Суҳбатнинг тўлиқ шакли", state="ist1")
async def sharh_handler(msg: types.Message, state:FSMContext):
	await msg.answer_video(video="BAACAgIAAxkBAAIFtGI_5l8xCLbdPrUAAZhWNvxd29rK3wACpB0AAnOKsUnak2UXCPzqeCME",
	                       caption="<b>МУСҲАФ ИСТИЛОҲЛАРИ ШАРҲИ | 1-ҚИСМ</b>"
	                       "\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>"
	                       "\n\n<a href='https://www.youtube.com/watch?v=xhHjOFK2nWU&list=PLE0uv2eFBCH1HYjsq28uu2ulZJakYMiWq&ab_channel=Quranuz\'>Youtube орқали кўриш</a>" + quranuz)
	await state.set_state("ist1")

@dp.message_handler(text = "Мусҳаф истилоҳлари шарҳи (2-қисм)", state="ist")
async def sharh_handler(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIFtmI_5mXLlkoGOXQupdiU-Y60ppacAAJvBgACcQ7gSEcbVbpd6xXaIwQ",
	                       caption="<b>МУСҲАФ ИСТИЛОҲЛАРИ ШАРҲИ | 2-ҚИСМ</b>"
	                       "\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>"
	                       "\n\n<a href='https://youtu.be/6PNgh2Mcgw8\'>Youtube орқали кўриш</a>" + quranuz)

@dp.message_handler(text = "Мусҳаф истилоҳлари шарҳи (3-қисм)", state="ist")
async def sharh_handler(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAIFuGI_5mpGxwlaofDmnqPef3NwldC3AAJ7BwACgsoQSXuTkVP8U3r3IwQ",
	                       caption="<b>МУСҲАФ ИСТИЛОҲЛАРИ ШАРҲИ | 3-ҚИСМ</b>"
	                       "\n\n<i>Қуръони Карим ходими\nҲасанхон Яҳё Абдулмажид</i>"
	                       "\n\n<a href='https://youtu.be/yP5w31GE_XA\'>Youtube орқали кўриш</a>" + quranuz)
