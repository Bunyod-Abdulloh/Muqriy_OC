from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from loader import dp

from keyboards.default.qasam_dk import qasam_bosqichlar, qasam01_default, qasam02_default, qasam03_default
from keyboards.default.start_dk import main_keyboard

@dp.message_handler(text='🕌 Ўн кеча билан қасам')
async def qasam_category(message: types.Message, state:FSMContext):
    await message.answer('"Ўн кеча билан қасам" туркум дарслари 3 босқичдан иборат. '
                         '\nУшбу дарслар орқали Сиз 10 кунда Қуръон ўқишни ўрганасиз.'
                         '\nҲар бир дарснинг остига дарснинг PDF шакли ҳам жойланган.\n<a href=\'https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg\'>Вазифаларни '
                         'бажариш канали</a>га аъзо бўлиб дарслардан олган билимларингизни мустаҳкамлаб боришингиз мумкин.',reply_markup=qasam_bosqichlar)
    await state.set_state("onm")

@dp.message_handler(text='Биринчи босқич', state="onm")
async def qasam_birinchi(message: types.Message, state:FSMContext):
    await message.answer("Биринчи босқич қуйидаги мавзуларни ўз ичига олади:"
                         "\n\nМУҚАДДИМА"
                         "\n\nАРАБ ҲАРФЛАРИ ВА УЛАРНИНГ ИМЛОСИ"
                         "\n\nНУТҚ ТОВУШЛАРИ. АРАБ ТИЛИГА ХОС УНДОШЛАР"
                         "\n\nНУТҚ ТОВУШЛАРИ. АРАБ ВА ЎЗБЕК ТИЛИДА МУШТАРАК БЎЛГАН НУТҚ ТОВУШЛАРИ"
                         "\n\nУНЛИЛАР ВА ЙЎҒОН УНДОШЛАР"
                         "\n\nТАШДИД ВА ТАНВИН"
                         "\n\nВАЗИФАЛАРНИ БАЖАРИШ БЎЙИЧА ТАВСИЯЛАР"
                         "\n\nТЎГАРАК ТĀ ҲАМДА АЛФИЙЯ ВĀВ ВА АЛФИЙЯ ЙĀ"
                         "\n\nВАҚФ, ИБТИДО ВА ВАСЛ. АЙИРУВЧИ ҲАМЗА ВА БОҒЛОВЧИ ҲАМЗА"
                         "\n\nМАД. ТАФХИМ ВА ТАРҚИҚ. ЛАФЗИ ЖАЛОЛА"
                         "\n\nЁЗИЛСА-ДА, ЎҚИЛМАЙДИГАН ҲАРФЛАР"
                         "\n\nВАҚФ. МУСҲАФДА СУКУН ВА ТАНВИН ИФОДАСИ"
                         "\n\n\"ЎН КЕЧА БИЛАН ҚАСАМ\" ДАСТУРИ ВА ҚУРЪОН ЁДЛАШ"
                         " БОРАСИДА БЕРИЛГАН САВОЛЛАРГА ЖАВОБЛАР",reply_markup=qasam01_default)
    await state.set_state("onb")

@dp.message_handler(text = "⏮ Олдинги", state="onb")
async def qadamjovid(msg: types.Message, state:FSMContext):
    await msg.answer("⏮ Олдинги", reply_markup=qasam_bosqichlar)
    await state.set_state("onm")

@dp.message_handler(text='Иккинчи босқич', state="onm")
async def qasam_ikkinchi(message: types.Message, state:FSMContext):
    await message.answer("Иккинчи босқич қуйидаги мавзуларни ўз ичига олади: "
                         "\n\nҚУРЪОНИ КАРИМ ТИЛОВАТИГА МАРҲАБО!"
                         "\n\nФОТИҲА СУРАСИ"
                         "\n\nАН-НАС СУРАСИ"
                         "\n\nФАЛАҚ СУРАСИ"
                         "\n\nИХЛОС СУРАСИ"
                         "\n\nМАСАД СУРАСИ"
                         "\n\nНАСР СУРАСИ"
                         "\n\nКОФИРУН СУРАСИ"
                         "\n\nКАВСАР СУРАСИ"
                         "\n\nМОЪУН СУРАСИ"
                         "\n\nҚУРАЙШ СУРАСИ",reply_markup=qasam02_default)
    await state.set_state("oni")

