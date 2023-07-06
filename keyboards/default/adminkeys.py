from aiogram.types import ReplyKeyboardMarkup

adm_adm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
adm_adm.add("users")
adm_adm.row("Forward ON", "Forward OFF")
adm_adm.row("MediaGroup ON", "MediaGroup OFF")
adm_adm.row("ID ON", "ID OFF")
adm_adm.row("Sending messages", "Cancel sending messages")
adm_adm.add("Admin qo'shish/o'chirish")
adm_adm.add("🏡 Бош меню")
