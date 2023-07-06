import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from typing import List

from data.config import WOMAN_GROUP
from keyboards.inline.sos_inline_keyboards import user_yes_no, user_check_ikeys

from loader import dp, sdb, bot
from states.sos_states import Man_Woman_State, Woman_State


async def first_check_woman(call, user_id, text_id=None, any_id=None, m_id=False, unique=False):
    try:
        if call.data == 'user_yes':
            woman_questions = await sdb.select_all_womanuser(user_id=user_id)
            if len(woman_questions) < 5:
                msg = await bot.send_message(chat_id=WOMAN_GROUP,
                                             text='Ботга янги хабар қабул қилинди! Кўриш учун /woman_questions '
                                                  'буйруғини киритинг')
                await call.message.answer('Саволингиз ҳақида админларимиз огоҳлантирилди! Яна хабар юборасизми?',
                                          reply_markup=user_check_ikeys)
                await Woman_State.user_checkone.set()
            else:
                await call.message.answer(text='Саволингиз ҳақида админларимиз огоҳлантирилди! Бештагача савол '
                                               'юборишингиз мумкин! Аввалги саволларингизга жавоб'
                                               'берилганидан сўнг яна савол юборсангиз бўлади!')
        elif call.data == 'user_no_again':
            if m_id:
                await sdb.delete_woman_id(m_id=text_id)
            elif unique:
                await sdb.delete_woman_unique(unique_id=any_id)
            await call.message.answer('<b><i>Хабарингизни қайта юборишингиз мумкин!</i></b>')
            await Man_Woman_State.woman_one.set()
        await call.message.delete()
    except Exception as err:
        logging.error(err)


async def second_check_woman(call, state):
    if call.data == 'user_check_yes':
        await call.message.answer('Хабарингизни киритинг:')
        await Man_Woman_State.woman_one.set()
    elif call.data == 'user_check_no':
        await call.message.answer('Бош меню')
        await state.finish()
    await call.message.delete()


@dp.message_handler(is_media_group=True, content_types=['video', 'photo', 'document', 'voice'],
                    state=Man_Woman_State.woman_one)
async def wa_two(msg: Message, album: List[Message], state: FSMContext):
    await msg.answer('Илтимос, фақат керакли файлни ўзини юборинг! Бир нечта жамланган файлларни қабул қила олмаймиз!')
    await state.finish()


@dp.message_handler(state=Man_Woman_State.woman_one, content_types=['audio', 'document', 'photo', 'text', 'video',
                                                                    'voice'])
