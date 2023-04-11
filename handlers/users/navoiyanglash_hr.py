from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from loader import dp

from keyboards.default.navoiyanglash_dk import nang_umum_keys, nang_aud_keys, nang_vid_keys

islomuz = "\n\n<a href='https://www.facebook.com/www.islom.uz'>Facebook</a> | <a href='https://www.instagram.com/islomuz_kanal/'>Instagram</a> | <a href='https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw'>Telegram</a> | <a href='https://www.youtube.com/user/islomuz?sub_confirmation=1'>Youtube</a>"

nang_dict = {14:{'v':'BAACAgIAAxkBAAEGOaFitCCCIrHvgChnCm1PWwtmG0Pq_QACAh0AAuyfiEnRRHWPoyS0nCkE','a':'CQACAgIAAxkBAAEGPClitGTfvU2nhUMBeAsFcMtEQ0_Z4gACqxoAAkjSoEk9pPiqGZZ32ikE','c':'<b>"Навоийни англаш сари" | Алишер Навоий ким бўлган? (14-суҳбат)</b>\n\n<a href=\'https://youtu.be/5aNSp1r5J6M\'>Youtube орқали кўриш</a>'},15:{'v':'BAACAgIAAxkBAAEGOaVitCHjzaT13zfIW1OThUtkQ4OTzgACqRwAAnSRmUkXxJw4XGuFoSkE','a': 'CQACAgIAAxkBAAEGPH5itGZSL319dnUg-Hx0GJSdWooUnQACshoAAkjSoElbyX-r2tQtKSkE','c': '<b>"Навоийни англаш сари" | "Ашрақат мин акси шамсил" ғазали шарҳи (15-суҳбат)</b>\n\n<a href=\'https://youtu.be/5aNSp1r5J6M\'>Youtube орқали кўриш</a>'},16: {'v': 'BAACAgIAAxkBAAEGhPNiupd-qnDFoWZKwtjwFPNqjacJ4QACqB4AAtoK0EkCSOTNFshWTCkE','a': 'CQACAgIAAxkBAAEGjp9iuwq8ICm5LW1hr2cpeJJJYZ_aEQACchcAAv4r2EkNSPyVwXpJqSkE','c': '<b>"Навоийни англаш сари" | "Шоҳ ва дарвеш" ғазали шарҳи (16-суҳбат)</b>\n\n<a href=\'https://youtu.be/gXTKytcY0QI\'>Youtube орқали кўриш</a>'}}

@dp.message_handler(text = "📑 Навоийни англаш сари")
async def nang_umum_hands(msg: types.Message, state:FSMContext):
	await msg.answer("<b>\"Навоийни англаш сари\"</b> туркум суҳбатлари.", reply_markup=nang_umum_keys)
	await state.set_state("nang")

@dp.message_handler(text = "🎧 Аyдиo", state="nang")
async def nang_aud_hands(msg: types.Message, state:FSMContext):
	await msg.answer("🎧 Ayдио", reply_markup=nang_aud_keys)
	await state.set_state("nanga")

