from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from keyboards.default.audio_video_dk import alldk
from states.jumasuhbatlari_states import JumaSuhbatlari
from keyboards.inline.juma_suhbatlari_inkeys import juma_suhbatlari_keys, video_dict, audio_dict, back_menyu_keys

from loader import bot, dp

VIDEO_CHANNEL = -1001739337616
AUDIO_CHANNEL = -1001847685422
list_messages = []


async def juma_title():
    text = '1. Намоз - мўминнинг меърожи\n2. Намозга оид масалалар баёни' \
           '\n3. Жаннат – оналар оёғи остида\n4. Ижтимоий иллатлар (фирибгарлик, ўзгалар молини ноҳақ ейиш)' \
           '\n5. Илмли ёшлар - юрт келажаги\n6. Азиз умрнинг қадрига етайлик' \
           '\n7. Тил офатлари\n8. Ёшларни ижтимоий иллатлардан сақлайлик!' \
           '\n9. Пайғамбаримиз алайҳиссаломнинг сўнги васиятлари' \
           '\n10. Бир ҳадис шарҳи: Киши исломининг гўзаллиги' \
           '\n11. Ўзаро меҳр - оқибатли бўлмагунингизча, комил мўмин бўлолмайсизлар' \
           '\n12. Ихлос - амаллар асоси\n13. Бир ҳадис шарҳи: ".... биздан эмас" ҳадислар туркуми' \
           '\n14. Закот - молиявий ибодат\n15. Қадр кечасининг фазилати\n16. Cилаи раҳм - қариндошлик алоқаларини яхшилаш' \
           '\n17. Фаришталар ҳам ҳаё қилган зот\n18. Суннатга амал қилиш ва бидъатнинг зарарлари' \
           '\n19. Oилавий ажримлар-жамият заволи\n20. Қиморнинг ижтимоий зарарлари' \
           '\n21. Исломда ҳамжиҳатлик - тинчлик гарови\n22. Эъзоз ва эҳтиромга муносиб зотлар' \
           '\n23. Аллоҳ ва Расулининг мухаббатига сазовор бўлган зот\n24. Аллоҳ таолога иймон келтириш ва унга оид масалалар' \
           '\n25. Ҳасад - эзгулик заволи'
    return text


@dp.message_handler(text='📌 Жума мавъизалари', state='*')
async def jumamaviza_func(msg: Message, state: FSMContext):
    await msg.answer(msg.text, reply_markup=alldk)
    await JumaSuhbatlari.juma_one.set()


@dp.message_handler(state=JumaSuhbatlari.juma_one)
async def juma_one_state(msg: Message, state: FSMContext):
    if msg.text == '🎧 Ayдиo':
        await msg.answer(text=await juma_title(), reply_markup=await juma_suhbatlari_keys(audio=True))
        await JumaSuhbatlari.juma_audio_one.set()

    elif msg.text == '🎬 Видео':
        await msg.answer(text=await juma_title(), reply_markup=await juma_suhbatlari_keys(video=True))
        await JumaSuhbatlari.juma_video_one.set()


@dp.callback_query_handler(state=JumaSuhbatlari.juma_audio_one)
async def juma_one_state(call: CallbackQuery, state: FSMContext):

    await call.message.delete()

    if call.data == 'juma_back':
        await call.message.answer('📌 Жума мавъизалари',
                                  reply_markup=alldk)
        await JumaSuhbatlari.juma_one.set()

    elif call.data in audio_dict.keys():
        for n in audio_dict[call.data]:
            msg_id = await bot.copy_message(chat_id=call.from_user.id,
                                            from_chat_id=AUDIO_CHANNEL,
                                            message_id=n,
                                            reply_markup=back_menyu_keys)
            list_messages.append(msg_id.message_id)
        await JumaSuhbatlari.juma_audio_two.set()


@dp.callback_query_handler(state=JumaSuhbatlari.juma_audio_two)
async def jumaaudio_two_state(call: CallbackQuery, state: FSMContext):

    if call.data == 'juma_back':
        for n in list_messages:
            try:
                await bot.delete_message(chat_id=call.message.chat.id,
                                         message_id=n)
            except:
                continue

        list_messages.clear()

        await call.message.answer(text=await juma_title(),
                                  reply_markup=await juma_suhbatlari_keys(audio=True))
        await JumaSuhbatlari.juma_audio_one.set()


@dp.callback_query_handler(state=JumaSuhbatlari.juma_video_one)
async def juma_one_state(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == 'juma_back':
        await call.message.answer('📌 Жума мавъизалари', reply_markup=alldk)
        await JumaSuhbatlari.juma_one.set()

    elif int(call.data) in video_dict.keys():
        msg_id = await bot.copy_message(chat_id=call.from_user.id,
                                        message_id=video_dict[int(call.data)],
                                        from_chat_id=VIDEO_CHANNEL,
                                        reply_markup=back_menyu_keys)
        list_messages.append(msg_id.message_id)
        await JumaSuhbatlari.juma_video_two.set()


@dp.callback_query_handler(state=JumaSuhbatlari.juma_video_two)
async def jumavideo_one_func(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    if call.data == 'juma_back':
        for n in list_messages:
            try:
                await bot.delete_message(chat_id=call.message.chat.id,
                                         message_id=n)
            except:
                continue

        list_messages.clear()

        await call.message.answer(text=await juma_title(),
                                  reply_markup=await juma_suhbatlari_keys(video=True))
        await JumaSuhbatlari.juma_video_one.set()

    elif call.data == 'bosh_menyu':
        await state.finish()
        pass