async def wa_three(msg: Message, state: FSMContext):
    fullname = msg.from_user.full_name
    user_id = int(msg.from_user.id)
    await state.update_data({'wuser_id': user_id})
    m_one = '<b><i>Хабарингиз қабул қилинди! Тасдиқлайсизми?</i></b>'
    try:
        if msg.content_type == 'audio':
            await msg.answer_audio(audio=msg.audio.file_id, caption=msg.caption)
            await sdb.add_woman_audio(fullname=fullname, user_id=user_id, audio_id=msg.audio.file_id,
                                      unique_id=msg.audio.file_unique_id, caption=msg.caption, turi='audio')
            user_audio = await sdb.select_woman_audio(user_id=user_id, turi='audio')
            for n in user_audio:
                if n[1] == msg.audio.file_unique_id:
                    await state.update_data({'waudio_unique': n[1]})
            await Woman_State.woman_audio.set()
            await msg.answer(m_one, reply_markup=user_yes_no)

        elif msg.content_type == 'document':
            await msg.answer_document(document=msg.document.file_id, caption=msg.caption)
            await sdb.add_woman_document(fullname=fullname, user_id=user_id, document_id=msg.document.file_id,
                                         unique_id=msg.document.file_unique_id, caption=msg.caption, turi='document')
            user_document = await sdb.select_woman_document(user_id=user_id, turi='document')
            for n in user_document:
                if n[1] == msg.document.file_unique_id:
                    await state.update_data({'wdocument_unique': n[1]})
            await Woman_State.woman_document.set()
            await msg.answer(m_one, reply_markup=user_yes_no)

        elif msg.content_type == 'photo':
            await msg.answer_photo(photo=msg.photo[-1].file_id, caption=msg.caption)
            await sdb.add_woman_photo(fullname=fullname, user_id=user_id, photo_id=msg.photo[-1].file_id,
                                      unique_id=msg.photo[-1].file_unique_id, caption=msg.caption, turi='photo')
            user_photo = await sdb.select_woman_photo(user_id=user_id, turi='photo')
            for n in user_photo:
                if n[1] == msg.photo[-1].file_unique_id:
                    await state.update_data({'wphoto_unique': n[1]})
            await Woman_State.woman_photo.set()
            await msg.answer(m_one, reply_markup=user_yes_no)

        elif msg.content_type == 'text':
            await msg.answer(msg.text)
            await sdb.add_woman_text(fullname=fullname, user_id=msg.from_user.id, text=msg.text, turi='text')
            user_text = await sdb.select_woman_text(user_id=user_id, turi='text')
            for n in user_text:
                if n[1] == msg.text:
                    await state.update_data({'wquestion_id': n[0]})
            await Woman_State.woman_text.set()
            await msg.answer(m_one, reply_markup=user_yes_no)

        elif msg.content_type == 'video':
            await msg.answer_video(video=msg.video.file_id, caption=msg.caption)
            await sdb.add_woman_video(fullname=fullname, user_id=user_id, video_id=msg.video.file_id,
                                      unique_id=msg.video.file_unique_id, caption=msg.caption, turi='video')
            user_video = await sdb.select_woman_video(user_id=user_id, turi='video')
            for n in user_video:
                if n[1] == msg.video.file_unique_id:
                    await state.update_data({'wvideo_unique': n[1]})
            await Woman_State.woman_video.set()
            await msg.answer(m_one, reply_markup=user_yes_no)

        elif msg.content_type == 'voice':
            await msg.answer_voice(voice=msg.voice.file_id, caption=msg.caption)
            await sdb.add_woman_voice(fullname=fullname, user_id=user_id, voice_id=msg.voice.file_id,
                                      unique_id=msg.voice.file_unique_id, caption=msg.caption, turi='voice')
            user_voice = await sdb.select_woman_voice(user_id=user_id, turi='voice')
            for n in user_voice:
                if n[1] == msg.voice.file_unique_id:
                    await state.update_data({'wvoice_unique': n[1]})
            await Woman_State.woman_voice.set()
            await msg.answer(m_one, reply_markup=user_yes_no)
        elif msg.content_type:
            await msg.answer('Фақат аудио/видео/матн/расм/овозли ва ҳужжат шаклидаги саволлар қабул қилинади!!!')
        await msg.delete()
    except Exception as err:
        logging.error(err)
        await msg.answer('Бир марта ботга старт буйруғини киритиб хабарингизни қайта киритинг')


@dp.callback_query_handler(state=Woman_State.woman_audio)
async def wa_four(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    unique = data['waudio_unique']
    await first_check_woman(call=call, user_id=data['wuser_id'], any_id=unique, unique=True)


@dp.callback_query_handler(state=Woman_State.woman_document)
async def wa_five(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    unique = data['wdocument_unique']
    await first_check_woman(call=call, user_id=data['wuser_id'], any_id=unique, unique=True)


@dp.callback_query_handler(state=Woman_State.woman_photo)
async def statephotoid_func(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    unique = data['wphoto_unique']
    await first_check_woman(call=call, user_id=data['wuser_id'], any_id=unique, unique=True)


@dp.callback_query_handler(state=Woman_State.woman_text)
async def statesos2_func(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data['wquestion_id']
    await first_check_woman(call=call, user_id=data['wuser_id'], text_id=int(text), m_id=True)


@dp.callback_query_handler(state=Woman_State.woman_video)
async def statevideoid_func(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    unique = data['wvideo_unique']
    await first_check_woman(call=call, user_id=data['wuser_id'], any_id=unique, unique=True)


@dp.callback_query_handler(state=Woman_State.woman_voice)
async def statevoiceid_func(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    unique = data['wvoice_unique']
    await first_check_woman(call=call, user_id=data['wuser_id'], any_id=unique, unique=True)


@dp.callback_query_handler(state=Woman_State.user_checkone)
async def check_ikeys_func(call: CallbackQuery, state: FSMContext):
    await second_check_woman(call=call, state=state)
