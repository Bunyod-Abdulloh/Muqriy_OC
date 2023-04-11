from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from states.data import Edit
from keyboards.default.hamnafas_dk import hamnafas_dk, hamnafas_dklist
from loader import dp, bot

CHANNEL_ID = -1001705654629

hamnafas_dict = {1:{'v':'BAACAgIAAxkBAAEEa55ioFJ9umVmTZ6ZLNDN8QABcKqy8NIAAiUEAAIrZnhKogPZTm-_JYYkBA','c':'Яҳёхон қори дада билан суҳбат.\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},2:{'v':'BAACAgIAAxkBAAEEa6FioFKWee6DKqftcdWFt5zMLtK4lwACBwMAAlF3sUoa7mD7EgxjTyQE','c':'Муҳсинжон қори дада.\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},3:{'v':'BAACAgIAAxkBAAEEa6NioFKdl7w6VG9vLks3KIj3LM0t9gACLQIAAo6Q8EpufcbGkG6BEyQE','c':'Андижонлик Ҳабибуллоҳ қори дада билан суҳбат\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},4:{'v':'BAACAgIAAxkBAAEEa6VioFKoZBpKaX5I6A-iOzO54lSiwQACmAQAAiyoOUtz5Q3_YO9-pCQE','c':'Оққўрғонлик Муҳаммадхон қори дада билан суҳбат.\n\n1-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},5:{'v':'BAACAgIAAxkBAAEEa6dioFK86FgwK2dHbNhqBjdv9mkdXQACmgQAAiyoOUsknZNb8UrhRSQE','c':'Оққўрғонлик Муҳаммадхон қори дада билан суҳбат\n\n2-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},6:{'v':'BAACAgIAAxkBAAEEa6lioFLGreNwx8oMhDGvcbzDzGkEywACUgIAAo_wSUtksw6gQXR2TiQE','c':'Андижонлик Неъматуллоҳ қори дада билан суҳбат\n\n1-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},7:{'v':'BAACAgIAAxkBAAEEa6tioFLQYB2bdIK7Z8nLi3DxHPpsuAAC7QMAAnroaUvtiiqErbhtzyQE','c':'Андижонлик Неъматуллоҳ қори дада билан суҳбат\n\n2-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},8:{'v':'BAACAgIAAxkBAAEEa61ioFLapk37SCqGRpD2phnSrq_bwwAC6AIAAo_0aEub4x1-LQvDoyQE','c':'Андижонлик Неъматуллоҳ қори дада билан суҳбат\n\n3-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},9:{'v':'BAACAgIAAxkBAAEEa69ioFLx97u0rcT9YTedB0YwRXVXKAAClgIAAorCgEunOInIDXcb8yQE','c':'Тошкентлик Раҳматуллоҳ қори дада Обидов билан суҳбат\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},10:{'v':'BAACAgIAAxkBAAEEa7FioFL3KHLIoZ31laN2Mwnv32pxVQAClwIAAiV1iEu1zmyjfqEvsSQE','c':'Қўқонлик Ҳошимжон қори дада билан суҳбат\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},11:{'v':'BAACAgIAAxkBAAEEa7NioFMAARsX7u4pt4PQ5EzgoaIwiq4AAgwCAAINtZBLc2EV20w1V3UkBA','c':'Чустлик Ҳафизуллоҳ қори дада билан суҳбат\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},12:{'v':'BAACAgIAAxkBAAEEa7VioFMMA8dwJUAVjc-DmptFXW2fBwACWwQAAoI_qUs-bu7siGJVJCQE','c':'Андижонлик Абдужалил қори ака билан суҳбат\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},13:{'v':'BAACAgIAAxkBAAEEa7dioFMX3cowZrLGNgYmitJnuCP4hgACOgQAAoI_sUuxQWt86f3mViQE','c':'Тошкентлик Зоҳидхон қори дада билан суҳбат\n\n1-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},14:{'v':'BAACAgIAAxkBAAEEa7xioFMk7y9a2iQng7FkQ4AG8WSmUAACqQYAAsv_gEnSwyDyr8YESiQE','c':'Тошкентлик Зоҳидхон қори дада билан суҳбат \n\n2-қисм\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'},15:{'v':'BAACAgIAAxkBAAEG65FiwzkbO6p6foLUEQrCXn4W7-OpJAACqwYAAsv_gEksYhwk-dc_CCkE','c':'Тошкентлик Зоҳидхон қори дада билан суҳбат \n\n3-қисм\n\nУшбу видеолавҳада ёш қорилар ва фарзандининг қори бўлишини ҳохлаганлар учун жуда керакли бўлган тавсиялар ҳамда кўплаб фойдали маълумотларни устоз Зоҳидхон қори дададан тинглашлари мумкин.\n\n<a href=\'@quranuz_kanali\'>@quranuz_kanali</a>'}}

@dp.message_handler(text="📌 Қуръон ила ҳамнафас")
async def hamnafasvid(msg: types.Message, state: FSMContext):
    await msg.answer("📌 Қуръон ила ҳамнафас",
                     reply_markup = await hamnafas_dk())
    await state.set_state("hamnafas_state")
@dp.message_handler(state="hamnafas_state")
async def iqrohands(msg: types.Message, state: FSMContext):
    hd = hamnafas_dklist
    mt = msg.text

    if mt in hd:
        if mt == hd[0]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=459)
        elif mt == hd[1]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=460)
        elif mt == hd[2]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=461)
        elif mt == hd[3]:
            for n in range(462,464):
                await bot.copy_message(chat_id=msg.from_user.id,
                                       from_chat_id=CHANNEL_ID,
                                       message_id=n)
        elif mt == hd[4]:
            for n in range(464,467):
                await bot.copy_message(chat_id=msg.from_user.id,
                                       from_chat_id=CHANNEL_ID,
                                       message_id=n)
        elif mt == hd[5]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=467)
        elif mt == hd[6]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=468)
        elif mt == hd[7]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=469)
        elif mt == hd[8]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=470)
        elif mt == hd[9]:
            for n in range(471,474):
                await bot.copy_message(chat_id=msg.from_user.id,
                                       from_chat_id=CHANNEL_ID,
                                       message_id=n)
    else:
        await msg.answer("Илтимос, қуйидаги тугмалардан бирини танланг:")