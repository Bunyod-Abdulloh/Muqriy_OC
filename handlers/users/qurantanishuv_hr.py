from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.quran_talimi import tanishuv_aud_vid_keys, tanishuv_keys, tanishuv_aud_keys

# VIDEO HANDLER

@dp.message_handler(text = "☪ Қуръон билан танишув")
async def tartil(msg: types.Message, state:FSMContext):
    await msg.answer_photo(photo="AgACAgIAAxkBAAIMhGJEDh2UKj_PGNAsU4aV9YMQwb6gAAIKqzEb8ri5SqY7pXiTQEn5AQADAgADeQADIwQ",
                           caption="Уламоларимиз, хусусан, устозимиз Шайх Муҳаммад Содиқ Муҳаммад Юсуф раҳматуллоҳи "
                                   "алайҳи ҳар йили Рамазон ойида ўзига хос тайёргарлик қилиб, ушбу ойда халқимизга "
                                   "нимадир янги бир ёки бир неча илмий туҳфа тақдим этардилар. Улуғларимизнинг "
                                   "анъаналарини давом эттиришга хизмат қилиш илинжида айнан Шайх ҳазратлари номидаги "
                                   "масжидда 1442 - ҳижрий йил Рамазон ойи учун янги илмий суҳбатлар туркуми тақдим этилди. Ушбу суҳбатлар 26 та суҳбатлар туркумидан иборат. "
                                   "Бунда ҳар куни оқшом таровеҳда ўқиладиган сура ва оятлар билан танишиб борилган. "
                                   "Аллоҳ Ўзи мақбул ва манзур этсин! Дуоларингиздан умидвормиз!", reply_markup=tanishuv_aud_vid_keys)

    await state.set_state("qbt1")

@dp.message_handler(text = "🎞 Видео", state="qbt1")
async def tanishuv_video(msg: types.Message, state:FSMContext):
    await msg.answer("<b>Суҳбатлардан қуйидаги мавзулар ўрин олган: "
                     "\n\n1. ФОТИҲА СУРАСИ 1-ОЯТДАН БАҚАРА СУРАСИ 167-ОЯТГАЧА"
                     "\n\n2. БАҚАРА СУРАСИ 168-ОЯТДАН 286-ОЯТГАЧА"
                     "\n\n3. ОЛИ ИМРОН 1-ОЯТДАН 200-ОЯТГАЧА"
                     "\n\n4. НИСО СУРАСИ 1-ОЯТДАН 176-ОЯТГАЧА"
                     "\n\n5. МОИДА СУРАСИ 1-ОЯТДАН 120-ОЯТГАЧА "
                     "\n\n6. АЪРОФ СУРАСИ 1-ОЯТДАН 206-ОЯТГАЧА"
                     "\n\n7. АНФОЛ СУРАСИ 1-ОЯТДАН ТАВБА СУРАСИ 71-ОЯТГАЧА"
                     "\n\n8. ТАВБА СУРАСИ 72-ОЯТДАН ЮНУС СУРАСИ 109-ОЯТГАЧА"
                     "\n\n9. ҲУД СУРАСИ 1-ОЯТДАН ЮСУФ СУРАСИ 111-ОЯТГАЧА "
                     "\n\n10. РАЪД СУРАСИ 1-ОЯТДАН НАҲЛ СУРАСИ 50-ОЯТГАЧА "
                     "\n\n11. НАҲЛ СУРАСИ 51-ОЯТДАН ИСРО СУРАСИ 111-ОЯТГАЧА "
                     "\n\n12. КАҲФ СУРАСИ 1-ОЯТДАН МАРЯМ СУРАСИ 98-ОЯТГАЧА"
                     "\n\n13. ТОҲA СУРAСИ 1-ОЯТДАН AНБИЁ СУРAСИ 112-ОЯТГАЧА"
                     "\n\n14. ҲАЖ СУРAСИ 1-ОЯТДАН МУЪМИНУН СУРAСИ 118-ОЯТГАЧA"
                     "\n\n15. НУР СУРAСИ 1-ОЯТДАН ШУАРО СУРAСИ 227-ОЯТГАЧА "
                     "\n\n16. НАМЛ СУРAСИ 1-ОЯТДАН ҚОСОС СУРAСИ 88-ОЯТГАЧА "
                     "\n\n17. АНКАБУТ СУРAСИ 1-ОЯТДАН САЖДА СУРAСИ 30-ОЯТГАЧА"
                     "\n\n18. АҲЗОБ СУРAСИ 1-ОЯТДАН ФОТИР СУРAСИ 45-ОЯТГАЧА"
                     "\n\n19. ЁСИН СУРAСИ 1-ОЯТДАН ЗУМАР СУРAСИ 75-ОЯТГАЧА "
                     "\n\n20. ҒОФИР СУРAСИ 1-ОЯТДАН ШУУРО СУРAСИ 53-ОЯТГАЧА "
                     "\n\n21. ЗУҲРУФ СУРAСИ 1-ОЯТДАН  МУҲАММАД СУРAСИ 38-ОЯТГАЧА"
                     "\n\n22. ФАТҲ СУРAСИ 1-ОЯТДАН  ҚАМАР СУРAСИ 55-ОЯТГАЧА"
                     "\n\n23. РАҲМОН СУРAСИ 1-ОЯТДАН  СОФФ СУРAСИ 14-ОЯТГАЧА"
                     "\n\n24. ЖУМУЪА СУРAСИ 1-ОЯТДАН  НУҲ СУРAСИ 28-ОЯТГАЧА"
                     "\n\n25. ЖИН СУРAСИ 1-ОЯТДАН ИНШИҚОҚ СУРAСИ 24-ОЯТГАЧА"
                     "\n\n26. БУРУЖ СУРAСИ 1-ОЯТДАН АН-НОС СУРAСИ 6-ОЯТГАЧА</b>", reply_markup=tanishuv_keys)
    await state.set_state("qbt2")

