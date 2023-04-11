from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from loader import dp, db
from keyboards.default.qurantartil_dk import tartil01_keys

@dp.message_handler(text = "📖 Қуръон тартили")
async def tartil(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIRaWJRXBXlAxpCqlhFE9GFN-CmyGwlAAK-AAO6phFI_1dfaKKXYo8jBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i> \n\n Анонс."
                                       "\n\n<b>Устоз:\nХасанҳон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>",
                               reply_markup=tartil01_keys)

@dp.message_handler(text = "Мyқaддимa")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbh2JgXsTSpS4db4MUSwnfJEu2Gvm9AAJEAAPyOVlI493tiH-ikcEkBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i> \n\n📌 Муқаддима"
                                       "\n\n<b>Устоз:\nХасанҳон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=KBLKx7xJw6U&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=1'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "1-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbs2JgZC-3R5nctjMDwgahNnYM_XfrAAI0AAPQtulJ7nVr9ijtDNgkBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nБиринчи дарс\n\n1. Тартил илмининг асослари.\n\n2. Товуш.\n\n3. Нутқ товушлари.\n\n4. Ундош ва унли товушлар."
                                       "\n\n5. Ҳарф.\n\n6. Овоз ҳақида сўз."
                                       "\n\n<b>Устоз:\nХасанҳон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=g_UN_46JvB0&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=2'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "2-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbtWJgZDYCS09s63Nx552bvk391CUyAAICAQACIX7YSnZXqYRsnXybJAQ",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nИккинчи дарс"
                                       "\n\nАраб алифбоси"
                                       "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=0QhV_vn5xDw&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=3'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "3-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbt2JgZD1QQApIgKwEcSsn3cMnAlABAAIxAAOsBIFL-nj0EeN6e_8kBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nУчинчи дарс"
                                       "\n\n1. Унлилар \n\n2. Ундошлар"
                                       "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=f7QSOU2qMA0&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=4'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "4-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbuWJgZELAXQZm7qUGDw--lrKHtbhaAALTAAOQUHlLouhCM_M04HEkBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nТўртинчи дарс"
                                       "\n\n1. Сукун \n\n2. Алиф ва ҳамза"
                                       "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=psyDMGxB3uM&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=5'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "5-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbu2JgZEoCYwk6xGhPrIhHO8z-ljjUAALUAAOQUHlLdHTn36Rn2t0kBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nБешинчи дарс\n\n1. Махраж ва сифат \n\n2. Махражлар сурати "
                                       "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=K5Nmb6bI1EI&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=6'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "6-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbvWJgZFFgIWw7O_cF_gclSxDk4mL4AALBAANm5eBIzKwCWJUvxdgkBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nОлтинчи дарс"
                                       "\n\n1. Унлиларнинг талаффузи \n\n2. Ҳамза ундоши"
                                       "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=2W_3UKgd0X4&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=7'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "7-дарс")
