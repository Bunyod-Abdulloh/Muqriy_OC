from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.shamoil_dk import sham_m, sham_v, sham_a

hazrat = "\n\n<a href='https://www.facebook.com/hazratim.uz'>Facebook</a> | <a href='https://www.instagram.com/hazratim_uz/'>Instagram</a> | <a href='https://t.me/joinchat/AAAAAFki3TLL4WCIyXw22g'>Telegram</a> | <a href='https://www.youtube.com/channel/UCWQFfFcK6Qt1zNrdlY1LF9Q'>Youtube</a>"

# VIDEO HANDLER

@dp.message_handler(text = "☀ Шамоилул Муҳаммадия")
async def shamoil_menyu(msg: types.Message, state:FSMContext):
    await msg.answer_photo(photo="AgACAgIAAxkBAAIBwGI_Df9YBlWxOLW01nPiNNONGUhhAAInsDEbCC-JSRowbITtWFr2AQADAgADeQADIwQ",
                           caption="\n\n“Шайх Муҳаммад Содиқ Муҳаммад Юсуф” жоме масжидида сийратга оид суҳбатлар "
                                   "давом этади."
                                   "\nҲафтанинг душанба ва пайшанба кунлари шом намозидан кейин буюк "
                                   "ватандошимиз Абу Ийсо Муҳаммад Термизийнинг «Шамоилул‑Муҳаммадия» "
                                   "китобидан ўқиб берилади. Асар китобни ўқиб, таржима қилиб берувчидан "
                                   "муаллифгача туташ санад асосида тақдим этилади. Суҳбатларда "
                                   "мунтазам қатнашган кишилар ушбу асар бўйича санадга эга "
                                   "бўлишлари мумкин."
                                   "\n\nCуҳбатлари 53 та суҳбатлар тўпламидан иборат."
                                   "\n\nСуҳбатларни “Шайх Муҳаммад Содиқ Муҳаммад Юсуф” жоме масжиди имом "
                                   "ноиби Ҳасанхон Яҳё Абдулмажид олиб боради."
                                   "\n\nБиринчи мажлис 2020-йил 16 ноябрь куни Имом Термизий ва у "
                                   "кишининг «Шамоилул‑Муҳаммадия» китоби ҳамда санад ҳақидаги суҳбат "
                                   "билан бошланади.", reply_markup=sham_m)
    await state.set_state("sham_m")

@dp.message_handler(text = "🎬 Bидео", state="sham_m")
async def shamoil_video01(msg: types.Message, state:FSMContext):
    await msg.answer("Суҳбатларни видео шаклини танладингиз", reply_markup=sham_v)
    await state.set_state("sham_v")

@dp.message_handler(text = "⏮ Oлдинги", state="sham_v")
async def backshamv(msg: types.Message, state:FSMContext):
    await msg.answer("⏮ Oлдинги", reply_markup=sham_m)
    await state.set_state("sham_m")

@dp.message_handler(text = "Mуқаддима", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBVGI_DBoaXhY-FbhQ6oCdEiAi1QhyAALoCwAC1EspSmEuuGDOlhAJIwQ",
                           caption="Шамоилул-Муҳаммадия | Муқаддима"
                                   "\n\nМавзу: Имом Термизий ва у кишининг «Шамоилул‑Муҳаммадия» китоби "
                                   "ҳамда санад ҳақида" + hazrat)

@dp.message_handler(text = "1 - 4 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBVmI_DCAjby_ecILfMwZp6RwHELgOAAKPCQAC4_6ZSj6QrkNPVsWiIwQ",
                           caption="Шамоилул-Муҳаммадия | 1-СУҲБАТ \n\n19.11.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBWGI_DCWviibtcAOHBNWEeRnLeRw5AAIJCgAC8MwBS-mDHU35oI5hIwQ",
                           caption="Шамоилул-Муҳаммадия | 2-СУҲБАТ \n\n23.11.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBWmI_DCrCpUSLk43EWLxa4h7uw36iAAIECgAC8MwRS1pWDqGpzVD1IwQ",
                           caption="Шамоилул-Муҳаммадия | 3-СУҲБАТ \n\n26.11.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBXGI_DC5ix5tcv13wKtZ5ojjkFyHqAAIQCQACunYhS2ZbUGTd1jtcIwQ",
                           caption="Шамоилул-Муҳаммадия | 4-СУҲБАТ \n\n30.11.2020 й." + hazrat)