@dp.message_handler(text = "⏮ Oлдинги", state="nanga")
async def nang_back_o(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги", reply_markup=nang_umum_keys)
	await state.set_state("nang")

@dp.message_handler(text = "🎬 Bидeo", state="nang")
async def nang_vid_hands(msg: types.Message, state:FSMContext):
	await msg.answer("🎬 Bидeо", reply_markup=nang_vid_keys)
	await state.set_state("nangv")

@dp.message_handler(text = "⏮ Oлдинги", state="nangv")
async def nang_back(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Oлдинги", reply_markup=nang_umum_keys)
	await state.set_state("nang")

@dp.message_handler(text = "1-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECk2RihptwyrbrCWuU_GHV48DhK4NsfgACMxYAAvbOOEgG_92KdtDfwyQE",
	                       caption="<b>\"Навоийни англаш сари\" | Муқаддима (1-cyҳбат, 1-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/BKZw0-5dKOM'>Youtube орқали кўриш</a>" + islomuz)

	await msg.answer_video(video="BAACAgIAAxkBAAECk2Zihpuh7dvhRfBfX-a5e-8SVV6yZAACNBYAAvbOOEgiFfq20O6F_SQE",
	                       caption="<b>\"Навоийни англаш сари\" | Исломда шеърият (1-cyҳбат, 2-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/j_WMzjOARDs?list=PLys356tU5j5TMWQKSxico62J6LojzleR-&t=1'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "2-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECk21ihpwWfxbVJo3h0jELA0tsQeHlxAACOBYAAvbOOEiUON0qcn0ubiQE",
	                       caption="<b>\"Навоийни англаш сари\" | Сийратда шеърият (2-cyҳбат, 1-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/ugnxZYHmbv0'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECk3NihpxNcmQQSIRg53KzTNB5GZOhBAACORYAAvbOOEiG6dQnwMFF3CQE",
	                       caption="<b>\"Навоийни англаш сари\" | Сийратда шеърият (2-cyҳбат, 2-қисм) </b>" 
	                               "\n\n<a href='https://youtu.be/P-6h-Y9WvAA'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "3-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECk3Vihpx12KUdc0kdWscQ8ENcro9qXwACOhYAAvbOOEhS7PCkc_30QSQE",
	                       caption="<b>\"Навоийни англаш сари\" | Шеъриятнинг фойда ва зарарлари (3-суҳбат, 1-қисм) </b>" 
	                               "\n\n<a href='https://youtu.be/MzBdea66NME'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECl8tihv_9Lz7erxOwsw3u1EYt4pxnqgACKBcAAvbOOEjBJVyGYBwAATwkBA",
	                       caption="<b>\"Навоийни англаш сари\" | Саҳобалар ҳаётида шеърият (3-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://www.youtube.com/watch?v=M57Er2u43zs&list=PLys356tU5j5TMWQKSxico62J6LojzleR-&index=6'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "4-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECl9lihwABOBtNPp443v7aPeJWsAwqiEwAAikXAAL2zjhIpgTDca35CzYkBA",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф ҳақида (4-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/nblTq6m1i9Y'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECl-ZihwABWrhLSkVDoobyu-Q1Nym8vA0AAioXAAL2zjhIDZbEt0gPp4kkBA",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф ҳақида (4-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/Yzm23uW-1pA'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "5-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECmEZihwLTMbiAK6kuyE7Fy_MuDgyfAgACsR8AAnf_AUn4NvZ8fKeE5SQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф: мақом ва мартабалар (5-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/QL1Q_B0HePQ'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECmEhihwLa0dWfnrFdg1r2ILCbb2y6EAACfBoAAoIbIEmPrjmq-jZKzyQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф: мақом ва мартабалар (5-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/muQmUO-oABg'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "6-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECmEpihwLpR2JQTofSC3RX5qDMk9tUBwAC7x8AAuJOgEnSL9QHJv1MLSQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф: Қуръон ва суннат йўлидир (6-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/DAcbIv2rlSw'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECmExihwLw8WBGbhnY06Yj_lbFYW5ikwACgxQAAs-bSUm6-OJYRdWF-iQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф: ҳол ва мақом тушунчалари (6-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/ialpmRCkmxk'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "7-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECmFVihwNRMqTlDTKHzbs2xJAbL9_beAACMRcAAvbOOEjUAAH7h5SCIj8kBA",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф: ҳол ва мақом ўртасидаги фарқлар (7-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/GupX1jstNr4?list=PLys356tU5j5TMWQKSxico62J6LojzleR-'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECmFdihwQxsQzSI4rXUTTTbU9dGrbBIwACLBkAAr1dkUnSC9vfUEVKJiQE",
	                       caption="<b>\"Навоийни англаш сари\" | Қабз ва баст мақомлари (7-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/xpwzTu4FWhY'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "8-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECmFlihwQ3rdNZa8khHhWnMJcaM5W3vwACDBcAAuzpwEllAvjBMII68yQE",
	                       caption="<b>\"Навоийни англаш сари\" | Ҳайбат ва унс мақомлари (8-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/7IAT57IQ4JE'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECmFtihwRICqfosqVgQRGoasZjRonfgQACRRUAAt9s2UmtWjUaYsL3XiQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тажовуд, Важд ва Вужуд тушунчалари (8-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/2G0zjk-RBj0'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECmF1ihwRVDaEcQ3GSrb5l0-KTozka5QAC2xUAArArGEqnp1xFxl0qmiQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тавҳид ва муроқаба мақомлари (8-суҳбат, 3-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/hCOglYcsH7o'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "9-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAECmF9ihwSsG1tCdNJ-1mO2Z0kLqMCsmQACMhcAAvbOOEhYn0awFxq4PyQE",
	                       caption="<b>\"Навоийни англаш сари\" | Фано ва Бақо мақомлари (9-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/I16EJDCPsts'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAECmGJihwTP7e6mrqrM_bqoAAHBdbqAzxEAAlcbAAK66ylI2uBjW_G_oxQkBA",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуфдаги баъзи руҳий ҳолатлар (9-суҳбат, 2-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/c9HTVbiFwrU'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "10-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAEDNDFij48x15r74qfmXLeqrrOb6g7W3QACShkAAuNocEgofZtxdRp14iQE",
	                       caption="<b>\"Навоийни англаш сари\" | Муҳаббатнинг даражалари (10-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/TqYoa6NxLP4'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAEDyiNinaTx-vXOEXtoMcsNzRASIh2DcwAC0hsAAmihgUh5k2S_kDbK-yQE",
	                       caption="<b>\"Навоийни англаш сари\" | Муҳаббатнинг даражалари (10-суҳбат, 2-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/-4VTH0SqCu4'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "11-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAEDyilinaUNvlvZZh0HFSidpwqRcDx0ywACHB4AAhVFqEiaLaOBj7mjWyQE",
	                       caption="<b>\"Навоийни англаш сари\" | Аллоҳга бўлган муҳаббат (11-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/ShU6avgVevQ'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAEDyitinaU1uRKOVfoVCWUnTNXxZ2hYzAACZxsAAu0ZwEhxfe5zFxfALCQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф шеърияти (11-суҳбат, 2-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/YskCN_y6qYY'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "12-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAEDyjVinaVE9pV_ENZKaxUYGhQXPVrZ8wACZhwAAlMg0EjYnsMzR0Bo_SQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф шеърият чўққиси (12-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/TfDPEgKgDL0'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAEFKiJip0HaRrJtttJqw89x95KwZ4Zu4AAC_RoAAiJvCUkOKFLOse5tgyQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф шеърият истилоҳлари ҳақида (12-суҳбат, 2-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/ubZcT0UN2Y0'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "13-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video="BAACAgIAAxkBAAEFTGVip_3OzM9iEICWffJGwzOeGniZ4wACQBoAAlP_OUkklScFDLjzjyQE",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф шеърият истилоҳлари изоҳи (13-суҳбат, 1-қисм)</b>" 
	                               "\n\n<a href='https://youtu.be/946t3muGqFU'>Youtube орқали кўриш</a>" + islomuz)
	await msg.answer_video(video="BAACAgIAAxkBAAEFtTxiq8PEDFUAAcgmY5Q3a5FkCfeAN9wAAlwZAAL2Y1FJ5IpJ1rBLIBYkBA",
	                       caption="<b>\"Навоийни англаш сари\" | Тасаввуф шеърияти истилоҳлари (13-суҳбат, 2-қисм)</b>"
	                               "\n\n<a href='https://youtu.be/dhMQEc_8Ric'>Youtube орқали кўриш</a>" + islomuz)

@dp.message_handler(text = "14-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video=nang_dict[14]['v'], caption=nang_dict[14]['c'] + islomuz)

@dp.message_handler(text = "15-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video=nang_dict[15]['v'], caption=nang_dict[15]['c'] + islomuz)

@dp.message_handler(text = "16-cyҳбат", state="nangv")
async def nang_vid(msg: types.Message):
	await msg.answer_video(video=nang_dict[16]['v'], caption=nang_dict[16]['c'] + islomuz)

@dp.message_handler(text = "1-3 суҳбатлар", state="nanga")
async def nang_aud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmqVihxnoNYf5GaT51ygsf0Xcl_A6rAACVhcAAvbOOEj0yt916RWawCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmqpihxnu_uZKf7l7XZnrBMCUcaPDSQACWBcAAvbOOEg1g4XARX9qYCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmq9ihxn1w6pUHet-dsxD00AvCcguRQACWRcAAvbOOEgqW-SSJGvVqyQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmrRihxn686rd_lsjsfvP4pzP0qKSzgACWhcAAvbOOEgjZSB_cbPxJyQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmrZihxoBcCnPLYOaCKlMUDv08Cg0mAACXBcAAvbOOEiKhPHCQquaSyQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmrhihxoHhlQtIYHzH3Xv48m8C6nCegACXRcAAvbOOEhHzvvwiSR_TyQE")

@dp.message_handler(text = "4-6 суҳбатлар", state="nanga")
async def nang_aud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmrpihxoNGaBFnC4t24uPg0ADjG8pPwACXhcAAvbOOEhzTDx68NXmxSQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmrxihxoQXfY7iqSdCFygKWm-EWxbcgACXxcAAvbOOEiRZcIAAUSz1BIkBA")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmr5ihxoZEB0VYDZ0ibiWN9EfAAGPJPcAAmEXAAL2zjhIcxXsK9pQvAYkBA")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmsBihxonmPTvWfZt_QE4O2nNw7sv4wACYhcAAvbOOEggzfJE-RjO-SQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmsRihxoyAVRex9v-2tsSc1UAAe3P2LQAAmMXAAL2zjhI9qHMzAYtti0kBA")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmsZihxo_dkgIlwRLqibqyTl8TA-HcAACZRcAAvbOOEjMnjhpIIwjviQE")

@dp.message_handler(text = "7-9 суҳбатлар", state="nanga")
async def nang_aud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmslihxpICUTfjtuiO5NqBXTZpXULAwACZhcAAvbOOEjwC-AWGMBdMCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmstihxpRAAHDpwV6MoldAAHDbi5YieUoAAJnFwAC9s44SCutL4APZ6nrJAQ")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECms1ihxpYJ-rE68ARuh01ZprWhk7xkQACaBcAAvbOOEhGO0LqGU-lgCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmtJihxpg6fDz8BXV4owVax8fOa6pVQACaRcAAvbOOEgxXQfUdTugwCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmtRihxpm_TwiK8U9hPeVJN5xn2RKQAACahcAAvbOOEiXocDY2bTSWSQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmtlihxpwMglueE3th1aVSaaetqHXmgACaxcAAvbOOEh98Yax-2SJ-SQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAECmttihxp9k90L2AyAV8X0pubgypLtGAACbBcAAvbOOEiaoL50zJL1xCQE")

@dp.message_handler(text = "10-12 суҳбатлар", state="nanga")
async def nang_aud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAEEBbFinfrw0HYDTnzx-6vWvQt_a6HPpAACEhoAAh-E8EgQ1s6SxKMWdyQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEEBoZinfwy_pyIP6gQRS2fAn_IN2mcgwACFBoAAh-E8EhhYsxNn3B97CQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEEBsNinfzmaLX3soiKgiBuv0yl6nRM1QACFRoAAh-E8EgvK7OC2UylBSQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEEBwNinf3YyHdIk8TDS4DVvJiHIaKY2wACGxoAAh-E8EjdkOS1OUqgHCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEEB39inf6FH5WMwKEccJoyBONs33yy8gACHRoAAh-E8Ej20Bv5sIyADCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEFKcBipz_fpXuZd5b48KvF0dkI3l3qNAACBhsAAmZtOUlg6WbgOJBltSQE")

@dp.message_handler(text = "13-15 суҳбатлар", state="nanga")
async def nang_aud(msg: types.Message):
	await msg.answer_audio(audio="CQACAgIAAxkBAAEFUtRiqBrrwe8X5t7G2DlyTXioqj5DTwAChBcAAmZtQUnNCtbeRVo5QCQE")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEGK_disz05FTPlKc_JFCs7cPSJXUh3YQACRhwAAq4ymEkU7x6bPf7k9ikE")
	await msg.answer_audio(audio=nang_dict[14]['a'], caption=nang_dict[14]['c'])
	await msg.answer_audio(audio=nang_dict[15]['a'], caption=nang_dict[15]['c'])

@dp.message_handler(text = "16 - суҳбат", state="nanga")
async def nang_aud(msg: types.Message):
	await msg.answer_audio(audio=nang_dict[16]['a'], caption=nang_dict[16]['c'])