@dp.message_handler(text = "⏮ Oлдинги", state="qbt2")
async def audio_video(msg: types.Message, state:FSMContext):
    await msg.answer("Қуръон билан танишув\" суҳбатлари 26 та суҳбатдан иборат",
                     reply_markup=tanishuv_aud_vid_keys)
    await state.set_state("qbt1")

@dp.message_handler(text = "1-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICqmI_Sg6FujTVu3QWqyZN_1Nf5zl4AAJ7CwACMfCpS2b61CNn1eIvIwQ",
        caption="🟢 ФОТИҲА СУРАСИ 1-ОЯТДАН БАҚАРА СУРАСИ 167-ОЯТГАЧА | "
                "Қуръон билан танишув | 1-СУҲБАТ"
                "\n\n<a href='https://www.youtube.com/watch?v=hFKprd8i5es'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "2-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICrGI_ShZazCwRJwYeo6MDEMfNXYuqAAJaCwAC6SHYSz7Z5iN_fn1qIwQ",
        caption="🟢 БАҚАРА СУРАСИ 168-ОЯТДАН 286-ОЯТГАЧА | "
                "Қуръон билан танишув \n2-Суҳбат"
                "\n\n<a href='https://youtu.be/bIJEHkgNw28'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "3-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICrmI_Sh-5dJ_e3sCvcxaFUSNXpi1jAAJ1CwAC6SHYS1xyubBza6eHIwQ",
        caption="🟢 ОЛИ ИМРОН 1-ОЯТДАН 200-ОЯТГАЧА | "
                "Қуръон билан танишув \n3-СУҲБАТ"
                "\n\n<a href='https://youtu.be/vRp12r8cUh0'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "4-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICsGI_Sjzk1ZE4X3iq2aFDGhPTrBpgAALlCwACea3pS1fGkTQ1ewJDIwQ",
        caption="🟢 НИСО СУРАСИ 1-ОЯТДАН 176-ОЯТГАЧА | "
                "Қуръон билан танишув \n4-СУҲБАТ"
                "\n\n<a href='https://youtu.be/vNyDc7_zCCw'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "5-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICsmI_Slm4Iu_yAuJvQY9EpVZ_Y2vsAALnCwACea3pS7rlC75HAAEI5iME",
        caption="🟢 МОИДА СУРАСИ 1-ОЯТДАН 120-ОЯТГАЧА | "
                "Қуръон билан танишув \n5-СУҲБАТ"
                "\n\n<a href='https://youtu.be/PlwCCuO9znY'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "6-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICtGI_SmEpSJcjXdPFxKagsKH6SGvvAAJ8CwAC5bgAAUgEFCuxEUufQyME",
        caption="🟢 АЪРОФ СУРАСИ 1-ОЯТДАН 206-ОЯТГАЧА | "
                "Қуръон билан танишув \n6-СУҲБАТ"
                "\n\n<a href='https://youtu.be/HZFntkN1PBc'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "7-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICtmI_Smqu-urfbR7K5iS-Jrxb0bvbAAJ_CwAC5bgAAUi8obUkWoEL1SME",
        caption="🟢 АНФОЛ СУРАСИ 1-ОЯТДАН ТАВБА СУРАСИ 71-ОЯТГАЧА | "
                "Қуръон билан танишув \n7-СУҲБАТ"
                "\n\n<a href='https://youtu.be/2bhfxfdzaD8'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "8-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICuGI_SnJxhtF-cEDFP2ORCYpwc7QCAAKACwAC5bgAAUgt9VLIbPB2KSME",
        caption="🟢 ТАВБА СУРАСИ 72-ОЯТДАН ЮНУС СУРАСИ 109-ОЯТГАЧА | "
                "Қуръон билан танишув \n8-СУҲБАТ"
                "\n\n<a href='https://youtu.be/0o8HWFRiI98'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "9-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICumI_SnmWZOohWn0UQol_RXbDtiftAAKzDAACvNQhSHB7-ZlPWqD5IwQ",
        caption="🟢 ҲУД СУРАСИ 1-ОЯТДАН ЮСУФ СУРАСИ 111-ОЯТГАЧА | "
                "Қуръон билан танишув \n9-СУҲБАТ | (1-ҚИСМ)"
                "\n\n<a href='https://youtu.be/EH5gpf7Q9cg'> Youtube орқали кўриш</a>")
    await msg.answer_video(
        video="BAACAgIAAxkBAAICvGI_Sn_Nc_5Y9uPk7pt_51RVoUEjAAK1DAACvNQhSEW5DWob-BQbIwQ",
        caption="🟢 ҲУД СУРАСИ 1-ОЯТДАН ЮСУФ СУРАСИ 111-ОЯТГАЧА |"
                " Қуръон билан танишув \n9-СУҲБАТ | (2-ҚИСМ)"
                "\n\n<a href='https://youtu.be/9YcaKuWqOK0'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "10-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICvmI_SoX557qzsEBFYPDOlRQBitRuAAK3DAACvNQhSHT4QhJa_Tb8IwQ",
        caption="🟢 РАЪД СУРАСИ 1-ОЯТДАН НАҲЛ СУРАСИ 50-ОЯТГАЧА | "
                "Қуръон билан танишув \n10-СУҲБАТ"
                "\n\n<a href='https://youtu.be/ObKtC7-yj0Y'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "11-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICwGI_SpSL7N96JWiAnGITDM8nKY8gAAK7DAACvNQhSDC1FSuLEP_tIwQ",
        caption="🟢 НАҲЛ СУРАСИ 51-ОЯТДАН ИСРО СУРАСИ 111-ОЯТГАЧА | "
                "Қуръон билан танишув \n11-СУҲБАТ"
                "\n\n<a href='https://youtu.be/xre297NiiS8'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "12-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICwmI_SpkrWTZnDPmVRXHAozfN2rVFAAK_DAACvNQhSC43WmCQzG9HIwQ",
        caption="🟢 КАҲФ СУРАСИ 1-ОЯТДАН МАРЯМ СУРАСИ 98-ОЯТГАЧА  | "
                "Қуръон билан танишув \n12-СУҲБАТ"
                "\n\n<a href='https://youtu.be/SqUQsMZdC4E'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "13-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICxGI_Sp_w15oOlidPy2fYjmoG6OsoAALdDQACjsVBSNUFi7s6mktwIwQ",
        caption="🟢 ТОҲA СУРAСИ 1-ОЯТДАН AНБИЁ СУРAСИ 112-ОЯТГАЧА  | "
                "Қуръон билан танишув \n13-СУҲБАТ"
                "\n\n<a href='https://youtu.be/qY5YDuIKoRU'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "14-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICxmI_SqaFMnTjVS4NqFfW3VMaka2uAALkDQACBulASPgVfzspehSbIwQ",
        caption="🟢 ҲАЖ СУРAСИ 1-ОЯТДАН МУЪМИНУН СУРAСИ 118-ОЯТГАЧA  | "
                "Қуръон билан танишув \n14-СУҲБАТ"
                "\n\n<a href='https://youtu.be/TX3ed3NuuP0'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "15-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICyGI_SrWT01CQ1Mtb_Olwq69ck1LBAAL0DAACx3JpSKD4kf3YKzf_IwQ",
        caption="🟢 НУР СУРAСИ 1-ОЯТДАН ШУАРО СУРAСИ 227-ОЯТГАЧА  | "
                "Қуръон билан танишув \n15-СУҲБАТ"
                "\n\n<a href='https://youtu.be/JbLQwXycij0'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "16-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICymI_St0x7860uP5xGhN2i3ZOlVwqAAKLDAACx3JxSHb-FaPKI6DqIwQ",
        caption="🟢 НАМЛ СУРAСИ 1-ОЯТДАН ҚОСОС СУРAСИ 88-ОЯТГАЧА  | "
                "Қуръон билан танишув \n16-СУҲБАТ"
                "\n\n<a href='https://youtu.be/YiYDklXiXhg'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "17-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICzGI_SuPiql8zR-zu8Yrg6qS31nt4AAKPDAACx3JxSEXVvH3knXcbIwQ",
        caption="🟢 АНКАБУТ СУРAСИ 1-ОЯТДАН САЖДА СУРAСИ 30-ОЯТГАЧА | "
                "Қуръон билан танишув \n17-СУҲБАТ"
                "\n\n<a href='https://youtu.be/BZFOJfYZDV8'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "18-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAICzmI_Sul495WcXKYcBB5g5p5YiuP0AAKSDAACx3JxSPSgJbkJnAh5IwQ",
        caption="🟢 АҲЗОБ СУРAСИ 1-ОЯТДАН ФОТИР СУРAСИ 45-ОЯТГАЧА | "
                "Қуръон билан танишув \n18-СУҲБАТ"
                "\n\n<a href='https://youtu.be/BZFOJfYZDV8'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "19-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC0GI_Su_nzLLPPXsumwx3ui2lfPxxAAKeDAACx3JxSJ1JoA6kR9_FIwQ",
        caption="🟢 ЁСИН СУРAСИ 1-ОЯТДАН ЗУМАР СУРAСИ 75-ОЯТГАЧА | "
                "Қуръон билан танишув \n19-СУҲБАТ"
                "\n\n<a href='https://youtu.be/F5qGLRIl6Qc'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "20-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC0mI_SvVYUXVDlblL7h-QIukMBVixAAKfDgACjqWYSJxvy-xtWmT2IwQ",
        caption="🟢 ҒОФИР СУРAСИ 1-ОЯТДАН ШУУРО СУРAСИ 53-ОЯТГАЧА | "
                "Қуръон билан танишув \n20-СУҲБАТ"
                "\n\n<a href='https://youtu.be/TBEM2jlL8v8'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "21-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC1GI_SvtHPZWEzpo3xFUiJInTarBBAAJqDQACjqWgSIEbugNoLmSOIwQ",
        caption="🟢 ЗУҲРУФ СУРAСИ 1-ОЯТДАН  МУҲАММАД СУРAСИ 38-ОЯТГАЧА | "
                "Қуръон билан танишув \n21-СУҲБАТ"
                "\n\n<a href='https://youtu.be/5s2yOY8hPwU'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "22-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC1mI_SwIDR7V67t45I_Ni3fvHYY3GAAJvDQACjqWgSBErN5rHwplvIwQ",
        caption="🟢 ФАТҲ СУРAСИ 1-ОЯТДАН  ҚАМАР СУРAСИ 55-ОЯТГАЧА | "
                "Қуръон билан танишув \n22-СУҲБАТ"
                "\n\n<a href='https://youtu.be/e3142wneOhM'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "23-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC2GI_SwhcOZonmEivoNCrPDhxAj4-AALzDAACvbvJSH0e3JI87WXVIwQ",
        caption="🟢 РАҲМОН СУРAСИ 1-ОЯТДАН  СОФФ СУРAСИ 14-ОЯТГАЧА | "
                "Қуръон билан танишув \n23-СУҲБАТ"
                "\n\n<a href='https://youtu.be/FhgzYJI9m5I'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "24-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC2mI_Sw5_JoBX374YTQnEjv_tHVAeAAL0DAACvbvJSCB4fAoVsEblIwQ",
        caption="🟢 ЖУМА СУРAСИ 1-ОЯТДАН  НУҲ СУРAСИ 28-ОЯТГАЧА | "
                "Қуръон билан танишув \n24-СУҲБАТ"
                "\n\n<a href='https://youtu.be/CIutknQqP7Y'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "25-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC3GI_SxQKiuqfxNT-a2d3etaqccf8AAL4DAACvbvJSL67oOZ5cn22IwQ",
        caption="🟢 ЖИН СУРAСИ 1-ОЯТДАН ИНШИҚОҚ СУРAСИ 24-ОЯТГАЧА  | "
                "Қуръон билан танишув \n25-СУҲБАТ"
                "\n\n<a href='https://youtu.be/oMLf4r4S45c'> Youtube орқали кўриш</a>")