@dp.message_handler(text = "5 - 8 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBXmI_DEnXAAGk6IZRIbUdAy_t3tvmVwACyAkAArSeMUt3_OcYkUpvhSME",
                           caption="Шамоилул-Муҳаммадия | 5-СУҲБАТ \n\n03.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBYGI_DE3dW_XwJCXcZiG5NTiRlRYtAALRCQACwwABOUvWi4au5n2sXyME",
                           caption="Шамоилул-Муҳаммадия | 6-СУҲБАТ \n\n07.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBYmI_DFNKfvY4qWJvp2LA9A9xvtUeAAJmCAAChuJZS29fjo8eSPaVIwQ",
                           caption="Шамоилул-Муҳаммадия | 7-СУҲБАТ \n\n07.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBZGI_DF1VFzxx5f47rsbcHdGnfJAZAAKdCQAChuJZS-2OqE2xlMh_IwQ",
                           caption="Шамоилул-Муҳаммадия | 8-СУҲБАТ\n\n14.12.2020 й." + hazrat)

@dp.message_handler(text = "9 - 12 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBZmI_DGOyrobVGFpK1P5-aP2OzV0-AALkCgAC3ViYSzoEWKVQTJ66IwQ",
                           caption="Шамоилул-Муҳаммадия | 9-СУҲБАТ\n\n17.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBaGI_DGqzfIf-vLuFtetEYlOTkerIAALsCgAC3ViYS70Oy0c_NfZgIwQ",
                           caption="Шамоилул-Муҳаммадия | 10-СУҲБАТ\n\n21.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBamI_DHDt5NttdBCkMw16DZEKM5o6AALfCQACEkSxSzEeY4B3kzIjIwQ",
                           caption="Шамоилул-Муҳаммадия | 11-СУҲБАТ\n\n24.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBbGI_DHZ2C19GzTVRJvlh5tfQ6nuBAALhCQACEkSxS918VeR1kYyTIwQ",
                           caption="Шамоилул-Муҳаммадия | 12-СУҲБАТ\n\n28.12.2020 й." + hazrat)

@dp.message_handler(text = "13 - 16 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBbmI_DHsovgXFOKpW0YGXLykqDzW7AAIkCwACUG_RSzBP6qjAPHDrIwQ",
                           caption="Шамоилул-Муҳаммадия | 13-СУҲБАТ\n\n31.12.2020 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBcGI_DIGSXCrehdUy5AGOAS-aHvuMAAI2CQACffnoSxpHgka7dZltIwQ",
                           caption="Шамоилул-Муҳаммадия | 14-СУҲБАТ\n\n04.01.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBcmI_DIchsmXaArKitQihPBT81K9QAAI5CgACffnoSykxrgv_EhMzIwQ",
                           caption="Шамоилул-Муҳаммадия | 15-СУҲБАТ\n\n07.01.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBdGI_DI5OAALMkFwH_ag7j8D-GhXwAAL-DAACzfZ5SLgQnIk3vB8RIwQ",
                           caption="Шамоилул-Муҳаммадия | 16-СУҲБАТ\n\n11.01.2021 й." + hazrat)

@dp.message_handler(text = "17 - 20 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBdmI_DJPkhlVM9Xl4Y2k9LzhaMkFtAAMNAALN9nlISzJdS2I7qI4jBA",
                           caption="Шамоилул-Муҳаммадия | 17-СУҲБАТ\n\n14.01.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBeGI_DJjWtv0FHUqiGCMt6BGk9Fl9AAIBDQACzfZ5SI8JckdaNeJSIwQ",
                           caption="Шамоилул-Муҳаммадия | 18-СУҲБАТ\n\n18.01.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBemI_DJ4aB-lvv2CLf8pAjAuUUNJTAAICDQACzfZ5SJFR6tI4-IfyIwQ",
                           caption="Шамоилул-Муҳаммадия | 19-СУҲБАТ\n\n21.01.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBfGI_DKQEo6fDkicmJVAbqQW5vk21AAKkDQACUEwRSXIRaOnet7voIwQ",
                           caption="Шамоилул-Муҳаммадия | 20-СУҲБАТ\n\n25.01.2021 й." + hazrat)