@dp.message_handler(text = "⏮ Олдинги", state="oni")
async def qadamjovid(msg: types.Message, state:FSMContext):
    await msg.answer("⏮ Олдинги", reply_markup=qasam_bosqichlar)
    await state.set_state("onm")

@dp.message_handler(text='Учинчи босқич', state="onm")
async def qasam_uchinchi(message: types.Message, state:FSMContext):
    await message.answer("Учинчи босқич қуйидаги мавзуларни ўз ичига олади: "
                         "\n\nМУҚАДДИМА"
                         "\n\nАЗОН ВА ИҚОМА"
                         "\n\nИНТИҚОЛ - ЎТИШ ЗИКРЛАРИ"
                         "\n\nНАМОЗ АМАЛЛАРИДАГИ ЗИКРЛАР"
                         "\n\nНАМОЗ АМАЛЛАРИДАГИ ЗИКРЛАР(қаъдада ўқиладиган зикрлар)"
                         "\n\nНАМОЗ АМАЛЛАРИДАГИ ЗИКРЛАР(қаъдада ўқиладиган дуолар)"
                         "\n\nҚУНУТ ДУОСИ"
                         "\n\nНАМОЗДАН КЕЙИНГИ ЗИКРЛАР"
                         "\n\nОЯТУЛ КУРСИЙ"
                         "\n\nНАМОЗДАН КЕЙИНГИ ДУОЛАР"
                         "\n\nЖАНОЗА ДУОСИ", reply_markup=qasam03_default)
    await state.set_state("onu")

@dp.message_handler(text = "⏮ Олдинги", state="onu")
async def qadamjovid(msg: types.Message, state:FSMContext):
    await msg.answer("⏮ Олдинги", reply_markup=qasam_bosqichlar)
    await state.set_state("onm")

# BIRINCHI BOSQICH

@dp.message_handler(text = "Анонс", state="onb")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAEGNZhis_eUfOrKxYBczL7reW3dZ-U6DgAC1AUAAscCAUkhe7NKLK5MPikE",
                               caption="Анонс \n\nЯнги лойиҳа \n\n«Ўн кеча билан қасам»"
                                       "\n\n<a href='https://t.me/Quranuz_darslar/3'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='http://www.youtube.com/channel/UCy4oB3A8HHY9xzzXhxGd5nA?sub_confirmation=1'>Youtube каналга уланиш</a>")

@dp.message_handler(text = "Myқаддимa", state="onb")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID02I_2DpR1TJU2O1C6qbtcqt-cZzMAAISCwACSi2IS8Pvs44v-ykgIwQ",
                               caption="Муқаддима"
                                       "\n\n<a href='https://t.me/Quranuz_darslar/3'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/167'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=u8u96XuFTxk'>Youtube орқали кўриш</a>")

@dp.message_handler(text = "1-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID1WI_2EI6Qn6rN4j5bCLP0lwxu8peAAJ3BgACz4kZSUrmFmWqFVEbIwQ",
                               caption="АРАБ ҲАРФЛАРИ ВА УЛАРНИНГ ИМЛОСИ"
                                       "\n\n<a href='https://t.me/c/1160004188/3'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/168'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=u8u96XuFTxk'>Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID12I_2EZhr_A9eIwhddt2222G6aLIAAJqBQACJUEoSQPNiL5kz_1kIwQ")


