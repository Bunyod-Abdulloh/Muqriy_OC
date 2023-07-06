from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.sos_all.admin_functions import admin_answer_yes_voice, admin_answer_yes_text, admin_answer_yes_video, \
    admin_answer_yes_photo, admin_answer_yes_document, admin_answer_yes_audio
from handlers.sos_man.mz_functions import all_send_man
from handlers.sos_woman.wb_bosh_oyna import wb_one
from handlers.sos_woman.wb_bosh_oyna import wuser_id
from handlers.sos_woman.wz_buttons import wbutton_one
from handlers.sos_woman.wz_functions import w_check_delete
from keyboards.inline.sos_inline_keyboards import admin_yes_no, user_check_ikeys, answer_questions_two
from loader import dp, sdb
from states.sos_states import WomanAdmin

wc_one = {}


@dp.message_handler(content_types=['text', 'photo', 'video', 'audio', 'voice', 'document'],
                    state=WomanAdmin.admin_one)
async def admin_answer_one(msg: Message, state: FSMContext):
    if msg.content_type == 'text':
        wc_one['admin_answer_text'] = msg.text
    elif msg.content_type == 'photo':
        wc_one['photo_id'] = msg.photo[-1].file_id
        wc_one['photo_caption'] = msg.caption
    elif msg.content_type == 'video':
        wc_one['video_id'] = msg.video.file_id
        wc_one['video_caption'] = msg.caption
    elif msg.content_type == 'audio':
        wc_one['audio_id'] = msg.audio.file_id
        wc_one['audio_caption'] = msg.caption
    elif msg.content_type == 'voice':
        wc_one['voice_id'] = msg.voice.file_id
        wc_one['voice_caption'] = msg.caption
    elif msg.content_type == 'document':
        wc_one['document_id'] = msg.document.file_id
        wc_one['document_caption'] = msg.caption

    await msg.answer('Жавобингиз қабул қилинди! Саволни базада қолдирасизми ёки ўчирасизми?',
                     reply_markup=admin_yes_no)
    await WomanAdmin.admin_two.set()


wc_two = {}