@dp.message_handler(text = "21 - 24 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBfmI_DKo3q6VMJfsHoOUwbk31tTLvAALUCQACAStZSbk0A1APPQSBIwQ",
                           caption="Шамоилул-Муҳаммадия | 21-СУҲБАТ\n\n28.01.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBgGI_DK-0EXU5rHBCYjebTOBrCGE2AALnCQACAStZSZz8FRBGLZlfIwQ",
                           caption="Шамоилул-Муҳаммадия | 22-СУҲБАТ\n\n01.02.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBgmI_DLamrjQq10oXAAEbWGxhyHnQ9wACgAgAApCQcUmAPtOOz9KN0iME",
                           caption="Шамоилул-Муҳаммадия | 23-СУҲБАТ\n\n04.02.2021 й." + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBhGI_DLt-gm19Q4VPEFKo502SHcF5AAKoDAAC5faxScloAgAB53OqHCME",
                           caption="Шамоилул-Муҳаммадия | 24-СУҲБАТ\n\n08.02.2021 й." + hazrat)

@dp.message_handler(text = "25 - 28 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBhmI_DMRjG0mXzBIhfAkYb8mhau2aAAItCgAC9354SvcueTpUsmNcIwQ",
                           caption="Шамоилул-Муҳаммадия | 25-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBiGI_DMpusaCsF2_PzbD21Ba-TfwkAAK4DwACBj_ZSr551GoVZQbjIwQ",
                           caption="Шамоилул-Муҳаммадия | 26-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBimI_DNKZCXlEK7yLcdlmhLkq8NO-AALfDwACBj_ZSpRuPndOnsTEIwQ",
                           caption="Шамоилул-Муҳаммадия | 27-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBjGI_DOI5QUMx2kNcnOtHZqoUCaPpAAIdDAACCLsZS5WW5sGlFLZOIwQ",
                           caption="Шамоилул-Муҳаммадия | 28-СУҲБАТ" + hazrat)

@dp.message_handler(text = "29 - 32 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBjmI_DOojg1T-pZeGBDUMkjGz6JfvAAImDAAC5VxBS49Fj9WrjVP4IwQ",
                           caption="Шамоилул-Муҳаммадия | 29-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBkGI_DPhd6t4PRb8rfdbceDZGasHLAALdDQACLXFhSyZAyzIpa7PXIwQ",
                           caption="Шамоилул-Муҳаммадия | 30-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBkmI_DQABPIbaiV3ZCmqClZh-wxIddAACQg4AAlAfgEswLDKJKdp2pyME",
                           caption="Шамоилул-Муҳаммадия | 31-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBlGI_DQvAU7uGPU3ygN_fKe6eEGYFAAKfDQACxTWRSzqmvcCXhYENIwQ",
                           caption="Шамоилул-Муҳаммадия | 32-СУҲБАТ" + hazrat)

@dp.message_handler(text = "33 - 36 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBlmI_DRL-GZ4Wzhf6v6DFtsDMvUikAAJlDgACLlLJS4aI_qUPuxV0IwQ",
                           caption="Шамоилул-Муҳаммадия | 33-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBmGI_DRiI9AW14xMcpTmGRNzAJiZqAAKREAACdqhASBoum0vNM8YeIwQ",
                           caption="Шамоилул-Муҳаммадия | 34-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBmmI_DSP8h7R6lo2OFyAKCTpc0bzUAAKWEAACdqhASM0x802rMyqJIwQ",
                           caption="Шамоилул-Муҳаммадия | 35-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBnGI_DSmt_fgle1gtRM5ZEHZFG5TRAAKeEAACdqhASFoOiL-njtxLIwQ",
                           caption="Шамоилул-Муҳаммадия | 36-СУҲБАТ" + hazrat)