@dp.message_handler(text = "2-кун", state="onb")
async def ikkinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID2WI_2EucYUQ_s-GyF-_2j_a2c8XBAAIQBwACo-UhSVIyCOnNWyrBIwQ",
                               caption="НУТҚ ТОВУШЛАРИ. АРАБ ТИЛИГА ХОС УНДОШЛАР"
                                       "\n\n<a href='https://t.me/c/1160004188/97'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/169'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=vCW_vqwuxkM'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID22I_2E7nqvjmuFRbMXUXbqtyCZkfAAIjBwACJUEwScoFcJmJWRQ-IwQ")

@dp.message_handler(text = "3-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID3WI_2FNSOK8E3JY4OaHiXQ_orT4yAAIlBgACU_4pSX36A7waBgwXIwQ",
                               caption="НУТҚ ТОВУШЛАРИ. АРАБ ВА ЎЗБЕК ТИЛИДА МУШТАРАК БЎЛГАН НУТҚ ТОВУШЛАРИ"
                                       "\n\n<a href='https://t.me/c/1160004188/112'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/170'> HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=OgfFcI7aBgA'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID32I_2Fa5qONF1sQP_seeIoOOpTxgAAI2BQACD_pASeZsKTrtGJlCIwQ")

@dp.message_handler(text = "4-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID4WI_2Ft0tYOkyreZmoC5yuMHYLorAAIfBwAC0-Q4SZf00zRv55mmIwQ",
                               caption="УНЛИЛАР ВА ЙЎҒОН УНДОШЛАР"
                                       "\n\n<a href='https://t.me/c/1160004188/127'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/171'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=42btpgfSQio'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID42I_2F94HKKEPd37aPb8pi5X_4KWAAJSBgACeGZZSa1yZItBGvVAIwQ")

@dp.message_handler(text = "Вазифаларни бажариш бўйича тавсиялар", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID6WI_2G0gqcozKyiw9tWlaeqwQDAxAAKLBgACo-UxSWbujW4NBi6QIwQ",
                               caption="Вазифаларни бажариш бўйича тавсиялар"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"                                       
                                       "\n\n<a href='https://www.youtube.com/watch?v=SIWQyRWpSrw&list=PLE0uv2eFBCH0uCLc_DmBLlLt8kurNBs-q&index=11&ab_channel=Quranuz'> Youtube орқали кўриш</a>")



@dp.message_handler(text = "5-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID5WI_2GSzYK_Xc93geF807D-hIZw-AAKOBwAC0-RASffhll89TVx0IwQ",
                               caption="ТАШДИД ВА ТАНВИН"
                                       "\n\n<a href='https://t.me/c/1160004188/151'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/172'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=NuUNbPajkaY'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID52I_2GjEOrQP3BM5FS10dvcHf3vxAAIqBwACFhRwSfIJH30iM2ONIwQ")

@dp.message_handler(text = "6-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID62I_2HLY-4jdu7hvzszPtZezS9rlAAIPBwAC0-RISXVGikGaNz1cIwQ",
                               caption="ТЎГАРАК ТĀ ҲАМДА АЛФИЙЯ ВĀВ ВА АЛФИЙЯ ЙĀ"
                                       "\n\n<a href='https://t.me/c/1160004188/192'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/173'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=QTs0S5cc5ng'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID7WI_2HUsrvj8tQRzNmldUWyRyaYIAAKZBQACjieQSV47KZ_Ya7nxIwQ")

@dp.message_handler(text = "7-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID72I_2Hqokx2H-KQ6CnodNgZ2Ps16AALnCAAChb9ZSS_6jVKMdmBwIwQ",
                               caption="1. ВАҚФ, ИБТИДО ВА ВАСЛ \n2. АЙИРУВЧИ ҲАМЗА ВА БОҒЛОВЧИ ҲАМЗА"
                                       "\n\n<a href='https://t.me/c/1160004188/218'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/175'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=o-Ammk1zvMQ'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID8WI_2H0Hi60DbOAt90lJzkARnEYZAAIEBwACyMCwSb42NHrS9wSvIwQ")

