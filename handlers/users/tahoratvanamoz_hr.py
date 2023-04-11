from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.default.tahoratvanamoz_dk import na
from keyboards.default.start_dk import main_keyboard

@dp.message_handler(text="⏳ Таҳорат ва намоз")
async def tahoratvanamoz_hand(msg: types.Message, state:FSMContext):
	await msg.answer("⏳ Таҳорат ва намоз", reply_markup=na)
	await state.set_state("na")

@dp.message_handler(text="Таҳорат", state="na")
async def tahoratvanamoz_hand(msg: types.Message):
	await msg.answer("Таҳорат олиш тартиби. \n\nhttps://telegra.ph/tahorat-11-11")
@dp.message_handler(text="Биринчи ракъат. Ният", state="na")
async def na_func(msg: types.Message):
	await msg.answer("<b>Эркаклар намози.\nНият.</b>")
	await msg.answer_photo(photo="AgACAgIAAxkBAAEDcpJilOTIsyZ6vG0oXgJrskjqInGMwQAClLIxG1BaAUmfAau8cTjqlgEAAwIAA3kAAyQE",
                           caption="Намоз вақти киргач, таҳорат ва пок кийим билан пок жойда туриб, қиблага юзланамиз"
                                   "ва ният қиламиз.\n\n<b>Масалан: <i>\"Холис Аллоҳ учун бомдод намозининг икки ракъат фарзини ўқишга ният қилдим\"</i></b> "
                                   "\n\nдеган мазмунда ният қиламиз. Имомга иқтидо қилган киши: \n\n<b><i>\"шу имомга иқтидо қилиб\"</i></b>"
                                   "\n\nжумласини қўшиб ният қилади. Ниятни пичирлаб, тилда ҳам айтиш мумкин, ичида айтиш ҳам мумкин.")
	
@dp.message_handler(text="Такбири таҳрима", state="na")
async def namozkb(msg: types.Message):
	await msg.answer("Такбири таҳрима")
	await msg.answer_animation(animation="CgACAgIAAxkBAAEDcqNilOf-bZLcNgyJb1mySjg6gGQuwAAC8AYAAlBaAUnG2zvAb3PTAyQE",
	                           caption="\"Аллоҳу акбар.\" \nАллоҳ буюкдир.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDcqVilOgE9FgBm5anAAFrWh0cHC_N1FgAAk0GAALm8yFJoLa9mnEYQxckBA")

@dp.message_handler(text="Қиём", state="na")
async def tahoratvanamoz_hand(msg: types.Message):
	await msg.answer("Қиём.")
	await msg.answer_photo(photo="AgACAgIAAxkBAAEDctRilOwzkJy8OvTVyyBOgboriied6QACmrIxG1BaAUkkzt1JuBJ2eQEAAwIAA3kAAyQE",
	                       caption="<b>\"Сано дуоси\"</b>\n\nАгар имомга иқтидо қилган бўлсак, \"сано\"дан "
	                               "бошқа нарсани айтмаймиз. \n\nСўнгра ичимизда <b><i>\"Аъзу биллаҳи минаш шайтонир "
	                               "рожийм. Бисмиллаҳир роҳманир роҳийм\"</i></b>ни айтамиз. \n\nбир ўзимиз ўқиётган бўлсак, "
	                               "Фотиҳа сурасини ўқиймиз. Кейин ичимизда <b>\"Омийн\"</b> деймиз.\n\nСуннат, нафл, "
	                               "вожиб намозларнинг ҳар ракъатида, фарз намозларининг эса, биринчи ва иккинчи ракъатларида"
	                               " Фотиҳа сурасидан кейин зам сураси, яъни бирор сура ёки узунроқ оят ёки камида учта қисқа оят ўқилади."
	                               " \n\nФарз намозларининг учинчи ва тўртинчи ракъатларида Фотиҳа сурасидан сўнг зам сура ўқилмасдан такбир айтиб "
	                               "рукуъга борилади. ")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDcs5ilOv-o8uiW8qUhkygApF6pNDZdgACSAYAAubzIUm99IbF3SuLqiQE",
	                       caption="<b>\"Субҳана каллоҳумма ва биҳамдика, ва табарокасмука, ва тааъла жаддука"
	                               " ва лаа илааҳа ғойрук\"</b>. \n\nМаъноси: <b>Аллоҳим! Сени поклаб ҳамдинг билан ёд этаман. "
	                               "Сенинг номинг табаррукдир, кибриёинг улуғдир. Сендан ўзга илоҳ йўқдир</b>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDctBilOwDh1Us7Y7kXjPkXIhDa7vNQAACRgYAAubzIUkbsIBW2wgHqyQE",
	                       caption="<b>Аъзу биллаҳи минаш шайтонир рожийм. Бисмиллаҳир роҳманир роҳийм.</b>"
	                               "\n\nМаъноси: <b>Қувилган шайтон ёмонлигидан Аллоҳнинг паноҳини сўрайман."
	                               " Роҳман ва Роҳийм Аллоҳнинг номи ила (бошлайман)</b>. \n\n<b><i>"
	                               "Фотиҳа сураси</i> \n\nАлҳамду лиллаҳи Роббил ъааламийн.\nАр-роҳмаанир роҳийм."
	                               "\nМаалики явмид-дийн.\nИййаака наъбуду ва иййаака настаъийн.\nИҳдинас-сироотол "
	                               "мустақийм.\nСироотол-лазийна анъамта ъалайҳим ғойрил мағдууби "
	                               "ъалайҳим валад-дооллийн.</b>\n\nМаъно таржимаси:\n\n<b>Ҳамд оламларнинг Робби - Аллоҳгадир"
	                               "\nУ Роҳман ва Роҳиймдир. \nЖазо-мукофот кунининг эгасидир."
	                               "\nФақат Сенгагина ибодат қиламиз ва фақат Сендангина ёрдам сўраймиз."
	                               "\nБизни тўғри йўлга ҳидоят қилгин.\nЎзинг неъмат берганларнинг йўлига: "
	                               "ғазабга қолганларникига ҳам эмас, адашганларникига ҳам эмас.</b>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDctJilOwJFgEffj4v0Blcm8pQ-0tNMwACQwYAAubzIUnFhPL9KoHueiQE",
	                       caption="<b>Зам сура. Ихлос сураси.</b>"
	                               "\n\n<b>Бисмиллаҳир роҳманир роҳийм."
	                               "\n\n1. Қул ҳуваллоҳу аҳад."
	                               "\n2. Аллоҳус сомад."
	                               "\n3. Лам ялид  ва лам ювлад."
	                               "\n4. Валам якуллаҳу куфуван аҳад.</b>"
	                               "\n\nМаъно таржимаси:"
	                               "\n\n<b>Меҳрибон ва раҳмли Аллоҳнинг номи ила бошлайман."
	                               "\n1. Айт: «У Аллоҳ ягонадир»."
	                               "\n2. Аллоҳ - сомаддир."
	                               "\n3. У туғмаган ва туғилмаган."
	                               "\n4. Ва Унга ҳеч ким тенг бўлмаган.</b>")

