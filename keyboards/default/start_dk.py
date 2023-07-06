from aiogram.types import ReplyKeyboardMarkup


main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_keyboard.row("🎧 \"Қуръони карим\" тиловати \n(ўттиз пора)")
main_keyboard.row("📖 Қуръони карим", "📌 Таровеҳ намози 1444")
main_keyboard.row("🤲 Рамазон - 1443", "📌 Таровеҳ намози 1443")
main_keyboard.row("☪ Қуръон билан танишув", "🗞 Иқро")
main_keyboard.row("🕌 Ўн кеча билан қасам", "📖 Қуръон тартили")
main_keyboard.row("🎧 \"Қуръони карим\" тиловати \n(таълим услубида)")
main_keyboard.row("📑 Мусҳаф истилоҳлари шарҳи", "📖 Қуръон таълими (тавсиялар)")
main_keyboard.row("🕋 Ҳаж - 2022", "📌 Қуръон ила ҳамнафас")
main_keyboard.row("⏳ Таҳорат ва намоз")
main_keyboard.row("☀ Шамоилул Муҳаммадия", "📜 Арбаъин Нававийя шарҳи")
main_keyboard.row("🔆 Мавлид", "📍 Расулуллоҳ ﷺ қадамжолари")
main_keyboard.row("📚 Илмий суҳбатлар", "📌 Жума мавъизалари")
main_keyboard.row("🏜 Миср сафари", "🌏 Ҳамсафар")
main_keyboard.row("📑 Навоийни англаш сари")
main_keyboard.row("📿 Тонгги ва кечки зикрлар", "❓ Савол ва таклифлар")

support_keys = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
support_keys.row('Аёллар', 'Эркаклар')

bosh_menyu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bosh_menyu.row('🏡 Бош меню')