@dp.message_handler(text = "8-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID82I_2IE8bnzNe_gyi_Uc95NureQ4AAJPBwACPGxZSbZcrPGIFyHQIwQ",
                               caption="1. МАД \n2. ТАФХИМ ВА ТАРҚИҚ \n3. ЛАФЗИ ЖАЛОЛА"
                                       "\n\n<a href='https://t.me/c/1160004188/253'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/176'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=n4PE1ykC-2s'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID9WI_2ISuN0hLXVRAiZ5osdHKXiZQAAINBwACyMCwSU7IAnXaD89GIwQ")

@dp.message_handler(text = "9-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID92I_2InwF4ZZUp5VaIFeENrzab7qAAJ_BwACZ8GISRTCYs44a3PYIwQ",
                               caption="ЁЗИЛСА-ДА, ЎҚИЛМАЙДИГАН ҲАРФЛАР"
                                       "\n\n<a href='https://t.me/c/1160004188/293'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/177'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=uBc08OyFdyg'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID-WI_2Ixwqp9zxqIHCFObSKi7nVYwAAKGBgACQL24SXnzMplXertZIwQ")

@dp.message_handler(text = "10-кун", state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID-2I_2JGz_l7DNMh_yD0PxRTSrppwAAI9CAACV3bJSWNlkJpab5HnIwQ",
                               caption="1. ВАҚФ \n2. МУСҲАФДА СУКУН ВА ТАНВИН ИФОДАСИ"
                                       "\n\n<a href='https://t.me/c/1160004188/326'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/178'>HD форматда кўриш</a>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=rHZE-lCXBWg'> Youtube орқали кўриш</a>")
    await message.answer_document(document="BQACAgIAAxkBAAID_WI_2JQjlyuunTlshgPt-UiarUs3AALXCAAC72CZScdF6D-Ocr9DIwQ")

@dp.message_handler(text = '"Ўн кечага қасам" дастури ва Қуръон ёдлаш борасида берилган саволларга жавоблар', state="onb")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAID_2I_2JoFpluAPPcelN-jr13-f3B3AAJFGQACrVzJSOVQjQP77qSFIwQ",
                               caption="\"Ўн кечага қасам\" дастури ва Қуръон ёдлаш борасида берилган саволларга жавоблар"                                       
                                       "\n\n<a href='https://www.youtube.com/watch?v=t5rgyMT7U4M&list=PLE0uv2eFBCH0uCLc_DmBLlLt8kurNBs-q&index=12&ab_channel=Quranuz'> Youtube орқали кўриш</a>")

# IKKINCHI BOSQICH

@dp.message_handler(text = "Aнонс", state="oni")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAEGNoNis_1TOoqc8YcM2XPiytbvNzHY6wACNAUAArUN4Ekc4WD-V1NmSikE",
                               caption="Анонс.\n\nИккинчи босқич.\n\n«Ўн кеча билан қасам» туркум дарслари давом этади."
                                       "\n\n<a href='https://t.me/Quranuz_darslar/3'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='http://www.youtube.com/channel/UCy4oB3A8HHY9xzzXhxGd5nA?sub_confirmation=1'>Youtube каналга уланиш</a>")

@dp.message_handler(text = "Мyқаддима", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEA2I_2kU93syzUORB0jErgfcUWa3QAAJKBQACtQ3gSeT92D1FsraQIwQ",
                               caption="ҚУРЪОНИ КАРИМ ТИЛОВАТИГА МАРҲАБО!"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/179'>HD</a> | "
                                       "<a href='https://youtu.be/QBo8ezSxXWM'>Youtube</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/posts/3229163563760842'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEBGI_2kVDeA0zUxzyH1_CHZu3icvqAALcBQACgwAB6EnvkU3N-GReoCME")

