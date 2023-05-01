import asyncio
import logging
import asyncpg

from aiogram import types
from aiogram.dispatcher import FSMContext
from typing import List
from keyboards.default.adminkeys import adm_adm
from keyboards.default.start_dk import main_keyboard
from keyboards.inline.elon_keys import yes_no

from data.config import BOT_ADMINS
from loader import dp, bot, db


@dp.message_handler(text="🏡 Бош меню", state="*")
async def boshmenyu_func(msg: types.Message, state: FSMContext):
    try:
        await db.add_user(telegram_id=msg.from_user.id)
    except asyncpg.exceptions.UniqueViolationError:
        pass
    await msg.answer("Бош меню", reply_markup=main_keyboard)
    await state.finish()


@dp.message_handler(text=['/bot_admins'], user_id=BOT_ADMINS, state="*")
async def buttons(msg: types.Message, state: FSMContext):
    await msg.answer("Админлар учун тугмалар",
                     reply_markup=adm_adm)
    await state.set_state("admbuttons")


@dp.message_handler(state="admbuttons", user_id=BOT_ADMINS)
async def bot_start(msg: types.Message, state: FSMContext):

    habar = "\nAvvalgi habarga javob olingan yo'qligini tekshirib ko'ring!"

    if msg.text == "users":
        count = await db.count_users()
        await msg.answer(f"\nБазада {count} та фойдаланувчи мавжуд.")

    elif msg.text == "Forward ON":
        await msg.answer(f"<b>FORWARD STATE</b> yoqildi!{habar}")
        await state.set_state("forw")

    elif msg.text == "MediaGroup ON":
        await msg.answer(f"<b>MEDIA GROUP STATE</b> yoqildi!{habar}")
        await state.set_state("mediagroup")

    elif msg.text == "ID ON":
        await msg.answer(f"<b>ID OLISH STATE</b> yoqildi!{habar}")
        await state.set_state("idolish")

    elif msg.text == "Sending messages":
        await msg.answer(f"<b>E'LON JO'NATISH STATE</b> yoqildi!{habar}")
        await state.set_state("elon")


@dp.message_handler(content_types=['video', 'audio', 'voice', 'photo', 'document', 'text'], user_id=BOT_ADMINS,
                    state="forw")
async def contumum(msg: types.Message, state: FSMContext):

    if msg.text == 'Forward OFF':
        await msg.answer("Forward ON state o'chirildi!")
        await state.set_state('admbuttons')
    else:
        if msg.video or msg.audio or msg.voice or msg.document or msg.photo or msg.text:

            await msg.answer("Хабар юборилмоқда...",
                             reply_markup=main_keyboard)
            await state.finish()

            users = await db.select_all_users()
            count_baza = await db.count_users()
            active = 0
            block = 0
            counter = 0

            for user in users:
                user_id = user[1]
                try:
                    await msg.forward(chat_id=user_id)

                    active += 1

                except Exception:

                    block += 1
                    continue

                counter += 1

                if counter == 25:
                    counter = 0
                    await asyncio.sleep(0.5)
            await state.finish()

            await msg.answer(f"SENT: <b>{active}</b>"
                             f"\nBLOCK: <b>{block}</b>"
                             f"\nALL_USERS: <b>{count_baza}</b>")

    active = 0
    block = 0
    counter = 0


@dp.message_handler(is_media_group=True, content_types=types.ContentType.ANY, state="mediagroup")
async def mediagr(msg: types.Message, album: List[types.Message], state: FSMContext):
    media_group = types.MediaGroup()
    for obj in album:
        if obj.photo:
            file_id = obj.photo[-1].file_id
        else:
            file_id = obj[obj.content_type].file_id
        try:
            media_group.attach({"media": file_id,
                                "type": obj.content_type,
                                "caption": obj.caption})
        except Exception as err:
            logging.exception(err)
            return await msg.answer("Бу альбомни aiogram қўлламайди!")

    users = await db.select_all_users()
    count_baza = await db.count_users()
    active = 0
    block = 0
    counter = 0
    await msg.answer(f"<i>Хабар юборилганлиги ҳақидаги тўлиқ маълумот тез орада юборилади</i>",
                     reply_markup=main_keyboard)
    for user in users:
        user_id = user[1]
        try:
            await bot.send_media_group(chat_id=user_id,
                                       media=media_group
                                       )
            active += 1

        except Exception:
            block += 1
            continue

        counter += 1

        if counter == 25:
            counter = 0
            await asyncio.sleep(0.5)
    await state.finish()
    await msg.answer(f"SENT: <b>{active}</b>"
                     f"\nBLOCK: <b>{block}</b>"
                     f"\nALL_USERS: <b>{count_baza}</b>")

    active = 0
    block = 0
    counter = 0


