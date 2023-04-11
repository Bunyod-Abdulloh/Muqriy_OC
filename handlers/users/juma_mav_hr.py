from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.default.juma_mav_dk import juma_abutton, juma_dicta
from keyboards.default.audio_video_dk import alldk

from loader import dp, bot

JUMA_FIRST = -1001739337616
JUMA_SECOND = -1001847685422

@dp.message_handler(text="📌 Жума мавъизалари", state="*") #
async def vvvf(msg: Message, state:FSMContext):
    await bot.copy_message(chat_id=msg.from_user.id,
                           from_chat_id=JUMA_SECOND,
                           message_id=27,
                           reply_markup=alldk)
    await state.set_state("juma_buttons")

@dp.message_handler(state = "juma_buttons")
async def sample_func(msg: Message, state:FSMContext):
    if msg.text == "🎧 Ayдиo":
        await msg.answer(msg.text,
                         reply_markup=juma_abutton)
        await state.set_state("juma_audio")
    elif msg.text == "🎬 Видео":
        await msg.answer(msg.text,
                         reply_markup=juma_abutton)
        await state.set_state("juma_video")
    else:
        await msg.answer("Қуйидаги тугмалардан бирини киритинг:")

@dp.message_handler(state="juma_video")
async def juma_audio_func(msg: Message, state:FSMContext):
    if msg.text in juma_dicta.keys():
        for n in juma_dicta[msg.text]['v']:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=JUMA_FIRST,
                                   message_id=n)
    elif msg.text == "⏮ Олдинги":
        await msg.answer(msg.text,
                         reply_markup=alldk)
        await state.set_state("juma_buttons")

@dp.message_handler(state="juma_audio")
async def abastate(msg: Message, state:FSMContext):
    if msg.text in juma_dicta.keys():
        for n in juma_dicta[msg.text]['a']:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=JUMA_SECOND,
                                   message_id=n)
    elif msg.text == "⏮ Олдинги":
        await msg.answer(msg.text,
                         reply_markup=alldk)
        await state.set_state("juma_buttons")