@dp.message_handler(text = "37 - 40 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBnmI_DTN2oTtRZNCdfmkXPx3xltxOAAKhEAACdqhASB9Cj2oGGX8LIwQ",
                           caption="Шамоилул-Муҳаммадия | 37-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBoGI_DT_3OYBFFo6i8EPtv7n2E_sfAAKjEAACdqhASJOBlHAIp2c9IwQ",
                           caption="Шамоилул-Муҳаммадия | 38-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBomI_DUqyBeism_Nm8leH_zoFO0ZuAAKmEAACdqhASCy9Y8NGJYVjIwQ",
                           caption="Шамоилул-Муҳаммадия | 39-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBpGI_DVBkYJcDATWYvzFAx6xhawNjAAKoEAACdqhASE3iEETsc2tXIwQ",
                           caption="Шамоилул-Муҳаммадия | 40-СУҲБАТ" + hazrat)

@dp.message_handler(text = "41 - 44 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBpmI_DVUDtQPZjD4jM-sKgP3nICn-AAKtEAACdqhASJbtTjOS0TrjIwQ",
                           caption="Шамоилул-Муҳаммадия | 41-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBqGI_DWEHcE3NLRdnw9VOVx4YvFqZAAKyEAACdqhASCxO9AABWLf-PiME",
                           caption="Шамоилул-Муҳаммадия | 42-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBqmI_DWeD3hhhI7as-XOhQtk7iXLUAAK3EAACdqhASJzoPGYiEeSqIwQ",
                           caption="Шамоилул-Муҳаммадия | 43-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBrGI_DWzPIbzWRCzXPPeNnaLyK0lwAAK5EAACdqhASCKsZ93IjluDIwQ",
                           caption="Шамоилул-Муҳаммадия | 44-СУҲБАТ" + hazrat)

@dp.message_handler(text = "45 - 48 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBrmI_DXd3CyE9Trr03QXWObLj8YjgAAK9EAACdqhASCTfkO5WLHVTIwQ",
                           caption="Шамоилул-Муҳаммадия | 45-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBsGI_DXxr4_IvTzdGb9OiWuiTy-4LAALAEAACdqhASAH10wffEiNOIwQ",
                           caption="Шамоилул-Муҳаммадия | 46-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBsmI_DYfkMJFCr85LvVg3o0quz0HgAALDEAACdqhASFrI7RHbEVRjIwQ",
                           caption="Шамоилул-Муҳаммадия | 47-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBtGI_DaJPLC9nuiE9KXjEhJ91-Z_QAALNEAACdqhASK9ItMMRRTZJIwQ",
                           caption="Шамоилул-Муҳаммадия | 48-СУҲБАТ" + hazrat)

@dp.message_handler(text = "49 - 52 cуҳбатлар", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBtmI_DaiaT62KhqQfOurc4tRTzWgRAALQEAACdqhASIz_SkXTWNO4IwQ",
                           caption="Шамоилул-Муҳаммадия | 49-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBuGI_Da46SNzH3m6bzuLLSQ3R4A3EAALSEAACdqhASHWkv0ArPTgsIwQ",
                           caption="Шамоилул-Муҳаммадия | 50-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBumI_DbYOL2UYiVykgVvc_t_4nXcAA9MQAAJ2qEBI_jJNi9w1o8IjBA",
                           caption="Шамоилул-Муҳаммадия | 51-СУҲБАТ" + hazrat)
    await msg.answer_video(video="BAACAgIAAxkBAAIBvGI_DbuaSHOdDb4BGcEotcBBTHWTAALVEAACdqhASGFzIC3HBcQhIwQ",
                           caption="Шамоилул-Муҳаммадия | 52-СУҲБАТ" + hazrat)

@dp.message_handler(text = "53 - cуҳбат", state="sham_v")
async def shamoil_video01(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIBvmI_DeWCPNfa51cnUrVuc7BuXensAAJzFwACZX5wSRybz3ca7kx-IwQ",
                           caption="Шамоилул-Муҳаммадия | Тўлдирувчи суҳбат" + hazrat)

# AUDIO HANDLER

@dp.message_handler(text = "🎧 Aудио", state="sham_m")
async def shamoil_func(msg: types.Message, state:FSMContext):
    await msg.answer("Суҳбатларни аудио шаклини танладингиз", reply_markup=sham_a)
    await state.set_state("sham_a")