@dp.message_handler(text = "1-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEB2I_2k-YNEBxoWN7QYU5RooSWKa5AALbBQACgwAB6EkYv1XnvIucSCME",
                               caption="ФОТИҲА СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/180'>HD</a> | "
                                       "<a href='https://youtu.be/IoVIn8CULqY'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIECGI_2k-68-F47u3nULMCrDuFbIpxAALdBQACgwAB6EkVzkTFexR7OCME")

@dp.message_handler(text = "2-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEC2I_2lZTv07bCj2n0MdqNupuFecRAALRBgACgwAB8ElS6s2uiEMJSiME",
                               caption="АН-НАС СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/181'>HD</a> | "
                                       "<a href='https://youtu.be/NE3BhmlykNc'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEDGI_2lapE6ui0M6r1KwHk9sfWuKQAALSBgACgwAB8ElD6bQedX_V7yME")

@dp.message_handler(text = "3-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIED2I_2lzz1xDr_cmonvtJH0N_mjWpAAKfBQACHXj5SUuwXW24me7uIwQ",
                               caption="ФАЛАҚ СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/182'>HD</a> | "
                                       "<a href='https://youtu.be/xxdatsbhBxU'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEEGI_2lx6oD-lvYXxgj19UN8kxOSwAAKhBQACHXj5SV-OO0tITybRIwQ")

@dp.message_handler(text = "4-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEE2I_2mObsVu-F5_AC5oEGkSTk73uAAKvBwACHXgBStDKbzzZhSWEIwQ",
                               caption="ИХЛОС СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/183'>HD</a> | "
                                       "<a href='https://youtu.be/JAi4sBlzMBA'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEFGI_2mNSCpzmOnp9VMtVS36-ehl5AAKwBwACHXgBSkuDzYndIS4oIwQ")

@dp.message_handler(text = "5-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEF2I_2msK-oR2wM1Sw7vUJOhCEkwfAAJcBQAC2FoQSsLd1U9_U4vuIwQ",
                               caption="МАСАД СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/184'>HD</a> | "
                                       "<a href='https://youtu.be/xmp0aRY9lHM'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEGGI_2mv5pdp5Uks5yJZ0tO9zJYbRAAJdBQAC2FoQSt8DNZ32Q6jjIwQ")

@dp.message_handler(text = "6-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEG2I_2nFY7E-AAAG_Z2ZoV544CQbo7QACxwUAAk7qIEqx4QOqUlAMZCME",
                               caption="НАСР СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/185'>HD</a> | "
                                       "<a href='https://youtu.be/KhvqooMzvDw'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEHGI_2nGKkIujvgTG0Wxl8NcWQWYtAALIBQACTuogSpCOErpHbBysIwQ")

@dp.message_handler(text = "7-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEH2I_2npyEeEqXFbzkzZxIfwOg0oNAAJFCAACz5owSvkkc5Nr_m5YIwQ",
                               caption="КОФИРУН СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/186'>HD</a> | "
                                       "<a href='https://youtu.be/m4S-U2VQapw'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEIGI_2npBOlqOk5FHEZYBtiXT-zQ5AAJGCAACz5owStg46z5ez9pAIwQ")

@dp.message_handler(text = "8-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEI2I_2oO-cP7xhxmVHRJKTtv-RDl_AAIBBgACxcJBSqFS_3qRiJK7IwQ",
                               caption="КАВСАР СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/187'>HD</a> | "
                                       "<a href='https://youtu.be/DZ6UmJbTySk'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEJGI_2oPkam0EfGzo6OdpWrcq8sG3AAICBgACxcJBSsP2OeXotMP3IwQ")

@dp.message_handler(text = "9-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEJ2I_2o0EaIkQ5aPjC4ykMAZmh2EaAAJsBgACxcJJSqLLwetpW6kaIwQ",
                               caption="МОЪУН СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/188'>HD</a> | "
                                       "<a href='https://youtu.be/gQnLiecFG-g'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEKGI_2o31FOOEl746rchcbkRfYsRJAAJtBgACxcJJSmlLlHV7cz03IwQ")