@dp.message_handler(text = "26-суҳбат", state="qbt2")
async def tanishuv_suhbat(msg: types.Message):
    await msg.answer_video(
        video="BAACAgIAAxkBAAIC3mI_SxqSP8QIYcQdiTL2cgTupo3rAAMNAAK9u8lIUc37HcKCVzYjBA",
        caption="🟢 БУРУЖ СУРAСИ 1-ОЯТДАН АН-НОС СУРAСИ 6-ОЯТГАЧА  | "
                "Қуръон билан танишув \n26-СУҲБАТ"
                "\n\n<a href='https://youtu.be/h8elqivC-Qw'> Youtube орқали кўриш</a>")
 
# AUDIO HANDLER

@dp.message_handler(text = "🎧 Аудио", state="qbt1")
async def tanishuv_audio(msg: types.Message, state:FSMContext):
    await msg.answer("Суҳбатларни аудио шаклини танладингиз.", reply_markup=tanishuv_aud_keys)
    await state.set_state("qbt3")

@dp.message_handler(text = "⏮ Oлдинги", state="qbt3")
async def audio_video(msg: types.Message, state:FSMContext):
    await msg.answer("Қуръон билан танишув\" суҳбатлари 26 та суҳбатдан иборат",
                     reply_markup=tanishuv_aud_vid_keys)
    await state.set_state("qbt1")