@dp.message_handler(text = "Рукуъ", state="na")
async def namoz(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtBBim5EgRZehb4b6kyoWYIdY0ANtrwAC8gYAAlBaAUlxxaYBjZgB3CQE",
	                           caption="<b>Рукуъ</b>"
	                                   "\n\nФотиҳа ёки зам сурадан кейин такбир айтиб, рукуъга эгиламиз. Рукуъда болдирлар "
	                                   "тик туради, икки қўл билан тиззаларни чангаллаб турамиз, тиззани букмаймиз, "
	                                   "бошни эгмаймиз. Орқамиз ҳам текис туриши керак. Шу ҳолатда камида уч марта "
	                                   "<b>\"Субҳаана Роббиял азийм\"</b> деймиз.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtCNim5ITasxyUmobr_w6Q8DRh1DE5QACQQYAAubzIUm8xkUwKWlycCQE",
	                       caption="<b>Субҳаана Роббиял азийм.</b>\n\nМаъноси: \n\n<b>Улуғ Роббим нуқсонлардан покдир.</b>")

@dp.message_handler(text = "Рукуъдан туриш", state="na")
async def namoz(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtE9im5UAAfaMOgwHfcENGhoTJk70EMQAAnAHAAJQWgFJNDWqVxX5vAYkBA",
	                           caption="<b>Рукуъдан туриш</b>"
	                                   "\n\nНамозни ёлғиз ўқиётган бўлсак, <b>\"Самиъаллоҳу лиман ҳамидаҳ\"</b> деб, "
	                                   "қаддимизни тиклаймиз ва <b>\"Роббанаа лакал ҳамд\"</b> деймиз. Жамоат намозида "
	                                   "эса имом <b>\"Самиъаллоҳу лиман ҳамидаҳ\"</b> деса, иқтидо қилганлар "
	                                   "ичида <b>\"Роббанаа, лакал ҳамд\"</b> дейди. \n\nҚаддимизни тўлиқ тиклаб, "
	                                   "тик туриб олгач, такбир айтиб, саждага кетамиз.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtFFim5UD9W0aqi0QqSffewVOJBPxvQACQAYAAubzIUnPbPC89yn78SQE",
	                       caption="<b>Самиъаллоҳу лиман ҳамидаҳ</b> \n\nМаъноси:\n\n<b>Ким ҳамд айтса Аллоҳ "
	                               "уни эшитади.</b>")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtFVim5UJmBZl839-sVvUsgWt11IUMgACPQYAAubzIUn3hn-3QERVHSQE",
	                       caption="<b>Роббанаа, лакал ҳамд</b>\n\nМаъноси:\n\n<b>Роббимиз, Сенга ҳамд "
	                               "бўлсин.</b>")

