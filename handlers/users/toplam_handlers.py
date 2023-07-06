from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from handlers.users.ilmiysuhbatlar_hr import CHANNEL_ID
from keyboards.default.ilmiysuhbatlar_dk import is1_dk, allk
from keyboards.inline.ilmiy_suhbatlar_harxil import tort_suhbat_video, tort_suhbat_audio, ilm_suhbat_inkeys
from states.toplam_states import TortToplam

from loader import dp, bot


async def tort_suhbatlar():
    text = '1. "Компас - лидерлар академияси"да "Оилавий муносабатлар" мавзусида ташкил этилган суҳбат' \
           '\n\n2. «Китобхонлик мактаби» лойиҳасининг махсус сони чақирув хатмонаси' \
           '\n\n3. Радикал атеистлар, феминизм, терроризм, гендер тенглиги ва жоҳил мусулмонлар.' \
           '\n\n4. Исломда ҳамжиҳатлик тинчлик гарови.' \
           '\n\n5. "Муносиб бека тайёрлаш ва уларни жамиятга тақдим этиш"' \
           '\n\n6. СССР тақиқлаган ибодат. Ҳасанхон Яҳё Абдулмажид ва Олимжон Ғуломов билан | "Fikrat"' \
           '\n\n7. Ислом тўғри ўрганилса, ҳамма замонга мос келади. 13 ёшида қори бўлган қори билан суҳбат.' \
           '\n\n8. Араб тили ва эски ўзбек ёзувини ўрганишнинг аҳамияти' \
           '\n\n9. Билганлар билан билмаганлар тенг бўладими? "Нажот Таълим" ўқув марказида бўлиб ўтган суҳбат' \
           '\n\n10. "Расулуллоҳ - улуғ неъмат" «Шайх Муҳаммад Содиқ Муҳаммад Юсуф» масжидида бўлиб ўтган илмий суҳбат' \
           '\n\n11. Илм олишнинг ҳаётимиздаги ўрни\n\n12. Аёл киши пул топиши керакми?' \
           '\n\n13. Устоз Ҳасанхон Яҳё Абдулмажид билан очиқ суҳбат\n\n14. Устозлар билан жонли суҳбат'
    return text


@dp.message_handler(state="tortt")
async def jonlifunc(msg: Message, state: FSMContext):
    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=await is1_dk())
        await state.set_state("ilmsuh")
    elif msg.text == "🎬 Видео":
        await msg.answer(text=await tort_suhbatlar(), reply_markup=await ilm_suhbat_inkeys(torttoplam=True))
        message = await msg.answer('Видео', reply_markup=ReplyKeyboardRemove())
        await message.delete()
        await TortToplam.video_one.set()

    elif msg.text == "🎧 Ayдиo":
        await msg.answer(text=await tort_suhbatlar(), reply_markup=await ilm_suhbat_inkeys(torttoplam=True))
        message = await msg.answer('Аудио', reply_markup=ReplyKeyboardRemove())
        await message.delete()
        await TortToplam.audio_one.set()


@dp.callback_query_handler(state=TortToplam.video_one)
async def tort_video_one(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        if call.data in tort_suhbat_video.keys():
            await bot.copy_message(chat_id=call.from_user.id, from_chat_id=CHANNEL_ID,
                                   message_id=tort_suhbat_video[call.data],
                                   reply_markup=await ilm_suhbat_inkeys(back=True))
            await TortToplam.video_two.set()
        elif call.data == 'back_tash_suh2':
            await call.message.answer('⬅ Ортга', reply_markup=allk)
            await state.set_state("tortt")
    except Exception:
        pass


@dp.callback_query_handler(state=TortToplam.video_two)
async def torttoplam_video_two(call: CallbackQuery):
    try:
        await call.message.delete()
        if call.data == 'back_tash_suh1':
            await call.message.answer(text=await tort_suhbatlar(), reply_markup=await ilm_suhbat_inkeys(
                torttoplam=True))
            await TortToplam.video_one.set()
    except Exception:
        pass


@dp.callback_query_handler(state=TortToplam.audio_one)
async def torttoplam_audio_one(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        if call.data in tort_suhbat_audio.keys():
            await bot.copy_message(chat_id=call.from_user.id, from_chat_id=CHANNEL_ID,
                                   message_id=tort_suhbat_audio[call.data],
                                   reply_markup=await ilm_suhbat_inkeys(back=True))
            await TortToplam.audio_two.set()
        elif call.data == 'back_tash_suh2':
            await call.message.answer('⬅ Ортга', reply_markup=allk)
            await state.set_state("tortt")
    except Exception:
        pass


@dp.callback_query_handler(state=TortToplam.audio_two)
async def torttoplam_audio_two(call: CallbackQuery):
    try:
        await call.message.delete()
        if call.data == 'back_tash_suh1':
            await call.message.answer(text=await tort_suhbatlar(), reply_markup=await ilm_suhbat_inkeys(torttoplam=True))
            await TortToplam.audio_one.set()
    except Exception:
        pass
