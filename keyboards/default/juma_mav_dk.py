from aiogram.types import ReplyKeyboardMarkup

juma_dicta = {"1 - 5 мавъизалар":{"a":[2,3,4,5,6], "v":[7,8,9,10,11]},"6 - 10 мавъизалар":{"a":[7,8,9,10,11],"v":[12,13,14,15,16]},
              "11 - 15 мавъизалар":{"a":[12,13,14,15,16],"v":[17,18,19,20,21]},"16 - 20 мавъизалар":{"a":[17,18,19,20,21],"v":[22,23,24,25,26]},
              "21 - 25 мавъизалар":{"a":[22,23,24,25,26],"v":[27,28,29,30,31]}
              }

juma_abutton = ReplyKeyboardMarkup(row_width=2,
                                   resize_keyboard=True,
                                   one_time_keyboard=True)
juma_abutton.insert("⏮ Олдинги")
juma_abutton.insert("🏡 Бош меню")
for n in juma_dicta.keys():
    juma_abutton.insert(n)