@dp.message_handler(text = "10-кyн", state="oni")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEK2I_2pO637k_wtss_TTJ6hVOnblEAAK8BQACIipZSjVwFDjIgsw3IwQ",
                               caption="ҚУРАЙШ СУРАСИ"
                                       "\n\n<a href='https://t.me/joinchat/AAAAAEUkQlyhuHM27IonOg'>Вазифаларни бажариш канали</a>"
                                       "\n\n<a href='https://t.me/quranuz_media/189'>HD</a> | "
                                       "<a href='https://www.youtube.com/watch?v=nvcEMdTA5g4'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz/'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIELGI_2pNCIGXT4FMfxJZPKDo_7HNBAAK9BQACIipZSj-32TdHCXtiIwQ")

# UCHINCHI BOSQICH

@dp.message_handler(text = "Мyқаддимa", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEL2I_3DJzDIVfqfJed8_m4LQEs0SVAAIkCAACqhCBSEZuYxw4dz_nIwQ",
                               caption="МУҚАДДИМА"
                                       "\n\n<a href='https://t.me/quranuz_media/237'>HD</a> | "
                                       "<a href='https://www.youtube.com/watch?v=bW5_d8f7zmE&list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO&index=2&ab_channel=Quranuz'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")

@dp.message_handler(text = "1 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEMWI_3Dnr9IRU-Kzch7DrBU8ysnQfAALjCAACqhCBSBDJT9fkzCx0IwQ",
                               caption="АЗОН ВА ИҚОМА"
                                       "\n\n<a href='https://t.me/quranuz_media/238'>HD</a> | "
                                       "<a href='https://www.youtube.com/watch?v=vjBHxpKRnD4&list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO&index=3&ab_channel=Quranuz'>"
                                       "Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEMmI_3Dma8JTgAg69Sri3d7dAJ2AjAAJRDQACb-WASI-3SXPQdAG3IwQ")

@dp.message_handler(text = "2 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIENWI_3ECwLGqq2UI2EErejwGUVdoBAAJRBwAC3deZSHjhnTo8tZxKIwQ",
                               caption="ИНТИҚОЛ - ЎТИШ ЗИКРЛАРИ"
                                       "\n\n<a href='https://t.me/quranuz_media/239'>HD</a> | "
                                       "<a href='https://www.youtube.com/watch?v=aiMBIN0fszI&list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO&index=4'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIENmI_3EDGG-mkzcKdEIJ9rx_r0QYVAAJSDQACb-WASIof14pct8J2IwQ")

@dp.message_handler(text = "3 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEOWI_3EjtyOaY_IULx8BHI1i5YhNdAAIkCQACJZuZSNLhU40kceHMIwQ",
                               caption="НАМОЗ АМАЛЛАРИДАГИ ЗИКРЛАР \n\nСАНО ВА ТАСБЕҲЛАР"
                                       "\n\n<a href='https://t.me/quranuz_media/240'>HD</a> | "
                                       "<a href='https://www.youtube.com/watch?v=NWUL6TFmFWU"
                                       "&list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO&index=5&ab_channel=Quranuz'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEOmI_3EgD0ofrwAbKE-SkYFQxjuB_AAJVDQACb-WASJOoHtXj6jkLIwQ")

@dp.message_handler(text = "4 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEPWI_3E-XBaujPnW44WLgRzlAWCW8AAIXCQACJZuhSJ0pFkKkelCNIwQ",
                               caption="НАМОЗ АМАЛЛАРИДАГИ ЗИКРЛАР \n(қаъдада ўқиладиган зикрлар)"
                                       "\n\n<a href='https://t.me/quranuz_media/241'>HD</a> | "
                                       "<a href='https://www.youtube.com/watch?v=kHJoWdar_S"
                                       "A&list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO&index=6'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEPmI_3E8LKRrV4a_kU4FkFVUOSFBVAAJWDQACb-WASGDlsYqbUAzRIwQ")