@dp.message_handler(text = "1-5 суҳбатлар", state="qbt3")
async def tanishuv_audio(msg: types.Message):
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMRGJDgL-MfI1Iys8frmsAAURUpsWL4gACFRIAAiosgEjAn0t2j6PCJiME",
        caption="ФОТИҲА СУРАСИ 1-ОЯТДАН БАҚАРА СУРАСИ 167-ОЯТГАЧА | "
                "Қуръон билан танишув | 1-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMRmJDgMf8hQrqXURjO9zcJptFraxYAAIWEgACKiyASBgrTQk_mGH2IwQ",
        caption="🟢 БАҚАРА СУРАСИ 168-ОЯТДАН 286-ОЯТГАЧА | "
                "Қуръон билан танишув \n2-Суҳбат")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMSGJDgNAykHYYLk8k0ERPjlOopg7RAAIXEgACKiyASNNgCAQYZhREIwQ",
        caption="🟢 ОЛИ ИМРОН 1-ОЯТДАН 200-ОЯТГАЧА | "
                "Қуръон билан танишув \n3-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMSmJDgNIBoRns5j91xHPuoQh20sp1AAIYEgACKiyASLu_VEoq6j_lIwQ",
        caption="🟢 НИСО СУРАСИ 1-ОЯТДАН 176-ОЯТГАЧА | "
                "Қуръон билан танишув \n4-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMTGJDgNa7S4HgFUyHwMSsFkifYvzcAAIZEgACKiyASLnLGeWSKdI-IwQ",
        caption="🟢 МОИДА СУРАСИ 1-ОЯТДАН 120-ОЯТГАЧА | "
                "Қуръон билан танишув \n5-СУҲБАТ")

