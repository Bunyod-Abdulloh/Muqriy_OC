import asyncpg
from aiogram.dispatcher import FSMContext
from aiogram import types

from data.config import CHANNELS
from keyboards.inline.qversein import check_button
from loader import bot, dp, db
from utils.misc import subscription
from keyboards.default.start_dk import main_keyboard

@dp.message_handler(commands=['start'], state="*")
async def show_channels(msg: types.Message, state: FSMContext):
    try:
        await db.add_user(
            telegram_id=msg.from_user.id,
            full_name=msg.from_user.full_name,
            username=msg.from_user.username,
        )
    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(telegram_id=msg.from_user.id)

    # channels_format = str()
    # for channel in CHANNELS:
    #     chat = await bot.get_chat(channel)
    #     invite_link = await chat.export_invite_link()
    #     #logging info (invite_link)
    #     channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await msg.answer(f"Ассалому алайкум!\nБу бот орқали Сиз Ҳасанхон Яҳё Абдулмажид қори дарсликларини аудио ва видео шаклда кўришингиз ва "
                         f"эшитишингиз мумкин.",
                         reply_markup=main_keyboard)
    await state.finish()

# @dp.callback_query_handler(text='check_subs') async def checker(call: types.CallbackQuery): await call.answer()
# result = str() for channel in CHANNELS: status = await subscription.check(user_id=call.from_user.id,
# channel=channel) channel = await bot.get_chat(channel) if status: result += f"✅ Сиз, <b>{channel.title}</b>
# каналимизга обуна бўлгансиз!\n\nБотимиздан фойдаланишингиз мумкин!" await call.message.answer(result,
# reply_markup=main_keyboard) try: await db.add_user( id=call.from_user.id, full_name=call.from_user.full_name,
# poralar="{}", ) except asyncpg.exceptions.UniqueViolationError: pass else: invite_link = await
# channel.export_invite_link() result += (f"❌ Сиз, <b>{channel.title}</b> каналимизга обуна бўлмагансиз! " f"<a
# href='{invite_link}'> Обуна бўлиш!</a>\n\n") await call.message.answer(result, disable_web_page_preview=True)