@dp.callback_query_handler(state=WomanAdmin.admin_two)
async def admin_answer_fcheck(call: CallbackQuery, state: FSMContext):
    user_id = wuser_id['user_id']
    all_questions = await sdb.select_all_woman()
    audio_db = await sdb.select_woman_audio(user_id=user_id, turi='audio')
    document_db = await sdb.select_woman_document(user_id=user_id, turi='document')
    photo_db = await sdb.select_woman_photo(user_id=user_id, turi='photo')
    text_db = await sdb.select_woman_text(user_id=user_id, turi='text')
    video_db = await sdb.select_woman_video(user_id=user_id, turi='video')
    voice_db = await sdb.select_woman_voice(user_id=user_id, turi='voice')

    if call.data == 'admin_yes':
        for n in wc_one.keys():
            if n == 'admin_answer_text':
                await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[n], user_savoli=wb_one)
                await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db,
                                   document_db=document_db, photo_db=photo_db, text_db=text_db, video_db=video_db,
                                   voice_db=voice_db)

            elif n == 'audio_id':
                await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db,
                                   document_db=document_db, photo_db=photo_db, text_db=text_db, video_db=video_db,
                                   voice_db=voice_db)

            elif n == 'document_id':
                await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db,
                                   document_db=document_db, photo_db=photo_db, text_db=text_db, video_db=video_db,
                                   voice_db=voice_db)

            elif n == 'photo_id':
                await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db,
                                   document_db=document_db, photo_db=photo_db, text_db=text_db, video_db=video_db,
                                   voice_db=voice_db)

            elif n == 'video_id':
                await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db,
                                   document_db=document_db, photo_db=photo_db, text_db=text_db, video_db=video_db,
                                   voice_db=voice_db)

            elif n == 'voice_id':
                await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db,
                                   document_db=document_db, photo_db=photo_db, text_db=text_db, video_db=video_db,
                                   voice_db=voice_db)
        wc_one.clear()
        wb_one.clear()
        await WomanAdmin.SOS_two.set()

    elif call.data == 'admin_check_delete':
        for n in wb_one.keys():
            if n == 'audio_admin_unique':
                for i in wc_one.keys():
                    if i == 'audio_id':
                        await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'document_id':
                        await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'photo_id':
                        await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'admin_answer_text':
                        await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[i], user_savoli=wb_one)

                    elif i == 'video_id':
                        await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'voice_id':
                        await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await w_check_delete(answer=wb_one['audio_admin_unique'], type_db=audio_db, boshqa=True)

            elif n == 'document_admin_unique':
                for i in wc_one.keys():
                    if i == 'audio_id':
                        await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'document_id':
                        await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one,
                                                        user_savoli=wb_one)
                    elif i == 'photo_id':
                        await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'admin_answer_text':
                        await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[i],
                                                    user_savoli=wb_one)
                    elif i == 'video_id':
                        await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'voice_id':
                        await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                await w_check_delete(answer=wb_one['document_admin_unique'], type_db=document_db,
                                     boshqa=True)

            elif n == 'photo_admin_unique':
                for i in wc_one.keys():
                    if i == 'audio_id':
                        await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'document_id':
                        await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one,
                                                        user_savoli=wb_one)
                    elif i == 'photo_id':
                        await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'admin_answer_text':
                        await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[i],
                                                    user_savoli=wb_one)
                    elif i == 'video_id':
                        await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'voice_id':
                        await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                await w_check_delete(answer=wb_one['photo_admin_unique'], type_db=document_db, boshqa=True)

            elif n == 'text_adm_ans':
                for i in wc_one.keys():
                    if i == 'audio_id':
                        await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'document_id':
                        await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one,
                                                        user_savoli=wb_one)
                    elif i == 'photo_id':
                        await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one,
                                                     user_savoli=wb_one)
                    elif i == 'admin_answer_text':
                        await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[i],
                                                    user_savoli=wb_one)

                    elif i == 'video_id':
                        await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'voice_id':
                        await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                await w_check_delete(answer=wb_one['text_adm_ans'], type_db=text_db, text=True)

            elif n == 'video_admin_unique':
                for i in wc_one.keys():
                    if i == 'audio_id':
                        await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'document_id':
                        await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'photo_id':
                        await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'admin_answer_text':
                        await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[i], user_savoli=wb_one)

                    elif i == 'video_id':
                        await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'voice_id':
                        await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                await w_check_delete(answer=wb_one['video_admin_unique'], type_db=video_db, boshqa=True)

            elif n == 'voice_admin_unique':
                for i in wc_one.keys():
                    if i == 'audio_id':
                        await admin_answer_yes_audio(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'document_id':
                        await admin_answer_yes_document(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'photo_id':
                        await admin_answer_yes_photo(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'admin_answer_text':
                        await admin_answer_yes_text(user_id=user_id, admin_javobi=wc_one[i], user_savoli=wb_one)

                    elif i == 'video_id':
                        await admin_answer_yes_video(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)

                    elif i == 'voice_id':
                        await admin_answer_yes_voice(user_id=user_id, admin_javobi=wc_one, user_savoli=wb_one)
                await w_check_delete(answer=wb_one['voice_admin_unique'], type_db=voice_db, boshqa=True)

        if len(all_questions) == 1:
            await call.message.answer('Базада саволлар мавжуд эмас!')
            await state.finish()
        else:
            user_questions = await sdb.select_all_womanuser(user_id=user_id)
            if len(user_questions) > 0:
                await call.message.answer('Фойдаланувчи саволлари бўлимига қайтасизми?',
                                          reply_markup=user_check_ikeys)
                await WomanAdmin.admin_delone.set()
            else:
                await call.message.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
                await WomanAdmin.SOS_one.set()
        wc_two.clear()
        wc_one.clear()
        wb_one.clear()

    elif call.data == 'admin_no_again':
        await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db, document_db=document_db,
                           photo_db=photo_db, text_db=text_db, video_db=video_db, voice_db=voice_db)
        await WomanAdmin.SOS_two.set()


@dp.callback_query_handler(state=WomanAdmin.admin_delone)
async def admin_check_delete_one(call: CallbackQuery):
    user_id = wuser_id['user_id']
    audio_db = await sdb.select_woman_audio(user_id=user_id, turi='audio')
    document_db = await sdb.select_woman_document(user_id=user_id, turi='document')
    photo_db = await sdb.select_woman_photo(user_id=user_id, turi='photo')
    text_db = await sdb.select_woman_text(user_id=user_id, turi='text')
    video_db = await sdb.select_woman_video(user_id=user_id, turi='video')
    voice_db = await sdb.select_woman_voice(user_id=user_id, turi='voice')

    if call.data == 'user_check_yes':
        await all_send_man(call=call, markup=await answer_questions_two(), audio_db=audio_db, document_db=document_db,
                           photo_db=photo_db, text_db=text_db, video_db=video_db, voice_db=voice_db)
        await WomanAdmin.SOS_two.set()
    elif call.data == 'user_check_no':
        await call.message.answer('❓ Саволлар бўлими', reply_markup=await wbutton_one())
        await WomanAdmin.SOS_one.set()
