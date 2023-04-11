from aiogram import types

from aiogram.dispatcher import FSMContext
from keyboards.default.arbain_dk import arbmenyu_kb, arbbuttons, arbtext, arb_vdict, arb_adict, arb_tdict, arbain_roviylar_buttons, arbain_roviylar_dict

from loader import dp, bot

VIDEOCHANNEL = -1001510029140
AUDIOCHANNEL = -1001806542919
TEXTCHANNEL = -1001896668195
ROVIYCHANNEL = -1001840404210

@dp.message_handler(text = "📜 Арбаъин Нававийя шарҳи")
async def arbmh(msg: types.Message, state:FSMContext):
    await msg.answer("\"Арбаъин Нававийя\" суҳбатлари. \n\n<b>Ҳушхабар!</b> \n\nПайғамбаримиз Муҳаммад алайҳиссаломнинг муборак ҳадисларини санад билан эшитишни соғинганлар учун Имом Нававийнинг \"Арбаъин\" дарслари бошланади. \n\n2021-йил 26-ноябр, Жума куни хуфтон намозидан кейин соат 18:50 да Имом Нававий, \"Арбаъин\" асари ва санад ҳақида суҳбатларнинг Муқаддима қисми бўлиб ўтади. \n\nАсар санад орқали ўрганилади ва иншааллоҳ асар тугагач, хатмонада санад тақдим қилинади.\n\nҚатнашувчилар 3 хил даражадаги ижозаларга эга бўладилар: \n\n<b>1. Тўлиқ ижоза \n\n2. Иккинчи даражали ижоза.\n\n3. Дарсларда қатнашганлик ҳақида гувоҳнома.</b>\n\nАрабча ва ўзбекча матнларини ёдлаб берган киши имтихондан ўтказилади ва тўлиқ ижоза берилади.\n\nЎзбекча матнни ёдлаган киши, имтихон қилинади ва иккинчи даражадаги ижоза берилади.\n\nДарсларда қатнашган ёки онлайн кузатганларга дарсларда қатнашганлиги ҳақидаги гувоҳнома берилади.\n\nДарслар тугагандан кейин видеоларини кўриб чиққанларга иккинчи даражадаги гувоҳнома берилади.\n\nДарсларнинг сўнгида иштирокчилар учун вазифалар берилади. \n\nДарслардан олинган фойдалар, дарслар ҳақидаги фикр-мулоҳазалар, таклифларни қуйидаги манзилга юборишингиз мумкин: t.me/masjiddarslari_bot",
                     reply_markup = arbmenyu_kb)
    await state.set_state("arbainmenyu")

@dp.message_handler(state="arbainmenyu")
async def arbainmenyufunc(msg: types.Message, state:FSMContext):

    if msg.text == "🎬 Bидeо":
        await msg.answer("🎬 Bидeо",
                         reply_markup = arbbuttons)
        await state.set_state("arbainvideo")

    elif msg.text == "🎧 Ayдио":
        await msg.answer("🎧 Ayдио",
                         reply_markup=arbbuttons)
        await state.set_state("arbainaudio")

    elif msg.text == "📑 Ҳадислар матни ва аудиолари":
        await msg.answer("📑 Ҳадислар матни ва аудиолари",
                         reply_markup = arbtext)
        await state.set_state("arbaintext")

    elif msg.text == "📜 Ҳадислар ровийлари":
        await bot.copy_message(chat_id = msg.from_user.id,
                               from_chat_id = ROVIYCHANNEL,
                               message_id = 11,
                               reply_markup = arbain_roviylar_buttons)
        await state.set_state("arbain_roviy")

@dp.message_handler(state="arbainvideo")
async def arbainvideofunc(msg: types.Message, state:FSMContext):

    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup = arbmenyu_kb)
        await state.set_state("arbainmenyu")

    elif msg.text in arb_vdict.keys():
        for n in arb_vdict[msg.text]:
            await bot.copy_message(
                chat_id=msg.from_user.id,
                from_chat_id=VIDEOCHANNEL,
                message_id=n
            )
    else:
        await msg.answer("Илтимос, қуйидаги тугмалардан бирини танланг:")

@dp.message_handler(state = "arbainaudio")
async def avstate(msg:types.Message, state:FSMContext):

    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup=arbmenyu_kb)
        await state.set_state("arbainmenyu")
    elif msg.text in arb_adict.keys():
        for n in arb_adict[msg.text]:
            await bot.copy_message(
                chat_id=msg.from_user.id,
                from_chat_id=AUDIOCHANNEL,
                message_id=n
            )
    else:
        await msg.answer("Илтимос, қуйидаги тугмалардан бирини танланг:")

@dp.message_handler(state = "arbaintext")
async def arbaintextfunc(msg: types.Message, state:FSMContext):

    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup = arbmenyu_kb)
        await state.set_state("arbainmenyu")

    elif msg.text in arb_tdict.keys():
        for n in arb_tdict[msg.text]:
            await bot.copy_message(
                chat_id=msg.from_user.id,
                from_chat_id=TEXTCHANNEL,
                message_id=n
            )
    else:
        await msg.answer("Илтимос, қуйидаги тугмалардан бирини танланг:")\

@dp.message_handler(state = "arbain_roviy")
async def arbainroviyfunc(msg: types.Message, state:FSMContext):

    if msg.text == "⏮ Олдинги":
        await msg.answer("⏮ Олдинги",
                         reply_markup = arbmenyu_kb)
        await state.set_state("arbainmenyu")

    elif msg.text in arbain_roviylar_dict.keys():
        for n in arbain_roviylar_dict[msg.text]:
            await bot.copy_message(
                chat_id=msg.from_user.id,
                from_chat_id=ROVIYCHANNEL,
                message_id=n
            )
    else:
        await msg.answer("Илтимос, қуйидаги тугмалардан бирини танланг:")