from keyboards.default.audio_video_dk import alldk
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot
from states.taroveh_states import TarovehTitle, TarovehAudio, TarovehVideo

MUQRIY_ID = -1001705654629

audio_dict = {'1 - 5': [2040, 2052, 2053, 2055, 2056], '6 - 10': [2057, 2058, 2059, 2060, 2061],
              '11 - 15': [2062, 2063, 2064, 2065, 2066], '16 - 20': [2067, 2068, 2069, 2070, 2071],
              '21 - 25': [2072, 2073, 2074, 2075, 2076], '26 - 27': [2077, 2078]}

video_dict = {1: 7, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7: 13, 8: 14, 9: 15, 10: 16, 11: 17, 12: 18, 13: 19,
              14: 20, 15: 21, 16: 22, 17: 23, 18: 24, 19: 25, 20: 26, 21: 27, 22: 28, 23: 29, 24: 30, 25: 31}

markup_audio = InlineKeyboardMarkup(row_width=5)
for k, v in audio_dict.items():
    markup_audio.insert(InlineKeyboardButton(text=str(k), callback_data=str(k)))
markup_audio.add(InlineKeyboardButton(text='⬅️ Ortga', callback_data='back_audio'))

markup_back = InlineKeyboardMarkup(row_width=1)
markup_back.add(InlineKeyboardButton(text='⬅️ Ortga', callback_data='back_back'))


@dp.message_handler(text='📌 Таровеҳ намози 1444', state='*')
async def taroveh_1444_one(m: Message, state: FSMContext):
    await m.answer(m.text, reply_markup=alldk)
    await TarovehTitle.one.set()


@dp.message_handler(state=TarovehTitle.one)
async def taroveh_1444_two(m: Message):

    if m.text == '🎧 Ayдиo':
        await m.answer(m.text, reply_markup=markup_audio)
        await TarovehAudio.one.set()

    elif m.text == '🎬 Видео':
        await m.answer('Видеолар ҳали жойланмаган!')
        # for k, v in video_dict.items():
        #     markup.insert(InlineKeyboardButton(text=str(k), callback_data=str(v)))
        # markup.add(InlineKeyboardButton(text='⬅️ Ortga', callback_data='back_video'))
        # await m.answer(m.text, reply_markup=markup)
        # await TarovehVideo.one.set()


@dp.callback_query_handler(state=TarovehAudio.one)
async def taroveh_1444_aone(c: CallbackQuery, state: FSMContext):
    await c.message.delete()

    if c.data == 'back_audio':
        await c.message.answer('📌 Таровеҳ намози 1444', reply_markup=alldk)
        await state.finish()

    elif c.data in audio_dict.keys():
        for n in audio_dict[c.data]:
            await bot.copy_message(chat_id=c.from_user.id,
                                   from_chat_id=MUQRIY_ID,
                                   message_id=n,
                                   reply_markup=markup_back)
        await TarovehAudio.two.set()


@dp.callback_query_handler(state=TarovehAudio.two)
async def taroveh_atwo(c: CallbackQuery):

    if c.data == 'back_back':
        await c.message.answer('📌 Таровеҳ намози 1444', reply_markup=markup_audio)
        await TarovehAudio.one.set()
