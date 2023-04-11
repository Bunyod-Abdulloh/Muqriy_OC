from aiogram.types import ReplyKeyboardMarkup

xatmona_keys = ReplyKeyboardMarkup(
	row_width=2,
	resize_keyboard=True
)

xatmona_keys.insert("📊 Жорий ҳолат")
xatmona_keys.insert("👥 Фойдаланувчилар сони")
xatmona_keys.insert("🔓 Хатм вақтини очиш")
xatmona_keys.insert("🔒 Хатм вақтини ёпиш")
xatmona_keys.insert("🧮 Сарҳисоб")
xatmona_keys.insert("❎ Қайтариш админ")
xatmona_keys.insert("📢 Эълон жўнатиш")
xatmona_keys.insert("🏡 Бош меню")

adm_adm = ReplyKeyboardMarkup(
	row_width=2,
	resize_keyboard=True
)

adm_adm.insert("users")
adm_adm.add("Forward ON")
adm_adm.insert("Forward OFF")
adm_adm.insert("MediaGroup ON")
adm_adm.insert("MediaGroup OFF")
adm_adm.insert("ID ON")
adm_adm.insert("ID OFF")
adm_adm.insert("Sending messages")
adm_adm.insert("Cancel sending messages")
adm_adm.insert("🏡 Бош меню")