@dp.message_handler(text = "6-10 суҳбатлар", state="qbt3")
async def tenishuv_audio(msg: types.Message):
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMTmJDgOJ8Zq2yF7Q7NnCXX7nK8dlYAAIcEgACKiyASKwOVTUO5nzDIwQ",
        caption="🟢 АЪРОФ СУРАСИ 1-ОЯТДАН 206-ОЯТГАЧА | "
                "Қуръон билан танишув \n6-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMUGJDgOZBmZ82SdHeiIvWkXqfEUVzAAIeEgACKiyASA2W5IjTPesDIwQ",
        caption="🟢 АНФОЛ СУРАСИ 1-ОЯТДАН ТАВБА СУРАСИ 71-ОЯТГАЧА | "
                "Қуръон билан танишув \n7-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMUmJDgOzE0gKV8ZQySr-h1AOMiNgnAAIiEgACKiyASCg-01CbR5eYIwQ",
        caption="🟢 ТАВБА СУРАСИ 72-ОЯТДАН ЮНУС СУРАСИ 109-ОЯТГАЧА | "
                "Қуръон билан танишув \n8-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMVGJDgPCzvJpKAAHP41-LGWfNgK_YKgACRRYAAq1c2UgOqN5BHvn51yME",
        caption="🟢 ҲУД СУРАСИ 1-ОЯТДАН ЮСУФ СУРАСИ 111-ОЯТГАЧА (1-ҚИСМ) | "
                "Қуръон билан танишув \n9-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMVmJDgPdmyeJL0DuvuOrHjtVI9BAwAAJHFgACrVzZSEYtVFsXfG2NIwQ",
        caption="🟢 ҲУД СУРАСИ 1-ОЯТДАН ЮСУФ СУРАСИ 111-ОЯТГАЧА  (2-ҚИСМ)  |"
                " Қуръон билан танишув \n9-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMWGJDgPwtrYdUpsizhq3_I5ScOA_AAAIlEgACKiyASCztcJ1TYKnJIwQ",
        caption="🟢 РАЪД СУРАСИ 1-ОЯТДАН НАҲЛ СУРАСИ 50-ОЯТГАЧА | "
                "Қуръон билан танишув \n10-СУҲБАТ")