@dp.message_handler(state="mediagroup")
async def mediagryopish(msg: types.Message, state: FSMContext):
    if msg.text == "MediaGroup OFF":
        await msg.answer("<b>MEDIA GROUP STATE</b> ЎЧИРИЛДИ!")
        await state.set_state("admbuttons")


@dp.message_handler(content_types=['video', 'audio', 'voice', 'photo', 'document', 'text'], user_id=BOT_ADMINS,
                    state="idolish")
async def idvideo(msg: types.Message, state: FSMContext):
    if msg.video:
        await msg.answer(f"<b>VIDEO/CAPTION:</b> \n\n{msg.caption}"
                         f"<b>\n\nVIDEO/ID:</b> \n\n{msg.video.file_id}")
    if msg.audio:
        await msg.answer(f"<b>AUDIO/CAPTION:</b> \n\n{msg.caption}"
                         f"\n\n<b>AUDIO/ID:</b>\n\n{msg.audio.file_id}")
    if msg.voice:
        await msg.answer(f"<b>AUDIO/CAPTION:</b> \n\n{msg.caption}"
                         f"\n\n<b>AUDIO/ID:</b>\n\n{msg.voice.file_id}")
    if msg.photo:
        await msg.answer(f"<b>PHOTO/CAPTION:</b>\n\n{msg.caption}"
                         f"\n\n<b>PHOTO/ID:</b>\n\n{msg.photo[-1].file_id}")
    if msg.document:
        await msg.answer(f"<b>DOCUMENT/CAPTION:</b>\n\n{msg.caption}"
                         f"\n\n<b>DOCUMENT/ID:</b>\n\n{msg.document.file_id}")

    if msg.text == "ID OFF":
        await msg.answer("<b>ID OLISH STATE</b> ЎЧИРИЛДИ!")
        await state.set_state("admbuttons")

    elif msg.text:
        await msg.answer("Сиз <b>ID OLISH STATE</b>дасиз."
                         "\n\nЧиқиш учун <b>ID o'chirish</b> тугмасини босинг!")


@dp.message_handler(content_types=['text'], state="elon", user_id=BOT_ADMINS)
async def elonj(msg: types.Message, state: FSMContext):
    if msg.text == "Cancel sending messages":
        await msg.answer("<b>E'LON JO'NATISH STATE</b> ЎЧИРИЛДИ!")
        await state.set_state("admbuttons")

    elif msg.text:
        matn = msg.text
        await msg.answer("<b><i>Юборадиган хабарингизни текширдингизми?"
                         "\n\n<b>ОГОҲ БЎЛИНГ ХАБАРИНГИЗ КЎПЧИЛИККА БОРАДИ!!!</b>"
                         "\n\nХабарни юборасизми?</i></b>", reply_markup=yes_no)
        await state.update_data(text=matn)
        await state.set_state("yes_no")


@dp.callback_query_handler(state="yes_no")
async def checkyes_no(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    users = await db.select_all_users()
    count_baza = await db.count_users()
    active = 0
    block = 0
    counter = 0
    if call.data == "yes":
        await call.message.answer(f"<i>Хабар юборилганлиги ҳақидаги тўлиқ маълумот тез орада юборилади</i>",
                                  reply_markup=main_keyboard)
        await state.finish()

        for user in users:
            user_id = user[1]
            try:
                await bot.send_message(chat_id=user_id,
                                       text=data['text']
                                       )
                active += 1

            except Exception:
                block += 1
                continue

            counter += 1

            if counter == 25:
                counter = 0
                await asyncio.sleep(0.5)

        await call.message.answer(f"SENT: <b>{active}</b>"
                                  f"\nBLOCK: <b>{block}</b>"
                                  f"\nALL_USERS: <b>{count_baza}</b>")

    elif call.data == "no_again":
        await call.message.answer("Хабарингизни қайта юборишингиз мумкин!")
        await state.set_state("elon")

    active = 0
    block = 0
    counter = 0