async def birinchi_anons(message: types.Message):
    await message.answer_video(video="BAACAgIAAxkBAAIbv2JgZFrPqSHc0mhLJsepCxD1fsmIAAKyAAN-i_hILtys4rOaSl0kBA",
                               caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                       "\n\nЕттинчи дарс\n\n1. Рō ва зā ҳарфлари. \n\n2. Рō ундоши. \n\n3. Зā ундоши. "
                                       "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                       "\n\n<a href='https://www.youtube.com/watch?v=FtrnVKkI3Vg&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=8'>Youtube орқали кўриш</a>"
                                       "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                       "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                       "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                       "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "8-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbwWJgZGBwY5W0qZIuP_8Udd7OHKwqAAJhAAObIilJGkZ5v1PfyPEkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nСаккизинчи дарс\n\n1. Мӣм, нӯн ва бā ҳарфлари. \n\n2. Мӣм ундоши. \n\n3. Нӯн ундоши. \n\n4. Бā ундоши. "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=KYBOi_xFUkY&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=9'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "9-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbw2JgZG2pjSApNxkQZa9KSAWuDAFhAAJ-AAOK5ThJc-OlxYKZQ34kBA",
                           caption="<b>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</b>"
                                   "\n\nТўққизинчи дарс\n\n1. Лāм, вāв ва фā ҳарфлари. \n\n2. Лāм ундоши. \n\n3. Вāв ундоши. \n\n4. Фā ундоши. "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=9YA3SyyTiWk&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=10'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "10-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbxWJgZHZa-24OggSSOCKU4hihXB_qAAJEAAOCn3BJ_oI3omncEzUkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎнинчи дарс"
                                   "\n\n1. Қōф, кāф ва ҳā ҳарфлари. \n\n2. Қōф ундоши. \n\n3. Кāф ундоши. \n\n4. Ҳā ундоши. "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=7tNa4Cea5OI&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=11'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "11-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbx2JgZH3HxOLe4MGWLKBGQiARqQ33AAKQAAObB3hJ40W9jWZR7HUkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн биринчи дарс\n\n1. Жӣм, шӣн ва йā ҳарфлари. \n\n2. Жӣм ундоши. \n\n3. Шӣн ундоши. \n\n4. Йā ундоши."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=PO7-yGWSL24&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=12'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "12-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbyWJgZIbjYSOP6kg8wKu_HJAHu_jKAAKJAANiZLhJTimyMpTxHsskBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн иккинчи дарс"
                                   "\n\n1. Сӣн, сōд ва сā ҳарфлари. \n\n2. Сӣн ундоши. \n\n3. Сōд ундоши. \n\n4. Сā ундоши. "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=bLZ-Fi5y7z4&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=13'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "13-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIby2JgZI1cid7ff9hJTiWh5MGj0yESAAJoAAOs7chJB5uSXY_-P8YkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн учинчи дарс\n\n 1. Дāл, тā ва тō ҳарфлари. \n\n2. Дāл ундоши. \n\n3. Тā ундоши. \n\n4. Тō ундоши."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=tjhm3fGkBH0&ab_channel=Quranuz'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "14-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbzWJgZJOE955t3Y6ACfM-LKfPsa38AAKdAAOHAeBJtOQfNMC4wv4kBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн тўртинчи дарс"
                                   "\n\n1. Ъаййн ва ҳ:ā ҳарфлари. \n\n2. Ъаййн ундоши. \n\n3. Ҳ:ā ундоши. "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=p87RBz7HqJ8&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=14'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "15-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIbz2JgZJtzus2C8nQqBnb10ps9cyAGAALLAAMVzPlJiTJ0xw2Cr04kBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн бешинчи дарс"
                                   "\n\n1. Ғоййн ва хō ҳарфлари.\n\n2. Ғоййн ундоши.\n\n3. Хō ундоши.  "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=tChdXITiYQA&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=15'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "16-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb0WJgZKBZGMzTQ55TP6S3qQXi4I1PAAJpAAP1TRBKyRVnhsTaHtgkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн олтинчи дарс"
                                   "\n\n1. Зāл, зō ва зōд ҳарфлари. \n\n2. Зāл ундош. \n\n3. Зō ундоши. \n\n4. Зōд ундоши."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=-OboXVMZNnI&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=16'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "17-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb02JgZKrEUGZPBGiv41Q-uIlxIBuEAALVAANqJBlKUJAseK8CW9IkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн еттинчи дарс"
                                   "\n\nЎхшаш ундошлар"
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=A6hhFSWhvus&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=17'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "18-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb1WJgZLBHrBtSouk8srNgnOE0qIUvAAKDAAPhHmBKb8g1EN8s-zMkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн саккизинчи дарс"
                                   "\n\n1. Чўзиқ унлилар.\n\n2. Кичик мад ҳарфлари. "
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=1QqsCdIn1OQ&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=18'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text="19-дарс")
async def birinchi_anons(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb12JgZLn_i1EcZdT2IWIJYxc6qrRmAAIaAAMbZPFKcxN7WGE3Z-okBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЎн тўққизинчи дарс"
                                   "\n\n1. Ташдид. \n\n2. Танвин. \n\n3. Танвинли ташдид."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=tRvydItsm9E&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=19'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "20-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb2WJgZL8n0yRwVdl8kchACzcOAwABQAACHgAD0UcwSx316Gz4K-ioJAQ",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирманчи дарс"
                                   "\n\n1. Тўгарак тā. \n\n2. Ā унли ифодаси: алфийя вāв ҳамда алфийя йā"
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=GZtc5m2CK68&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=20'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "21-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb22JgZMaK-qgKuub0EzfSNWh6xSgmAAIlAQAC74E5Swm8qEuydEuHJAQ",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирма биринчи дарс"
                                   "\n\n1. Ҳамзанинг ёзилиши. \n\n2. Вақф, ибтидо ва васл."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=hdIl3TQomT4&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=21'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "22-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb3WJgZNUCnba4LQfJbD11DGIYR-FBAAIvAQAC7fxYS9jsvyCJOorKJAQ",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирма иккинчи дарс"
                                   "\n\nМад."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=LHq9ryBbS-w&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=22'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "23-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb32JgZNtJJYmd7ndHOJkyMFKyvwRWAALUAANA6mlLFUEvAAHYEYNCJAQ",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирма учинчи дарс"
                                   "\n\n1. Ёзилса-да, ўқилмайдиган ҳарфлар.\n\n2. Сўз бошида келиб, васлда ўқилмай, ибтидода ўқиладиган ҳарфлар."
                                   "\n\n3. Айирувчи ва боғловчи ҳамза.\n\n4. Сўз охирида келиб, васлда ўқилмай, вақфда ўқиладиган ҳарфлар"
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=1jsFua9tp1k&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=23'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "24-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb4WJgZOEa45szQYFesbjNo1-AzXDbAAJiAANgbpBLlTURzR5LNCUkBA",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирма тўртинчи дарс"
                                   "\n\n1. Умуман ўқилмайдиган ҳарфлар. \n\n2. Аниқлик лāми. \n\n3. Лафзи жалола."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=QMTHqyWyQt4&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=24'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "25-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb42JgZOhnAAGDqqFNhnSj7yMf_DbeKgACjAADxh6wS06RUy6wxzZ-JAQ",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирма бешинчи дарс"
                                   "\n\nВақф."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=q4Cn7DINpck&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=25'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")

@dp.message_handler(text = "26-дарс")
async def tartil02(msg: types.Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIb5WJgZPPsg8zOOAvbjqlJC5llQA5PAAJiAQACjlZJSBYpMGEmPljEJAQ",
                           caption="<i>Қуръони каримни бошидан бирга мукаммал ўрганамиз!</i>"
                                   "\n\nЙигирма олтинчи дарс"
                                   "\n\nКалималар."
                                   "\n\nУстоз: \n<b>Ҳасанхон Яҳё Абдулмажид</b>"
                                   "\n\n<a href='https://www.youtube.com/watch?v=1t076Jc6j40&list=PLE0uv2eFBCH1oEsMx39tvjYw96hNrsDEE&index=26'>Youtube орқали кўриш</a>"
                                   "\n\n<a href='https://www.facebook.com/www.quran.uz'>Facebook</a> | "
                                   "<a href='https://www.instagram.com/quran.uz_/?hl=ru'>Instagram</a> | "
                                   "<a href='https://t.me/quranuz_kanali'>Telegram</a> | "
                                   "<a href='https://www.youtube.com/c/Quranuz/featured'>Youtube</a>")