@dp.message_handler(text = "11-15 суҳбатлар", state="qbt3")
async def tanishuv_audio(msg: types.Message):
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMWmJDgQd9F8FVvF2_7W5rHUE36NxiAAImEgACKiyASIu_o-kzpJMeIwQ",
        caption="🟢 НАҲЛ СУРАСИ 51-ОЯТДАН ИСРО СУРАСИ 111-ОЯТГАЧА | "
                "Қуръон билан танишув \n11-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMXGJDgQ1QxR_eEOXauA-3XPTZ3TLgAAInEgACKiyASECmJmlDZnWvIwQ",
        caption="🟢 КАҲФ СУРАСИ 1-ОЯТДАН МАРЯМ СУРАСИ 98-ОЯТГАЧА  | "
                "Қуръон билан танишув \n12-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMXmJDgRTX8SrUmgSGgLO5RA5ACKz6AAIpEgACKiyASE1HcpyJhWklIwQ",
        caption="🟢 ТОҲA СУРAСИ 1-ОЯТДАН AНБИЁ СУРAСИ 112-ОЯТГАЧА  | "
                "Қуръон билан танишув \n13-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMYGJDgRyMhrVs0i4mIXQSW3s_WiNOAAIqEgACKiyASBrzmR0QAcp8IwQ",
        caption="🟢 ҲАЖ СУРAСИ 1-ОЯТДАН МЎМИНУН СУРAСИ 118-ОЯТГАЧ  | "
                "Қуръон билан танишув \n14-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMYmJDgSP_9YaBcmX29p_4mmGYfZpKAAIrEgACKiyASHaswBRSPjZ6IwQ",
        caption="🟢 НУР СУРAСИ 1-ОЯТДАН ШУЪАРО СУРAСИ 227-ОЯТГАЧА  | "
                "Қуръон билан танишув \n15-СУҲБАТ")

