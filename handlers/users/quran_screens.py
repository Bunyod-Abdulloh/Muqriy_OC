from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ReplyKeyboardMarkup

from keyboards.default.start_dk import main_keyboard
from loader import dp, bot

QURAN_SCREENSHOTS = -1001801981610

dict_one = {"Fotiha": 9487, "Baqara": 9488, "Oli Imron": 9489, "Niso": 9490, "Moida": 9491, "An'om": 9492, "A'rof": 9493,
            "Anfol": 9494, "Tavba": 9495, "Yunus": 9496, "Hud": 9497, "Yusuf": 9498, "Ra'd": 9499, "Ibrohim": 9500,
            "Hijr": 9501, "Nahl": 9502, "Isro": 9503, "Kahf": 9504, 'Maryam': 9505, "Toha": 9506, "Anbiyo": 9507,
            "Haj": 9508, "Mu'minun": 9509, "Nur": 9510, "Furqon": 9511,  "Shuaro": 9512, "Naml": 9513, "Qosos": 9514,
            "Ankabut": 9515, "Rum": 9516, "Luqmon": 9517, "Sajda": 9518, "Ahzob": 9519, "Saba": 9520, "Fotir": 9521,
            "Yaasiyn": 9522, "Soffaat": 9523, "Sod": 9524, "Zumar": 9525, "G'ofir": 9526, "Fussilat": 9527,
            "Shuuro": 9528, "Zuxruf": 9529, "Duxon": 9530, "Josiya": 9531, "Ahqof": 9532, "Muhammad": 9533, "Fath": 9534,
            "Hujurot": 9535, "Qof": 9536, "Zaariyaat": 9537, "Tur": 9538, "Najm": 9539, "Qamar": 9540, "Ar-Rohman": 9541,
            "Voqi'a": 9542, "Hadid": 9543, "Mujodala": 9544, "Hashr": 9545, "Mumtahana": 9546, "Soff": 9547,
            "Jumu'a": 9548, "Munofiqun": 9549, "Tag'obun": 9550, "Taloq": 9551, "Tahrim": 9552, "Mulk": 9553,
            "Qalam": 9554, "Al-Haaqqoh": 9555, "Ma'orij": 9556, "Nuh": 9557, "Jin": 9558, "Muzzammil": 9559,
            "Muddassir": 9560, "Qiyaama": 9561, "Inson": 9562, "Mursalaat": 9563, "Naba'": 9564, "Nazi'aat": 9565,
            "Abasa": 9566, "Takvir": 9567, "Infitor": 9568, "Mutoffifun": 9569, "Inshiqoq": 9570, "Buruj": 9571,
            "Toriq": 9572, "A'laa": 9573, "G'oshiya": 9574, "Fajr": 9575, "Balad": 9576, "Shams": 9577, "Layl": 9578,
            "Zuho": 9579, "Sharh": 9580, "Tiyn": 9581, "Alaq": 9582, "Qadr": 9583, "Bayyina": 9584, "Zalzala": 9585,
            "Adiyat": 9586, "Qori'a": 9587, "Takaasur": 9588, "Asr": 9589, "Humaza": 9590, "Fil": 9591, "Quraysh": 9592,
            "Maa'uun": 9593, "Kavsar": 9594, "Kaafirun": 9595, "Nasr": 9596, "Masad": 9597, "Ixlos": 9598,
            "Falaq": 9599, "Naas": 9600}

ruyxat = list(dict_one)

markup_first = list(dict_one.keys())[:57]
markup_second = list(dict_one.keys())[58:]

markup_one = InlineKeyboardMarkup(row_width=3)
for n in markup_first:
    markup_one.insert(InlineKeyboardButton(text=n, callback_data=n))
markup_one.add(InlineKeyboardButton(text='🏡 Bosh menyu', callback_data='b_menyu'))
markup_one.insert(InlineKeyboardButton(text='Keyingi ➡️', callback_data='qs_next'))

markup_two = InlineKeyboardMarkup(row_width=3)
for n in markup_second:
    markup_two.insert(InlineKeyboardButton(text=n, callback_data=n))
markup_two.add(InlineKeyboardButton(text='⬅️ Oldingi', callback_data='qs_prev'))
markup_two.insert(InlineKeyboardButton(text='🏡 Bosh menyu', callback_data='b_menyu'))

markup_back = InlineKeyboardMarkup(row_width=1)
markup_back.add(InlineKeyboardButton(text='⬅️ Ortga', callback_data='qs_back'))


@dp.message_handler(text="📖 Қуръони карим", state='*')
async def bot_start(msg: Message, state: FSMContext):
    await msg.answer('Sura nomini tanlang:', reply_markup=markup_one)
    await state.set_state('qs_one')


@dp.callback_query_handler(state='qs_one')
async def q_s_two(call: CallbackQuery, state: FSMContext):
    if call.data == "qs_next":
        await call.message.edit_text('Sura nomini tanlang:', reply_markup=markup_two)
        await state.set_state('qs_two')

    elif call.data == 'qs_back':
        await call.message.edit_text('Sura nomini tanlang:', reply_markup=markup_one)

    elif call.data == 'b_menyu':
        await call.message.delete()
        await call.message.answer('Bosh menyu', reply_markup=main_keyboard)
        await state.finish()
    else:
        if call.data in dict_one.keys():
            await call.message.delete()
            await bot.copy_message(chat_id=call.from_user.id,
                                   from_chat_id=QURAN_SCREENSHOTS,
                                   message_id=dict_one[call.data],
                                   reply_markup=markup_back)


@dp.callback_query_handler(state='qs_two')
async def q_s_four(call: CallbackQuery, state: FSMContext):
    if call.data == 'qs_prev':
        await call.message.edit_text('Sura nomini tanlang:', reply_markup=markup_one)
        await state.set_state('qs_one')

    elif call.data == 'qs_back':
        await call.message.edit_text('Sura nomini tanlang:', reply_markup=markup_two)

    elif call.data == 'b_menyu':
        await call.message.delete()
        await call.message.answer('Bosh menyu', reply_markup=main_keyboard)
        await state.finish()

    else:
        if call.data in dict_one.keys():
            await call.message.delete()
            await bot.copy_message(chat_id=call.from_user.id,
                                   from_chat_id=QURAN_SCREENSHOTS,
                                   message_id=dict_one[call.data],
                                   reply_markup=markup_back)
