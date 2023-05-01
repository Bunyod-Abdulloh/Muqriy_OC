from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.ilmiysuhbatlar_dk import allk, is1_dk, is1_dict, is2_dict, is2_dk, is3_dict
from states.ilmiy_suhbatlar_states import ToshShaharSuhbatlar
from loader import dp, bot

CHANNEL_ID = -1001705654629

habar = "Илтимос қуйидаги тугмалардан бирини танланг:"


@dp.message_handler(text="📚 Илмий суҳбатлар", state="*")
async def ilm_suh(msg: types.Message, state: FSMContext):
    await msg.answer("📚 Илмий суҳбатлар",
                     reply_markup=await is1_dk())
    await state.set_state("ilmsuh")


@dp.message_handler(state="ilmsuh")
async def ilmsuh_func(msg: types.Message, state: FSMContext):
    if msg.text in is1_dict.keys():
        if msg.text == "1-тўплам":
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=719,
                                   reply_markup=allk)
        else:
            await msg.answer(f"{msg.text}",
                             reply_markup=allk)
        if is1_dict[msg.text] == 'tosh1':
            await ToshShaharSuhbatlar.one.set()
        else:
            await state.set_state(is1_dict[msg.text])


@dp.message_handler(state="jonli")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(614, 619):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        for n in range(664, 669):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="surhon")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(626, 633):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        for n in range(657, 664):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="toshvil")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(635, 637):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        for n in range(655, 657):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="tosh2")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(696, 705):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        for n in range(687, 696):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="hajqurbonlik")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(706, 719):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        await bot.copy_message(chat_id=msg.from_user.id,
                               from_chat_id=CHANNEL_ID,
                               message_id=705)
    else:
        await msg.answer(habar)


@dp.message_handler(state="birt")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        await msg.answer(msg.text,
                         reply_markup=await is2_dk())
        await state.set_state("birtvideo")
    elif msg.text == "🎧 Ayдиo":
        await msg.answer(msg.text,
                         reply_markup=await is2_dk())
        await state.set_state("birtaudio")
    else:
        await msg.answer(habar)


@dp.message_handler(state="birtvideo")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=allk)
        await state.set_state("birt")
    elif msg.text in is2_dict.keys():
        for n in is2_dict[msg.text]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="birtaudio")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=allk)
        await state.set_state("birt")
    elif msg.text in is3_dict.keys():
        for n in is3_dict[msg.text]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="ikkit")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(830, 841):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        for n in range(824, 830):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer(habar)


@dp.message_handler(state="ucht")
async def jonlifunc(msg: types.Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        for n in range(842, 850):
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    elif msg.text == "🎧 Ayдиo":
        await bot.copy_message(chat_id=msg.from_user.id,
                               from_chat_id=CHANNEL_ID,
                               message_id=841)
    else:
        await msg.answer(habar)
