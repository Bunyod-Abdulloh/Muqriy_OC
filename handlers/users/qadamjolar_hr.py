from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from loader import dp

from keyboards.default.qadamjolar_dk import qadamjolarvid, qadamjolaraud, qadamjolarumum

qadamjolar = {1:{'v':'BAACAgIAAxkBAAEFpM5iqyfru7XJQzOvYKimLfQxM34YlwACAxIAAtMiqEgYWGM8jiXh3CQE','a':'CQACAgIAAxkBAAEFymBirRBQKpXT0Gl7JH9Y6aK36YHB2wACmBwAAg10aUmWdcnsqNL7CCQE','c':'Умра сафарига борувчилар учун маслаҳатлар | Расулуллоҳ ﷺ қадамжолари\n\n<a href=\'https://www.youtube.com/watch?v=HFGmbAxYh5o\'>Youtube орқали кўриш</a>'},
              2:{'v':'BAACAgIAAxkBAAEFpO5iqyi-WviNiwZJI8x3vHNFYd1TVQACmRMAAhnfQUuW0pAp-gpldSQE','a':'CQACAgIAAxkBAAEFymVirRBohf5Le9mWa6mX4q_g3QqcbwACmRwAAg10aUkj1FpcFoUSryQE','c':'Уҳуд тоғи. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/4tdUD-7nW_E\'>Youtube орқали кўриш</a>'},
              3:{'v':'BAACAgIAAxkBAAEFpPBiqyjJfB9wdAup9BSZ32-jMYJM_gACJhQAAtxEeEv2FDzqytSXLyQE','a':'CQACAgIAAxkBAAEFymhirRCJJwVTIrBVel-LAAEKaFsG_RgAApocAAINdGlJyKISqp1779kkBA','c':'Эҳромга кириш ва умрага ният қилиш. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/oEiTMrSB9jU\'>Youtube орқали кўриш</a>'},
              4:{'v':'BAACAgIAAxkBAAEFtQZiq78CJ7NaFw80jBbY8y0YqLtE8AACMyEAAplPYEmM7yF2NNsPYyQE','a':'CQACAgIAAxkBAAEFympirRCTSWbU42iQEVr67Hr8vO4AAfwAApscAAINdGlJKhIVIAzdktkkBA','c':'Савр тоғи. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/IpQRx8v--ak\'>Youtube орқали кўриш</a>'},
              5:{'v':'BAACAgIAAxkBAAEFtStiq8AupTVYB0UFkORY7cFCbEal3AACNCEAAplPYEmqu2EgZBLiISQE','a':'CQACAgIAAxkBAAEFymxirRCbprWlpyPYU9mUDCErV2PEBgACnBwAAg10aUkvMJuQBsT0YCQE','c':'Икки қиблали масжид. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/TXkAk48xtiQ\'>Youtube орқали кўриш</a>'},
              6:{'v':'BAACAgIAAxkBAAEFtS1iq8CabnC2JAJ0boy2c7cNFPtB8gACNSEAAplPYEkq-F-A8TW8sCQE','a':'CQACAgIAAxkBAAEFym5irRClKgZJnDtltA6Tzok8LQABV0QAAp0cAAINdGlJq-Bg1yZXrGskBA','c':'Қизил тоғ (Дажжол тушадиган ер). | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/ePS4Fx1F5GI\'>Youtube орқали кўриш</a>'},
              7:{'v':'BAACAgIAAxkBAAEFtYFiq8c2Qtv05D8DNOgvrfkjAAGO6usAAjYhAAKZT2BJ5GbHbnMumkokBA','a':'CQACAgIAAxkBAAEFynBirRDIox3DFWyIXNz2Y94FdhAZcAACnxwAAg10aUlv34X9f7dUoSQE','c':'Масжидул-ҳаромга боришдан олдин нималарни билиш керак? | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/W7asFial21U\'>Youtube орқали кўриш</a>'},
              8:{'v':'BAACAgIAAxkBAAEFtZpiq8scpkeVAAGELFcO1UfoZ5EfqeMAAjghAAKZT2BJRc1c0OSgmXIkBA','a':'CQACAgIAAxkBAAEFynJirRD864bwZf30vnVCBN2K3vJQKwACoBwAAg10aUnmAtzLRfjMUyQE','c':'Масжидул-ҳаромдаги жоиз ва ножоиз амаллар. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/9cv6k5MBe_A\'>Youtube орқали кўриш</a>'},
              9:{'v':'BAACAgIAAxkBAAEFtZ5iq81LsRsWQHZEfcQW5rcJ-JpdEAACOiEAAplPYEmY2dswVYgI-CQE','a':'CQACAgIAAxkBAAEFynRirREFweNj7mzZzuBUlgoV5wyXcQACoRwAAg10aUlmwLwoVGEnZCQE','c':'Эҳромдан чиқишнинг шарти. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/10i30RJ-vEs\'>Youtube орқали кўриш</a>'},
              10:{'v':'BAACAgIAAxkBAAEMeSBjK9VLFKTfrkOOjnWsAUXbXGNOmQACohIAAuJOiEmKp0tcuE7D-ikE','a':'CQACAgIAAxkBAAEFynZirRGsE4i_63FmhZVqayL7x_pVdwACohwAAg10aUl5Y2RWhAABiJIkBA','c':'Сафо ва Марва. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/IRL0Xcqg5QU\'>Youtube орқали кўриш</a>'},
              11:{'v':'BAACAgIAAxkBAAEFtaZiq9BlE4-64lwwOFyo6Hlww-hVgwACPSEAAplPYEk2SbRjKu_sUyQE','a':'CQACAgIAAxkBAAEFynhirRG3lhXaqqKTX_n2FnPNSFVRWwACoxwAAg10aUnGdkgQIrHk_iQE','c':'Абдуллоҳ ибн Аббос розияллоҳу анҳунинг масжидлари. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/n-ajFoKObOE\'>Youtube орқали кўриш</a>'},
              12:{'v':'BAACAgIAAxkBAAEFtjZiq9Nwp7aKjtloG7YubhhoeCd2kQACQyEAAplPYEmHX4Ama2QMgiQE','a':'CQACAgIAAxkBAAEFynpirRHO4HvOCjMTY7Ue1Vels0D9DwACpBwAAg10aUn3YtLNdAAB1rgkBA','c':'Азақ қудуғи. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/QMMF0iDpA-c\'>Youtube орқали кўриш</a>'},
              13:{'v':'BAACAgIAAxkBAAEFtkViq9VulAABywZSj9g9cetyKYFH8QcAAkshAAKZT2BJl5lxMW3l3v4kBA','a':'CQACAgIAAxkBAAEFynxirRHzBu7dY9JmBUtR5CONBD_JwQACpRwAAg10aUnQ5X1fQIrZDiQE','c':'Жума масжиди. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/nqxCQ7S2nWU\'>Youtube орқали кўриш</a>'},
              14:{'v':'BAACAgIAAxkBAAEFtk1iq9afT3vRhkUEX8TfXkRHJTpLxQACTCEAAplPYEnKirE3B2MUvCQE','a':'CQACAgIAAxkBAAEFyoBirRICu6RzImlI_k3-v9VXC6FlhgACphwAAg10aUn1l5RZ6vYX_SQE','c':'Каъб ибн Ашраф қасри. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/-IeyGt0iHBw\'>Youtube орқали кўриш</a>'},
              15:{'v':'BAACAgIAAxkBAAEFtvtiq-lEF8dQmRC5B5xb-DEEHSuO5wACtxkAAslSQUkVEvOQ1hBzvSQE','a':'CQACAgIAAxkBAAEFyoNirRIvw9kmhlPcIbifcFOxsw8BQAACpxwAAg10aUmDf88m2VqrZyQE','c':'Ижоба масжиди. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/7dzw8zV8M9Q\'>Youtube орқали кўриш</a>'},
              16:{'v':'BAACAgIAAxkBAAEMeS5jK9Wf9_DTJqyyJdKwcvXi5NzY1QAC0hoAAob3kUmtOh1tDVJjrSkE','a':'CQACAgIAAxkBAAEGPBBitGK__LjmSsFB59tS74I51f3SBAACkxoAAkjSoEn6hlMN2fBZqykE','c':'Сажда масжиди. | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/Y6J6knuCvaE\'>Youtube орқали кўриш</a>'},
              17:{'v':'BAACAgIAAxkBAAEGm0livBjIMJ6ywVcHUl1EyoEDoT5NrAACfxkAAu9C2UmuVkPq46uKSikE','a':'CQACAgIAAxkBAAEJCLFi_apOS_p5dZoB8kF0CpX_jGibggACpRcAAt6r8Eu-vRSqODGmnykE','c':'Бану Соъида сақифаси | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/7tqHYTV3k5w\'>Youtube орқали кўриш</a>'},
              18:{'v':'BAACAgIAAxkBAAEHScBizRsW0cX9VhM4CBMnE6wKjwUEmAACORkAAgjeaEq-M5pJYVzRfikE','a':'CQACAgIAAxkBAAEJCL1i_apqN344js6K1M3_V1ipEw5QGQACqRcAAt6r8EvUSNAHaTQGkikE','c':'Раҳмат тоғи | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://www.youtube.com/watch?v=rJSL4nwU-mo\'>Youtube орқали кўриш</a>'},
              19:{'v':'BAACAgIAAxkBAAEHU9hizZ8EWdjTYxB5JPP5MzcJhop5vQACcxkAAnj8aEruUkAKbfxy1SkE','a':'CQACAgIAAxkBAAEJCMFi_ap0azr2IxpfH17mv5KB3cwvfwACqxcAAt6r8EuvyYTZ7LZlhCkE','c':'Зубайдахоним қудуғи | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/-6Batx62G6A\'>Youtube орқали кўриш</a>'},
              20:{'v':'BAACAgIAAxkBAAEHwwABYtdkuvHn-RMdV8AZf19xlOOBsz8AAvkcAAIngrlK2Zv2ss-XbtQpBA','a':'CQACAgIAAxkBAAEJCLNi_apZsLul9kvwYBucy9G2Y4F7ZQACphcAAt6r8Euxis-vUJXu0ykE','c':'Мино водийси | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/X-duk6ba0Kg\'>Youtube орқали кўриш</a>'},
              21:{'v':'BAACAgIAAxkBAAEIUX1i6RyMiYfrWU0MlT2NXOkZYGFDtgACpBkAArabCEudMdvgO_8T5SkE','a':'CQACAgIAAxkBAAEJCLli_aphqANIkxIILvSJ6--qJ-xAvwACpxcAAt6r8EuOo9srts74aykE','c':'Қодамун набий | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/7d7i4_oo7QU\'>Youtube орқали кўриш</a>'},
              22:{'v':'BAACAgIAAxkBAAEMecNjK-aetrye3wrSMO6B1FIUII9Z4wACkiAAAqwtYEkuYcnkenxKTykE','a':'CQACAgIAAxkBAAEMef1jK-dwt0NApGIaPeBHBWOFChLIJgAClSAAAqwtYEnGnD0J-Q3RTSkE','c':'Ғорс қудуғи | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/vmnIiF1M7XA\'>Youtube орқали кўриш</a>'},
              23:{'v':'BAACAgIAAxkBAAEIwz9i9mLB_bLHyf3wYvaLGuAsoUeX5AAC7xwAAm0auEvIDcZPN9YuOykE','a':'CQACAgIAAxkBAAEJCL9i_apvPaLbOHus_lbYkFm8jPieOwACqhcAAt6r8EuBX3rES31WzSkE','c':'Салмон Форсий қудуғи | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/i-zZ8hXxVNA\'>Youtube орқали кўриш</a>'},
              24:{'v':'BAACAgIAAxkBAAEJCHZi_aHcpyUCVD2ho2GufSU4aMP2zQACnhcAAt6r8EsV-fux7RkeHCkE', 'a':'CQACAgIAAxkBAAEJCLti_aplS7_lNgPJmGcSQK_aKT1JaQACqBcAAt6r8EsfOlcJVgFAdykE', 'c':'Ҳазрати Усмон қудуғи | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://www.youtube.com/watch?v=rSPwCZCmlik\'>Youtube орқали кўриш</a>'},
              25:{'v':'BAACAgIAAxkBAAEMee5jK-dBMoeQwDNVRQ-BDgABEnUDpwsAApQgAAKsLWBJvRgEhEWOv6YpBA','a':'CQACAgIAAxkBAAEMef9jK-d68O7jkBILOunOAiiVfy-iXwACliAAAqwtYEkCfjgHzjR6gykE','c':'Расулуллоҳ ﷺ таваллуд топган уй | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'https://youtu.be/zSDVjTWCNgE\'>Youtube орқали кўриш</a>'}} #'v':'','c':' | Расулуллоҳ  ﷺ қадамжолари\n\n<a href=\'\'>Youtube орқали кўриш</a>'
islomuz = '\n\n<a href=\'https://www.facebook.com/www.islom.uz\'>Facebook</a> | <a href=\'https://www.instagram.com/islomuz/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAEHZQeuVw_Jq0k57Bw\'>Telegram</a> | <a href=\'https://www.youtube.com/user/islomuz?sub_confirmation=1\'>Youtube</a>'

@dp.message_handler(text = "📍 Расулуллоҳ ﷺ қадамжолари")
async def qadamjovid(msg: types.Message, state:FSMContext):
	await msg.answer("📍 Расулуллоҳнинг қадамжолари", reply_markup=qadamjolarumum)
	await state.set_state("qad0")

@dp.message_handler(text = "🔈 Aудио", state="qad0")
async def qadamjovid(msg: types.Message, state:FSMContext):
	await msg.answer("🔈 Aудио", reply_markup=qadamjolaraud)
	await state.set_state("qad1")

@dp.message_handler(text = "⏮ Олдинги", state="qad1")
async def qadamjovid(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Олдинги", reply_markup=qadamjolarumum)
	await state.set_state("qad0")

@dp.message_handler(text = "🎞 Bидео", state="qad0")
async def qadamjovid(msg: types.Message, state:FSMContext):
	await msg.answer("🎞 Bидео", reply_markup=qadamjolarvid)
	await state.set_state("qad2")

@dp.message_handler(text = "⏮ Олдинги", state="qad2")
async def qadamjovid(msg: types.Message, state:FSMContext):
	await msg.answer("⏮ Олдинги", reply_markup=qadamjolarumum)
	await state.set_state("qad0")

@dp.message_handler(text = "Умра сафарига борувчилар учун маслаҳатлар", state="qad2")
async def qadamjovid(msg:types.Message):
	await msg.answer_video(video=qadamjolar[1]['v'], caption=qadamjolar[1]['c'] + islomuz)

@dp.message_handler(text = 'Уҳуд тоғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[2]['v'], caption=qadamjolar[2]['c'] + islomuz)

@dp.message_handler(text = 'Эҳромга кириш ва умрага ният қилиш', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[3]['v'], caption=qadamjolar[3]['c'] + islomuz)

@dp.message_handler(text = 'Савр тоғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[4]['v'], caption=qadamjolar[4]['c'] + islomuz)

@dp.message_handler(text = 'Икки қиблали масжид', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[5]['v'], caption=qadamjolar[5]['c'] + islomuz)

@dp.message_handler(text = 'Қизил тоғ', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[6]['v'], caption=qadamjolar[6]['c'] + islomuz)

@dp.message_handler(text = 'Масжидул-ҳаромга киришдан олдин нималарни билиш керак?', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[7]['v'], caption=qadamjolar[7]['c'] + islomuz)

@dp.message_handler(text = 'Масжидул-ҳаромдаги жоиз ва ножоиз амаллар', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[8]['v'], caption=qadamjolar[8]['c'] + islomuz)

@dp.message_handler(text = 'Эҳромдан чиқишнинг шарти', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[9]['v'], caption=qadamjolar[9]['c'] + islomuz)

@dp.message_handler(text = 'Сафо ва Марва', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[10]['v'], caption=qadamjolar[10]['c'] + islomuz)

@dp.message_handler(text = 'Абдуллоҳ ибн Аббос розияллоҳу анҳунинг масжидлари', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[11]['v'], caption=qadamjolar[11]['c'] + islomuz)

@dp.message_handler(text = 'Азақ қудуғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[12]['v'], caption=qadamjolar[12]['c'] + islomuz)

@dp.message_handler(text = 'Жума масжиди', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[13]['v'], caption=qadamjolar[13]['c'] + islomuz)

@dp.message_handler(text = 'Каъб ибн Ашраф қасри', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[14]['v'], caption=qadamjolar[14]['c'] + islomuz)

@dp.message_handler(text = 'Ижоба масжиди', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[15]['v'], caption=qadamjolar[15]['c'] + islomuz)

@dp.message_handler(text = 'Сажда масжиди', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[16]['v'], caption=qadamjolar[16]['c'] + islomuz)

@dp.message_handler(text = 'Бану Соъида сақифаси', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[17]['v'], caption=qadamjolar[17]['c'] + islomuz)

@dp.message_handler(text = 'Раҳмат тоғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[18]['v'], caption=qadamjolar[18]['c'] + islomuz)

@dp.message_handler(text = 'Зубайдахоним қудуғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[19]['v'], caption=qadamjolar[19]['c'] + islomuz)

@dp.message_handler(text = 'Мино водийси', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[20]['v'], caption=qadamjolar[20]['c'] + islomuz)

@dp.message_handler(text = 'Қодамун набий', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[21]['v'], caption=qadamjolar[21]['c'] + islomuz)

@dp.message_handler(text = 'Ғорс қудуғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[22]['v'], caption=qadamjolar[22]['c'] + islomuz)

@dp.message_handler(text = 'Салмон Форсий қудуғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[23]['v'], caption=qadamjolar[23]['c'] + islomuz)

@dp.message_handler(text = 'Ҳазрати Усмон қудуғи', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[24]['v'], caption=qadamjolar[24]['c'] + islomuz)

@dp.message_handler(text = 'Расулуллоҳ ﷺ таваллуд топган уй', state="qad2")
async def qadamjovid(msg: types.Message):
	await msg.answer_video(video=qadamjolar[25]['v'], caption=qadamjolar[25]['c'] + islomuz)

@dp.message_handler(text = '1-4', state="qad1")
async def qadamjoaud(msg: types.Message):
	await msg.answer_audio(audio=qadamjolar[1]['a'], caption=qadamjolar[1]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[2]['a'], caption=qadamjolar[2]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[3]['a'], caption=qadamjolar[3]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[4]['a'], caption=qadamjolar[4]['c'] + islomuz)

@dp.message_handler(text = '5-8', state="qad1")
async def qadamjoaud(msg: types.Message):
	await msg.answer_audio(audio=qadamjolar[5]['a'], caption=qadamjolar[5]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[6]['a'], caption=qadamjolar[6]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[7]['a'], caption=qadamjolar[7]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[8]['a'], caption=qadamjolar[8]['c'] + islomuz)

@dp.message_handler(text = '9-12', state="qad1")
async def qadamjoaud(msg: types.Message):
	await msg.answer_audio(audio=qadamjolar[9]['a'], caption=qadamjolar[9]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[10]['a'], caption=qadamjolar[10]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[11]['a'], caption=qadamjolar[11]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[12]['a'], caption=qadamjolar[12]['c'] + islomuz)

@dp.message_handler(text = '13-16', state="qad1")
async def qadamjoaud(msg: types.Message):
	await msg.answer_audio(audio=qadamjolar[13]['a'], caption=qadamjolar[13]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[14]['a'], caption=qadamjolar[14]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[15]['a'], caption=qadamjolar[15]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[16]['a'], caption=qadamjolar[16]['c'] + islomuz)

@dp.message_handler(text = '17-20', state="qad1")
async def qadamjoaud(msg: types.Message):
	await msg.answer_audio(audio=qadamjolar[17]['a'], caption=qadamjolar[17]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[18]['a'], caption=qadamjolar[18]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[19]['a'], caption=qadamjolar[19]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[20]['a'], caption=qadamjolar[20]['c'] + islomuz)

@dp.message_handler(text = '21-25', state="qad1")
async def qadamjoaud(msg: types.Message):
	await msg.answer_audio(audio=qadamjolar[21]['a'], caption=qadamjolar[21]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[22]['a'], caption=qadamjolar[22]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[23]['a'], caption=qadamjolar[23]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[24]['a'], caption=qadamjolar[24]['c'] + islomuz)
	await msg.answer_audio(audio=qadamjolar[25]['a'], caption=qadamjolar[25]['c'] + islomuz)
