import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from handlers.sos_woman.wb_bosh_oyna import wuser_id, wb_two
from handlers.sos_woman.wz_buttons import wbutton_one
from handlers.sos_man.mz_functions import all_send_man
from keyboards.inline.sos_inline_keyboards import answer_questions_two, check_bot_answer, user_check_ikeys
from loader import sdb, bot, dp
from states.sos_states import WomanAdmin

wd_one = {}


@dp.callback_query_handler(state=WomanAdmin.bot_one)
async def adm_answer_fone(call: CallbackQuery, state: FSMContext):
    user_id = wuser_id['user_id']
    audio_db = await sdb.select_woman_audio(user_id=user_id, turi='audio')
    document_db = await sdb.select_woman_document(user_id=user_id, turi='document')
    photo_db = await sdb.select_woman_photo(user_id=user_id, turi='photo')
    text_db = await sdb.select_woman_text(user_id=user_id, turi='text')
    video_db = await sdb.select_woman_video(user_id=user_id, turi='video')
    voice_db = await sdb.select_woman_voice(user_id=user_id, turi='voice')

    if call.data == 'edit_bot_answer':
        await call.message.answer('Ушбу жавоб <b>ℹ Бот жавоби</b> тугмасини босганингизда фойдаланувчига боради.'
                                  '\nЖавоб матнини киритинг:')
        await WomanAdmin.bot_editone.set()

    elif call.data == 'send_answer':
        bot_answer = await sdb.select_bot_answer(gender='woman')
        user_question = 'Сизнинг саволингиз\n\n'

        if call.message.content_type == 'audio':
            await bot.send_audio(chat_id=user_id, audio=call.message.audio.file_id, caption=f'{user_question}'
                                                                                            f'{call.message.caption}')
            await sdb.delete_woman_unique(unique_id=call.message.audio.file_unique_id)

        elif call.message.content_type == 'document':
            await bot.send_document(chat_id=user_id, document=call.message.document.file_id,
                                    caption=f'{user_question}{call.message.caption}')
            await sdb.delete_woman_unique(unique_id=call.message.document.file_unique_id)

        elif call.message.content_type == 'photo':
            await bot.send_photo(chat_id=user_id, photo=call.message.photo[-1].file_id,
                                 caption=f'{user_question}{call.message.caption}')
            await sdb.delete_woman_unique(unique_id=call.message.photo[-1].file_unique_id)

        elif call.message.content_type == 'text':
            user_quest = wb_two['user_question']
            await bot.send_message(chat_id=user_id, text=f"{user_question}{user_quest}"
                                                         f"<b>\n\nЖавоб:</b>\n\n{bot_answer[0][1]}")
            await sdb.delete_woman_text(text=user_quest)

        elif call.message.content_type == 'video':
            await bot.send_video(chat_id=user_id, video=call.message.video.file_id,
                                 caption=f'{user_question}{call.message.caption}')
            await sdb.delete_woman_unique(unique_id=call.message.video.file_unique_id)

        elif call.message.content_type == 'voice':
            await bot.send_voice(chat_id=user_id, voice=call.message.voice.file_id,
                                 caption=f'{user_question}{call.message.caption}')
            await sdb.delete_woman_unique(unique_id=call.message.voice.file_unique_id)

        await call.answer('Жавоб юборилди ва савол базадан ўчирилди!', show_alert=True)
        user_questions = await sdb.select_all_womanuser(user_id=user_id)
        if len(user_questions) > 0:
            await call.message.answer('Фойдаланувчи саволлари бўлимига қайтасизми?', reply_markup=user_check_ikeys)
            await WomanAdmin.admin_delone.set()
        else:
            all_users_db = await sdb.select_all_woman()
            if len(all_users_db) == 0:
                await call.message.answer('Базада саволлар мавжуд эмас!')
                await state.finish()
            else:
                await call.message.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
                await WomanAdmin.SOS_one.set()

    elif call.data == 'back_bot_answer':
        await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db, document_db=document_db,
                           photo_db=photo_db, text_db=text_db, video_db=video_db, voice_db=voice_db)
        await WomanAdmin.SOS_two.set()


@dp.message_handler(state=WomanAdmin.bot_addone)
async def bat_one_func(msg: Message):
    try:
        await msg.answer('Жавоб қабул қилинди! Тасдиқлайсизми?', reply_markup=check_bot_answer)
        wd_one['add_bot_answer'] = msg.text
        await WomanAdmin.bot_two.set()
    except Exception as err:
        logging.info(err)


@dp.callback_query_handler(state=WomanAdmin.bot_two)
async def bat_two_func(call: CallbackQuery, state: FSMContext):
    user_id = wuser_id['user_id']
    audio_db = await sdb.select_woman_audio(user_id=user_id, turi='audio')
    document_db = await sdb.select_woman_document(user_id=user_id, turi='document')
    photo_db = await sdb.select_woman_photo(user_id=user_id, turi='photo')
    text_db = await sdb.select_woman_text(user_id=user_id, turi='text')
    video_db = await sdb.select_woman_video(user_id=user_id, turi='video')
    voice_db = await sdb.select_woman_voice(user_id=user_id, turi='voice')

    if call.data == 'check_bot':
        await sdb.add_bot_answer(text=wd_one['add_bot_answer'], gender='woman')
        await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db, document_db=document_db,
                           photo_db=photo_db, text_db=text_db, video_db=video_db, voice_db=voice_db)
        await WomanAdmin.SOS_two.set()

    elif call.data == 'again_bot':
        await call.message.answer('Бот жавобини қайта киритинг:')
        await WomanAdmin.bot_addone.set()
    elif call.data == 'back_check':
        await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db, document_db=document_db,
                           photo_db=photo_db, text_db=text_db, video_db=video_db, voice_db=voice_db)
        await WomanAdmin.SOS_two.set()
    wd_one.clear()


@dp.message_handler(state=WomanAdmin.bot_editone)
async def adm_answer_ftwo(msg: Message, state: FSMContext):
    try:
        await sdb.update_bot_answerwoman(text=msg.text, gender='woman')
        await msg.answer(text='Бот жавоби ўзгартирилди!')
        await msg.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
        await WomanAdmin.SOS_one.set()
    except Exception as err:
        logging.info(err)