@dp.message_handler(text = "5 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEQWI_3FZBsMS87QP0QjcFHUK2NMIGAALACgACm_OxSLRtF1QxG8FJIwQ",
                               caption="НАМОЗ АМАЛЛАРИДАГИ ЗИКРЛАР \n(қаъдада ўқиладиган дуолар)"
                                       "\n\n<a href='https://t.me/quranuz_media/242'>HD</a> | "
                                       "<a href='https://youtu.be/-uKSHXynu5g?list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEQmI_3FbnznsNn24k2_dGvpVMBTHlAAJYDQACb-WASJjFBvqdBx5NIwQ")

@dp.message_handler(text = "6 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIERWI_3F1BiAOzt7bYBecZUNEN5GOIAAKwCQACjdLASIf0-FWt9hi2IwQ",
                               caption="ҚУНУТ ДУОСИ"
                                       "\n\n<a href='https://t.me/quranuz_media/243'>HD</a> | "
                                       "<a href='https://youtu.be/XIax97b7SuU?list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIERmI_3F2itBumsxTN-gifd1DfC-fnAAJaDQACb-WASIpXBkZ0DmTXIwQ")

@dp.message_handler(text = "7 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIESWI_3GTSLvbChBFNTbvJUB4ybWXJAAKiBgACjdLISKChp8CWcZdfIwQ",
                               caption="НАМОЗДАН КЕЙИНГИ ЗИКРЛАР"
                                       "\n\n<a href='https://t.me/quranuz_media/244'>HD</a> | "
                                       "<a href='https://youtu.be/s2pCGDtZwT8?list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIESmI_3GRQwepElR8uvvuiF0U65_H5AAJbDQACb-WASAaSM3kXI2ydIwQ")

@dp.message_handler(text = "8 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIETWI_3GwaqmEQr58CpLd8nDt-Gn6kAAIGCQAC7wfRSE7vnf2glBehIwQ",
                               caption="ОЯТУЛ КУРСИЙ"
                                       "\n\n<a href='https://t.me/quranuz_media/245'>HD</a> | "
                                       "<a href='https://youtu.be/zenZJaO-RJ4?list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIETmI_3GyWGE3CQBzdvucAAVJI3xstNQACXA0AAm_lgEjeW7flwws7-yME")

@dp.message_handler(text = "9 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEVWI_3JrbWLG5FXZK3bUX4LBjeE5RAAJFCQACoLbhSEr-YwJHIEUAASME",
                               caption="НАМОЗДАН КЕЙИНГИ ДУОЛАР"
                                       "\n\n<a href='https://t.me/quranuz_media/246'>HD</a> | "
                                       "<a href='https://youtu.be/JZ4VUSE6G9c?list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEVmI_3JpE5B5H1xMiuZfoXX_1TuPUAAJdDQACb-WASN5ww-gyHDdwIwQ")

@dp.message_handler(text = "10 - кун", state="onu")
async def birinchi_kun(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIEWWI_3KBklVmBBwHGcSGnNQkK23ZsAAJQCQACFbfpSCASxKsZQvN9IwQ",
                               caption="ЖАНОЗА ДУОСИ"
                                       "\n\n<a href='https://t.me/quranuz_media/247'>HD</a> | "
                                       "<a href='https://youtu.be/PRrR9buUF5g?list=PLE0uv2eFBCH3EFeemSfmsILFTTLD11xiO'>Youtube</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/'>Instagram</a> | "
                                       "<a href='https://www.facebook.com/www.quran.uz'>Facebook</a>")
    await message.answer_document(document="BQACAgIAAxkBAAIEWmI_3KAt-XYEsakSl3Sv4Lem-oI1AAJeDQACb-WASAv2qkjZbHxVIwQ")