@dp.message_handler(text = "16-20 суҳбатлар", state="qbt3")
async def tanishuv_audio(msg: types.Message):
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMZGJDgU-YDGEOfpiuwRsPYns8QVXvAAIvEgACKiyASLUMbqPpq4uKIwQ",
        caption="🟢 НАМЛ СУРAСИ 1-ОЯТДАН ҚАСАС СУРAСИ 88-ОЯТГАЧА  | "
                "Қуръон билан танишув \n16-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMZmJDgVMPZhLF1HYEc8-ApFLi4FPUAAIwEgACKiyASNjmFo2JwSqOIwQ",
        caption="🟢 АНКАБУТ СУРAСИ 1-ОЯТДАН САЖДА СУРAСИ 30-ОЯТГАЧА | "
                "Қуръон билан танишув \n17-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMaGJDgVwMZi1LSk_AB-eL5pZC7tAwAAIyEgACKiyASPZ1gV0BxtytIwQ",
        caption="🟢 АҲЗОБ СУРAСИ 1-ОЯТДАН ФОТИР СУРAСИ 45-ОЯТГАЧА | "
                "Қуръон билан танишув \n18-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMbGJDgWg5nBH099aoKM9kFIeHx-bnAAI1EgACKiyASErSSUJVJR6mIwQ",
        caption="🟢 ЁСИН СУРAСИ 1-ОЯТДАН ЗУМАР СУРAСИ 75-ОЯТГАЧА | "
                "Қуръон билан танишув \n19-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMbmJDgW29JWMF45gvnWmuIsHOUJh8AAI4EgACKiyASPgjXDLkOiwVIwQ",
        caption="🟢  ҒОФИР СУРAСИ 1-ОЯТДАН ШУРО СУРAСИ 53-ОЯТГАЧА | "
                "Қуръон билан танишув \n20-СУҲБАТ")

@dp.message_handler(text = "21-25 суҳбатлар", state="qbt3")
async def tanishuv_audio(msg: types.Message):
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMcGJDgcC7yIlFH72blfgAAVnxs0epVgACyRMAAiosgEhDeuCW03G7vCME",
        caption="🟢  ЗУҲРУФ СУРAСИ 1-ОЯТДАН  МУҲАММАД СУРAСИ 38-ОЯТГАЧА | "
                "Қуръон билан танишув \n21-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMcmJDgcSxS5fVcyIYGXePIDXGHAhbAAIsGwAChrqJSMwXVTtFKeW3IwQ",
        caption="🟢 ФАТҲ СУРAСИ 1-ОЯТДАН  ҚАМАР СУРAСИ 55-ОЯТГАЧА | "
                "Қуръон билан танишув \n22-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMdGJDgcl2pWMc07E4QJGEqq4EuNp6AAJgFgACrVzZSIeLE9ObiXoIIwQ",
        caption="🟢 РАҲМОН СУРAСИ 1-ОЯТДАН  САФ СУРAСИ 14-ОЯТГАЧА | "
                "Қуръон билан танишув \n23-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAEcvrNkmZFH0GAu8vKnWsOvaAk2H8acvAACIDUAAptIyUg2lUZbPbU0eS8E",
        caption="🟢 ЖУМА СУРAСИ 1-ОЯТДАН  НУҲ СУРAСИ 28-ОЯТГАЧА | "
                "Қуръон билан танишув \n24-СУҲБАТ")
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMeGJDgdNBmHjIHEzRdZu9OXMMmnjMAAJlFgACrVzZSIJvYAjUPzHHIwQ",
        caption="🟢 ЖИН СУРAСИ 1-ОЯТДАН ИНШИҚОҚ СУРAСИ 24-ОЯТГАЧА  | "
                "Қуръон билан танишув \n25-СУҲБАТ")

@dp.message_handler(text = "26-суҳбaт", state="qbt3")
async def tanishuv_audio(msg: types.Message):
    await msg.answer_audio(
        audio="CQACAgIAAxkBAAIMemJDgeClTAwJssLbRjgq8X9mckUoAAJDGwAChrqJSIgY-KGNi7vhIwQ",
        caption="🟢 БУРУЖ СУРAСИ 1-ОЯТДАН АН-НОС СУРAСИ 6-ОЯТГАЧА  | "
                "Қуръон билан танишув \n26-СУҲБАТ")