@dp.message_handler(text = "Cажда", state="na")
async def namoz(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtINim5Z09P2la0mO96G-UnwUl613IgACeQcAAlBaAUkilqGz_SgZNSQE",
	                           caption="<b>Сажда</b>"
	                                   "\n\nҚаддимизни тўлиқ тиклаб, тик туриб олгач, <b>\"Аллоҳу акбар\"</b> деб "
	                                   "саждага кетамиз. Саждага бораётганида аввал тиззани, кейин қўлни ерга қўямиз, "
	                                   "кейин эса икки қўлнинг орасига бошимизни қўямиз. Саждада турганда қўлнинг "
	                                   "бармоқлари қиблага қараб туриши керак. Пешона билан бурунни ерга текказамиз, "
	                                   "қўлтиқларимиз очилиб туради, қорин сонга тегмай туради. Оёқ бармоқлари ҳам "
	                                   "қиблага қараб туради. Шу ҳолатда камида уч марта <b>\"Субҳаана роббиял аъла\"</b> "
	                                   "деймиз.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtIVim5Z3Omi_5xhRRw3lj72Viu0QmQACPAYAAubzIUkSFruFHb1H1iQE",
	                       caption="<b>Субҳаана роббиял аъла.</b>\n\nМаъноси: \n\n<b>Олий Роббим "
	                               "нуқсонлардан покдир.</b>")

@dp.message_handler(text = "Жалса - саждадан туриш", state="na")
async def namoz(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtKlim5qGFWio3Y7uHevQC7awEFbJFAACzAcAAlBaCUlXQ0CTKf10KyQE",
	                           caption="<b>Жалса - саждадан туриш</b>"
	                                   "\n\nКейин <b>\"Аллоҳу акбар\"</b> деб, саждадан бошимизни кўтариб, хотиржамлик "
	                                   "билан чап оёқ устига ўтириб, ўнг оёқнинг бармоқларини қиблага қаратиб ўтирамиз. "
	                                   "Икки қўлимиз икки тиззанинг устида бўлади.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtKtim5qJkWGoV0tCyO8brPSnX7OYwgACOwYAAubzIUnu-aHToq34NCQE")

@dp.message_handler(text = "Caждa", state="na")
async def namoz(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtQVim5wVe3TGuhoDdd9-ixrTEkngGwACzwcAAlBaCUlGhHROFfsaUyQE",
	                           caption="<b>Сажда</b>"
	                                   "\n\nКейин такбир айтиб, иккинчи саждага борамиз ва камида уч марта "
	                                   "<b>\"Субҳаана роббиял аъла\"</b> деймиз.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtQdim5wYOgZh71GGuAsstRV-03KxugACOgYAAubzIUmAIhgtQQJNVSQE",
	                       caption="<b>Субҳаана роббиял аъла.</b>\n\nМаъноси:\n\n<b>Олий Роббим нуқсонлардан покдир.</b>")
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtQFim5vtXB4PtHf0s3HBignC1qyfiQAC1AcAAlBaCUn2ioDMw7vgeSQE",
	                           caption="<b>Қиём</b>"
	                                   "\n\nЯна такбир айтиб, кейинги ракъатга турамиз. Саждадан туришда аввал бошни, "
	                                   "кейин қўлларни, кейин тиззани кўтарамиз.")

@dp.message_handler(text = "Иккинчи ракъат", state="na")
async def n_ah(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtQlim5yKYwElJA0lSyMD4qJQxfbhNQAC2gcAAlBaCUlSBLpy9hZ43SQE",
	                           caption="<b>Иккинчи ракъат</b>"
	                                   "\n\nИккинчи ракъат ҳам худди биринчи ракъатга ўхшаб ўқилади. Фақат бошида такбири "
	                                   "таҳрима, сано ва \"аъузу\" айтилмайди. Фотиҳани ўқиб, сўнг зам сурани ўқиб, такбир "
	                                   "айтиб рукуъга эгиламиз. Кейин туриб, такбир айтиб, икки марта сажда қиламиз.")