@dp.message_handler(text = "⏮ Oлдинги", state="sham_a")
async def backshamv(msg: types.Message, state:FSMContext):
    await msg.answer("⏮ Oлдинги", reply_markup=sham_m)
    await state.set_state("sham_m")

@dp.message_handler(text = "Мyқaддима", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB2WI_GgABmT3BBUD9fE0iqib3_qDXXQACOBMAApq7gUlUsHds6k5o0iME", caption = hazrat)

@dp.message_handler(text = "1-5 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB22I_GgakeI45l1Z2o6LkW7Nccy-UAAI6EwACmruBSSo1p2Kxx4I_IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB3WI_GhWTpiCreEjbbd06EnxfjVCZAAI7EwACmruBSSDzvD2ISlBMIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB32I_Ghn8dY7lWqQwPuCglv5oSuCOAAI-EwACmruBSdDfWNDVwHW7IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB4WI_Gh-C6wUtk-SN_f4qlX_UqLjbAAJCEwACmruBSc62f-uOEco4IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB42I_Gi8Yfsafg-ivLegiwiseG9rcAAJDEwACmruBSbhqRYevKfh-IwQ", caption = hazrat)

@dp.message_handler(text = "6-10 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB5WI_Gj7j6Kd9wavcaWFUHsZdVkXOAAJEEwACmruBSRqLlFs49Hm3IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB52I_GkJtfaOFW3CJK77mBkXhTsdFAAJFEwACmruBSWyw-hRRXp72IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB6WI_GkgflZLJki7AlHJvcG0MD_NUAAJGEwACmruBSbjLwa6JW8zrIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB72I_GqrybI0ZpJ4qKIz5Tla7k6HbAAJHEwACmruBSVdCiW09D0EfIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB8WI_GrS1UygqFOUqJWYmKbGKdjrDAAJIEwACmruBSQPA8ScIVRltIwQ", caption = hazrat)

@dp.message_handler(text = "11-15 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB82I_Grng3rUTuQXG2Na_mxoW41knAAJJEwACmruBSe-J9lesMTJ5IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB9WI_GsFXsTT9zqd69qKEs58DbKh2AAJKEwACmruBSQuM37WpGMshIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB92I_GtNS6waN4ewwwXN6FKasIJcsAAJLEwACmruBSb7sTNbrOc1KIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB-WI_GtgpM82dDVKLri_No6oDgIugAAJMEwACmruBSZeI8g9mRVhDIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB-2I_Gt7YHJDbabf9jkW6th7LVVwyAAJNEwACmruBSSKUR7czSoyTIwQ", caption = hazrat)

@dp.message_handler(text = "16-20 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB_WI_Gui7jZ6HGNfsfbRy9wzQTzlDAAJOEwACmruBSQoklOVWGjbOIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAIB_2I_Gw6N5PJH6sbldmqPvnOEsgSIAAJPEwACmruBSQPI39TNx0WQIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICAWI_Gxrm9ThL-VeeAe0OKVnfAAF-CgACVBMAApq7gUnKlH3ZXRwl3yME", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICA2I_GyD3hR3K7BKMicLDGti0cPMOAAJQEwACmruBSTTkhM-jrwAB0SME", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICBWI_GyTG83xnFxYVYLK7VAsCKEW1AAJREwACmruBSRO1EyHMZgbmIwQ", caption = hazrat)

@dp.message_handler(text = "21-25 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICB2I_G23aRjQAAbIoit2sR9fdxgE0cAAC3AkAAgErWUnxH6kysxRqyCME", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICCWI_G3XSvlJMm9nzdd5lUf9ub1FyAALoCQACAStZSci3pfuFydofIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICC2I_G9pUnguc7LllMhlq5IOedmajAAKBCAACkJBxSeFsQ9hnD5OvIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICDWI_G96W-9ClNA98z-3UFzF7xfrkAAKqDAAC5faxSaj6dYwSJk1kIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICD2I_G-ILprUY7hQP286PguWlmHcEAAIvCgAC9354SuZH_4GbkgHwIwQ", caption = hazrat)

@dp.message_handler(text = "26-30 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICE2I_HBDsb3wcRnFw6YCGbYch2EVNAAK7DwACBj_ZSj4EhdCjGkezIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICFWI_HBXlqhbL-ZLAubmwvgSoTzN-AALgDwACBj_ZSqmllp-_fP4SIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICF2I_HBrko7CRRc7KW-_WsN16nabMAAIeDAACCLsZS3QBIBDwyollIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICGWI_HCVBGZ5YXcSXVYO8H41ZKyb8AAInDAAC5VxBS62Gyjuos2SYIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICG2I_HCo6QGAOkVS0lUjeMRiiN2_xAALeDQACLXFhS6Y_S47o5hJGIwQ", caption = hazrat)

@dp.message_handler(text = "31-35 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICHWI_HC50dk8UviNZRYTZUVAlcTVgAAJDDgACUB-AS25IYl9A-BilIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICH2I_HDPEw1gYzz1kXCNFYuuuqWCGAAKgDQACxTWRS1llD6bTlyx_IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICIWI_HDi89CUZuGVPHVnPOdV3n00yAAJmDgACLlLJSy0seq_stQuUIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICI2I_HDx1a_xW5_hc-1bc85BMc1xhAAKSEAACdqhASEB1qQHgLu_8IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICJWI_HED3velExjDF7jNVzpc8C9XZAAKYEAACdqhASEVJswABrVbT_iME", caption = hazrat)

@dp.message_handler(text = "36-40 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICJ2I_HEP49Ixol0dX0btnFsK6jCB6AAKfEAACdqhASHSxV6uzgEP7IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICKWI_HEdZrSHDxpP2uHD-BTp-HlzWAAKiEAACdqhASHOCrJHfK79pIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICK2I_HExtfBXmLf5K5pAOVoaZNhcVAAKkEAACdqhASB4v4a3HvETdIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICLWI_HFgHVv3gw3JjWolSra_NhIswAAKnEAACdqhASGEbJvTrf_uhIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICL2I_HFu6YreY_ruyYDyKvX3g20gmAAKqEAACdqhASP-Qa9ftnIqpIwQ", caption = hazrat)

@dp.message_handler(text = "41-45 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICMWI_HGD5HrMDSfDy_yJ-OHS4vrhtAAKvEAACdqhASLVPQ00yTar_IwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICM2I_HGSFTZfkoCZM56xUPIdjs-OOAAK0EAACdqhASNDn17e0KBDsIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICNWI_HGhCuxOMMGWQg_A9Rn8zQnZ5AAK4EAACdqhASLpwQUgFWKDnIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICN2I_HG1m_nfHjY4W56oQ4SGsks0BAAK6EAACdqhASHaskrVq8PJKIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICOWI_HHB-bhp4jySHXm_ebqDmbl3rAAK_EAACdqhASFIG8xDu1vLrIwQ", caption = hazrat)

@dp.message_handler(text = "46-50 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICO2I_HHT4cbluTauEmuL0d-2hW1FZAALCEAACdqhASAVUbjE_2WodIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICPWI_HHgvzWjVrLnYBzQvfTgYsjPlAALHEAACdqhASE1DbzC8lVGBIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICP2I_HH23C4wugNL8lz77qFH3uhFCAALOEAACdqhASIL39GmefPGBIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICQWI_HIKqEBQ1o7X3jAI6wwlDEuu_AALREAACdqhASN58g7HJZ7HEIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICQ2I_HIr-agnpAAH-zdpOmA_JlXAn9AAC1hAAAnaoQEg4hMtqp-QBHSME", caption = hazrat)

@dp.message_handler(text = "51-53 cуҳбатлар", state="sham_a")
async def shamoil_func(msg: types.Message):
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICRWI_HI4pVqWlo5JEJsetfJA4wG1rAALXEAACdqhASC4wpe3onwhxIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICR2I_HKZHLwtQ_XT-2QUXrNf0eyUKAALZEAACdqhASNb9whj5FaIoIwQ", caption = hazrat)
    await msg.answer_audio(audio = "CQACAgIAAxkBAAICSWI_HLKm6JM0Tu_yeITBBSsKnyFaAAJnEwACmruBSQTyanEDvukuIwQ", caption = hazrat)

