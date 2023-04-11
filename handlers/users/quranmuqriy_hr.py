from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.quranmuqriy_dk import muqriy_dk,muqriy_dict

from loader import bot, dp

CHANNEL_ID = -1001705654629

@dp.message_handler(text = "🎧 \"Қуръони карим\" тиловати \n(ўттиз пора)", state="*")
async def tartil(message: types.Message, state:FSMContext):
    await message.answer("\"Қуръони карим\" тиловати",
                         reply_markup = await muqriy_dk()
                         )
    await state.set_state("quranmuqriy_state")

@dp.message_handler(state="quranmuqriy_state")
async def quranmuqriy_func(msg: types.Message):
    if msg.text in muqriy_dict.keys():
        for n in muqriy_dict[msg.text]:
            await bot.copy_message(chat_id=msg.from_user.id,
                                   from_chat_id=CHANNEL_ID,
                                   message_id=n)
    else:
        await msg.answer("Илтимос, қуйидаги тугмалардан бирини танланг:")