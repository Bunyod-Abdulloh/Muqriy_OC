
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from keyboards.default.ilmiysuhbatlar_dk import allk, is1_dk
from keyboards.inline.ilmiy_suhbatlar_harxil import toshshahar_suhbat_audio, toshshahar_suhbat_video, ilm_suhbat_inkeys
from states.ilmiy_suhbatlar_states import ToshShaharSuhbatlar
from loader import dp, bot

CHANNEL_ID = -1001705654629


async def toshshahar_suhbats():
    text = '1. «Минор» жомеъ масжиди аҳли билан илмий учрашув. Мазҳаб ва мазҳабсизлик' \
           '\n\n2. «Минор» жомеъ масжиди аҳли билан савол-жавоблар' \
           '\n\n3. «Пул емас ота» жомеъ масжиди аҳли билан илмий учрашув. Оила ҳақида' \
           '\n\n4. «Фотимаи Заҳро» жомеъ масжиди аҳли билан илмий учрашув. Аёллар хақида' \
           '\n\n5. «Юнусобод» жомеъ масжиди аҳли билан илмий учрашув. Расулуллоҳ соллаллоҳу алайҳи васалламнинг васиятлари' \
           '\n\n6. «Яккасарой» жомеъ масжиди аҳли билан илмий учрашув. Ота-онага яхшилик қилиш, уларни рози қилиш фарзандлик бурчидир мавзусида' \
           '\n\n7. «Валихўжа ўғли Норхўжа» жомеъ масжиди аҳли билан илмий учрашув. Ихлос хақида' \
           '\n\n8. «Тўхтабой» жомеъ масжиди аҳли билан илмий учрашув. Насиҳат ҳадиси шарҳи' \
           '\n\n9. «Шайх Зайниддин» жомеъ масжиди аҳли билан илмий учрашув. Хабарни қабул қилиш ва шариат илмларини олишдаги асослар' \
           '\n\n10. «Нўғай қўрғон» жомеъ масжиди аҳли билан илмий учрашув. Исломда биродарлик' \
           '\n\n11. «Лаби Заҳ» жомеъ масжиди аҳли билан илмий учрашув. Аллоҳнинг риоясини қилиш' \
           '\n\n12. «Ҳазрати Умар» жомеъ масжиди аҳли билан илмий учрашув. Нафс тарбияси' \
           '\n\n13. «Чимир ота» жомеъ масжиди аҳли билан илмий учрашув. Мусулмон биродарининг хаққига ғойибона дуо қилиш' \
           '\n\n14. «Муҳаммад Носир ҳожи» жомеъ масжиди аҳли билан илмий учрашув. Оила хақида' \
           '\n\n15. «Уккоша» жомеъ масжиди аҳли билан илмий учрашув. Шукр хақида' \
           '\n\n16. «Ҳазрати Алий» жомеъ масжиди аҳли билан илмий учрашув. Оила хақида' \
           '\n\n17. «Абу Ҳанифа» жомеъ масжиди аҳли билан илмий учрашув. Обид бўлиш хақидаги ҳадис шарҳи' \
           '\n\n18. «Имом Бухорий» жомеъ масжиди аҳли билан илмий учрашув. Ростгуйлик ва ёлғон'
    return text


@dp.message_handler(state=ToshShaharSuhbatlar.one)
async def toshshahar_one(msg: Message, state: FSMContext):
    if msg.text == '🎧 Ayдиo':
        await msg.answer(text=await toshshahar_suhbats(), reply_markup=await ilm_suhbat_inkeys(toshshahar_one=True))
        message = await msg.answer('Аудио', reply_markup=ReplyKeyboardRemove())
        await message.delete()
        await ToshShaharSuhbatlar.audio_one.set()
    elif msg.text == '🎬 Видео':
        await msg.answer(text=await toshshahar_suhbats(), reply_markup=await ilm_suhbat_inkeys(toshshahar_one=True))
        message = await msg.answer('Видео', reply_markup=ReplyKeyboardRemove())
        await message.delete()
        await ToshShaharSuhbatlar.video_one.set()
    elif msg.text == '⏮ Олдинги':
        await msg.answer(msg.text, reply_markup=await is1_dk())
        await state.set_state("ilmsuh")


@dp.callback_query_handler(state=ToshShaharSuhbatlar.audio_one)
async def toshshahar_audio_one(call: CallbackQuery):
    try:
        await call.message.delete()
        if call.data in toshshahar_suhbat_audio.keys():
            await bot.copy_message(chat_id=call.from_user.id, from_chat_id=CHANNEL_ID,
                                   message_id=toshshahar_suhbat_audio[call.data],
                                   reply_markup=await ilm_suhbat_inkeys(back=True))
            await ToshShaharSuhbatlar.audio_two.set()
        elif call.data == 'back_tash_suh2':
            await call.message.answer('⬅ Ортга', reply_markup=allk)
            await ToshShaharSuhbatlar.one.set()
    except Exception:
        pass


@dp.callback_query_handler(state=ToshShaharSuhbatlar.video_one)
async def toshshahar_video_one(call: CallbackQuery):
    try:
        await call.message.delete()
        if call.data in toshshahar_suhbat_video.keys():
            await bot.copy_message(chat_id=call.from_user.id, from_chat_id=CHANNEL_ID,
                                   message_id=toshshahar_suhbat_video[call.data],
                                   reply_markup=await ilm_suhbat_inkeys(back=True))
            await ToshShaharSuhbatlar.video_two.set()
        elif call.data == 'back_tash_suh2':
            await call.message.answer('⬅ Ортга', reply_markup=allk)
            await ToshShaharSuhbatlar.one.set()
    except Exception:
        pass


@dp.callback_query_handler(state=ToshShaharSuhbatlar.audio_two)
async def toshshahar_audio_two(call: CallbackQuery):
    try:
        await call.message.delete()
        if call.data == 'back_tash_suh1':
            await call.message.answer(text=await toshshahar_suhbats(), reply_markup=await ilm_suhbat_inkeys(toshshahar_one=True))
            await ToshShaharSuhbatlar.audio_one.set()
    except Exception:
        pass


@dp.callback_query_handler(state=ToshShaharSuhbatlar.video_two)
async def toshshahar_video_two(call: CallbackQuery):
    try:
        await call.message.delete()
        if call.data == 'back_tash_suh1':
            await call.message.answer(text=await toshshahar_suhbats(), reply_markup=await ilm_suhbat_inkeys(toshshahar_one=True))
            await ToshShaharSuhbatlar.video_one.set()
    except Exception:
        pass
