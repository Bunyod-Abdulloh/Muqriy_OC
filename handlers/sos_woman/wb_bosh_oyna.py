import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from filters import IsGroup
from handlers.sos_all.admin_functions import admin_answer_func
from handlers.sos_woman.wz_buttons import wbutton_one
from handlers.sos_man.mz_functions import all_send_man, bot_answer_content_type
from handlers.sos_woman.wz_functions import w_check_delete
from keyboards.inline.sos_inline_keyboards import answer_questions_two
from loader import sdb, dp
from states.sos_states import WomanAdmin

wuser_id = {}
wb_one = {}
wb_two = {}


class CommandWoMan(Command):

    def __init__(self):
        super().__init__(['woman_questions'])


@dp.message_handler(IsGroup(), CommandWoMan(), state='*')
async def questions_command_func(msg: Message):
    admins = await sdb.all_admins()
    for n in admins:
        if n[1] == int(msg.from_user.id):
            try:
                all_users_db = await sdb.select_all_woman()
                if len(all_users_db) == 0:
                    await msg.answer('Базада саволлар мавжуд эмас!')
                else:
                    await msg.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
                await msg.delete()
                await WomanAdmin.SOS_one.set()
            except Exception as err:
                logging.info(err)


@dp.callback_query_handler(state=WomanAdmin.SOS_one)
async def group_ans_two(call: CallbackQuery):
    user_id = int(call.data)
    audio_db = await sdb.select_woman_audio(user_id=user_id, turi='audio')
    document_db = await sdb.select_woman_document(user_id=user_id, turi='document')
    photo_db = await sdb.select_woman_photo(user_id=user_id, turi='photo')
    text_db = await sdb.select_woman_text(user_id=user_id, turi='text')
    video_db = await sdb.select_woman_video(user_id=user_id, turi='video')
    voice_db = await sdb.select_woman_voice(user_id=user_id, turi='voice')
    wuser_id['user_id'] = user_id

    try:
        await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db, document_db=document_db,
                           photo_db=photo_db, text_db=text_db, video_db=video_db, voice_db=voice_db)
    except Exception as err:
        logging.info(err)
    await WomanAdmin.SOS_two.set()


@dp.callback_query_handler(state=WomanAdmin.SOS_two)
async def group_ans_three(call: CallbackQuery, state: FSMContext):
    bot_db = await sdb.select_bot_answer(gender='woman')
    user_id = wuser_id['user_id']
    audio_db = await sdb.select_woman_audio(user_id=user_id, turi='audio')
    document_db = await sdb.select_woman_document(user_id=user_id, turi='document')
    photo_db = await sdb.select_woman_photo(user_id=user_id, turi='photo')
    text_db = await sdb.select_woman_text(user_id=user_id, turi='text')
    video_db = await sdb.select_woman_video(user_id=user_id, turi='video')
    voice_db = await sdb.select_woman_voice(user_id=user_id, turi='voice')
    try:
        if call.data == 'bot_answer':
            if len(bot_db) == 0:
                await call.message.answer('Жавоб киритилмаган! Бот жавобини киритинг.\n\nУшбу жавоб <b>ℹ Бот '
                                          'жавоби</b> тугмасини босганингизда фойдаланувчига боради')
                await WomanAdmin.bot_addone.set()
            else:
                bot_answer = f'\n\n<b>ℹ Бот жавоби:\n\n{bot_db[0][1]}</b>'
                await bot_answer_content_type(call=call, bot_answer=bot_answer, bot_dict=wb_two)
                await WomanAdmin.bot_one.set()

        elif call.data == 'admin_answer':
            await admin_answer_func(call=call, gender_state=wb_one)
            await WomanAdmin.admin_one.set()

        elif call.data == 'delete_answer':
            if call.message.content_type == 'audio':
                await w_check_delete(answer=call.message.audio.file_unique_id, type_db=audio_db, boshqa=True)

            elif call.message.content_type == 'document':
                await w_check_delete(answer=call.message.document.file_unique_id, type_db=document_db, boshqa=True)

            elif call.message.content_type == 'photo':
                await w_check_delete(answer=call.message.photo[-1].file_unique_id, type_db=photo_db, boshqa=True)

            elif call.message.content_type == 'text':
                await w_check_delete(answer=call.message.text, type_db=text_db, text=True)

            elif call.message.content_type == 'video':
                await w_check_delete(answer=call.message.video.file_unique_id, type_db=video_db, boshqa=True)

            elif call.message.content_type == 'voice':
                await w_check_delete(answer=call.message.voice.file_unique_id, type_db=voice_db, boshqa=True)

            await call.answer(text='Савол базадан ўчирилди!', show_alert=True)

            await call.message.delete()

            all_users_db = await sdb.select_all_woman()
            user_questions = await sdb.select_all_womanuser(user_id=user_id)

            if len(user_questions) == 0:
                if len(all_users_db) == 0:
                    await call.message.answer('Базада саволлар мавжуд эмас!')
                    await state.finish()
                else:
                    await call.message.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
                    await WomanAdmin.SOS_one.set()

        elif call.data == 'back_answer_true':
            await call.message.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
            await WomanAdmin.SOS_one.set()

        elif call.data == 'back_answer_false':
            all_users_db = await sdb.select_all_woman()
            if len(all_users_db) == 0:
                await call.message.answer('Базада саволлар мавжуд эмас!')
                await state.finish()
            else:
                await call.message.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
                await WomanAdmin.SOS_one.set()
    except Exception as err:
        logging.info(err)