@dp.message_handler(text = "Қаъда", state="na")
async def namoz(msg: types.Message):
	await msg.answer_photo(photo = "AgACAgIAAxkBAAEDtTdim55beT5NtyaRgMy8PjF47ON0wAACIK4xG1BaEUmhFiRLl8U58QEAAwIAA3gAAyQE",
	                           caption="<b>Қаъда</b>"
	                                   "\n\nИккинчи ракатнинг иккинчи саждасини қилиб бўлгандан кейин чап оёқ устига "
	                                   "ўтирамиз, ўнг оёқнинг бармоқлари қиблага қараб тураверади. Ўнг қўлни ўнг тизза "
	                                   "устига, чап қўлни чап тизза устига, бармоқларни ёйган ҳолда қўямиз. Кейин ташаҳҳуд ўқийди.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtTlim55erUUGm0ZBXViOsTftuN1OkQACOQYAAubzIUnkUgJhogckYiQE",
	                       caption="<b>\"Аттаҳийяту лиллаҳи ва вассолавату ваттоййибат. Ассаламу ъалайка айюҳан-набийю ва роҳматуллоҳи "
	                               "вабарокатуҳ. Ассаламу ъалайна ва аълаа ибаадиллааҳис солиҳийн. Ашҳаду аллаа илааҳа иллаллоҳу "
	                               "ва ашҳаду анна Муҳаммадан ъабдуҳу ва росулуҳ\".</b>\n\nМаъноси:\n\n<b>«Саломлар Aллоҳ "
	                               "учундир, салавот ва барча гўзал сўзлар ҳам. Эй Набий! Сенга салом, Aллоҳнинг раҳмати ва "
	                               "баракалари бўлсин. Бизларга ва Aллоҳнинг солиҳ бандаларига салом бўлсин. Aллоҳдан ўзга "
	                               "илоҳу маъбуд йўқ деб шаҳодат келтираман. Aлбатта, Муҳаммад Унинг бандаси ва Расули деб "
	                               "шаҳодат келтираман»</b>.")

@dp.message_handler(text = "Салом", state="na")
async def namoz(msg: types.Message):
	await msg.answer_animation(animation = "CgACAgIAAxkBAAEDtw9im_2vXWt8t4FvMSjSA02LRqNu4wAC3wcAAlBaCUmVvEDeASzm1SQE",
	                           caption="<b>Салом</b>"
	                                   "\n\n\"Ассаламу ъалайкум ва роҳматуллоҳ\"")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtwtim_0qlqL1jnUxwAeidOlJBkMexwACLwYAAubzIUkv-SjTEc_iFSQE",
	                       caption="<b>Ассаламу ъалайкум ва роҳматуллоҳ</b>\n\nМаъноси:<b>Сизга тинчлик-омонлик, Аллоҳнинг раҳмати бўлсин!</b>")
	await msg.answer("Агар намоз икки ракъатли бўлса, ташаҳҳуддан кейин салавотларни (\"Аллоҳумма солли...\" ва \"Аллоҳумма барик...\"ларни) "
	                 "ўқиймиз.")
	await msg.answer_audio(audio="CQACAgIAAxkBAAEDtxFim_7QewiiE02vlcsPGvmmSdD1bwACNgYAAubzIUkRD7nPiaqnciQE",
	                       caption="<b>\"Аллоҳумма солли ъалаа Муҳаммадив ва ъалаа али Муҳаммад. Кама соллайта ъалаа Иброҳима ва ъалаа али Иброҳим."
	                               " Иннака ҳамидум мажид. Аллоҳумма барик ъалаа Муҳаммадив ва ъалаа али Муҳаммад. Кама барокта ъалаа Иброҳима ва "
	                               "ъалаа али Иброҳим. Иннака ҳамидум мажид\".</b>\n\nМаъноси: "
	                               "\n\n<b>Аллоҳим Иброҳимга ва Иброҳимнинг аҳли байтларига Ўз раҳматингни нозил қилганингдек, Муҳаммадга ва "
	                               "Муҳаммаднинг оила аъзоларига Ўзингнинг зиёда раҳматларингни нозил қилгин! Албатта, Сен мақталган, улуғланган Зотсан!"
	                               "Аллоҳим! Иброҳимга ва Иброҳимнинг аҳли байтларига Ўз баракангни нозил қилганингдек, Муҳаммадга ва Муҳаммаднинг оила "
	                               "аъзоларига Ўз баракангни нозил қилгин! Албатта, Сен мақталган, улуғланган Зотсан!</b>")
	await msg.answer("Сўнг бошқа дуоларни ўқиб, <b>\"Ассалому алайкум ва роҳматуллоҳи\"</b> деб ўнг ва чап томонларига қараб салом берамиз.")
	await msg.answer("Агар намоз уч ёки тўрт ракъатли бўлса, икки ракъатнинг ташаҳҳудини ўқиб бўлиб, кейин учинчи ракъатга турамиз ва худди иккинчи ракъатга "
	                 "ўхшатиб, намозни давом эттирамиз. Лекин учинчи ва тўртинчи ракъатларда фақат Фотиҳанинг ўзини ўқиймиз, зам сура ўқимаймиз. Тўртинчи "
	                 "ракъатнинг иккинчи саждасидан кейин ўтириб, ташаҳҳуд, саловат ва дуоларни ўқиб, икки томонга салом берамиз.")
