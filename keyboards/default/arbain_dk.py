from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

arb_vdict = {"Муқаддимa":[264],"Кириш":[265],"Арбаъин ҳақидаги ҳадис":[266],"Арбаъин асари бўйича санад":[267],"1 - 5 ҳадислар":[268,269,270,271,272,273],
             "6 - 10 ҳадислар":[274,275,276,277,278],"11 - 15 ҳадислар":[279,280,281,282,283],"16 - 20 ҳадислар":[284,285,286,287,288],
             "21 - 25 ҳадислар":[289,290,291,292,293],"26 - 30 ҳадислар":[294,295,296,297,298],"31 - 35 ҳадислар":[299,300,301,302,303],"36 - 40 ҳадислар":[305,306]}
arb_adict = {"Муқаддимa":[54],"Кириш":[55],"Арбаъин ҳақидаги ҳадис":[56],"Арбаъин асари бўйича санад":[57],"1 - 5 ҳадислар":[58,59,60,61,62,63],
             "6 - 10 ҳадислар":[64,65,66,67,68],"11 - 15 ҳадислар":[69,70,71,72,73],"16 - 20 ҳадислар":[74,75,76,77,78],
             "21 - 25 ҳадислар":[79,80,81,82,83],"26 - 30 ҳадислар":[84,85,86,87,88],"31 - 35 ҳадислар":[89,90,91,92,93],"36 - 40 ҳадислар":[95,96]}
arb_tdict = {"Кириш":[84,85],"Арбаъин ҳақидаги ҳадис":[86,87],"1 - 5 ҳадислар":[88, 89, 90, 91, 92, 93, 94, 95, 96, 97],
             "6 - 10 ҳадислар":[98, 99, 100, 101, 102, 103, 104, 105, 106, 107],"11 - 15 ҳадислар":[108, 109, 110, 111, 112, 113, 114, 115, 116, 117],
             "16 - 20 ҳадислар":[118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129],"21 - 25 ҳадислар":[130, 131, 132, 133, 134, 135, 136, 137, 138, 139],
             "26 - 30 ҳадислар":[140, 141, 142, 143, 144, 145, 146, 147, 148, 149],"31 - 35 ҳадислар":[150, 151, 152, 153, 154, 155, 156, 157, 158, 159],
             "36 - 40 ҳадислар":[160, 161,162,163,164,165]}

arbain_roviylar_dict = {'1':[12],'2':[13,14],'3':[15,16,17,18,19,20,21,22,23,24],
                        '4':[25,26,27,28,29], '5':[30]}

arbmenyu_kb = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True
)

arbmenyu_kb.add("🏡 Бош меню")
arbmenyu_kb.add("🎧 Ayдио")
arbmenyu_kb.insert("🎬 Bидeо")
arbmenyu_kb.add("📑 Ҳадислар матни ва аудиолари")
arbmenyu_kb.add("📜 Ҳадислар ровийлари")

arbbuttons = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True
)

arbbuttons.add("⏮ Олдинги")
arbbuttons.insert("🏡 Бош меню")

for n in arb_vdict.keys():
    arbbuttons.insert(n)
arbbuttons.insert("36 - 40 ҳадислар")

arbtext = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True
)
arbtext.add("⏮ Олдинги")
arbtext.insert("🏡 Бош меню")

for n in arb_tdict:
    arbtext.insert(n)

arbain_roviylar_buttons = ReplyKeyboardMarkup(
    row_width=4,
    resize_keyboard=True,
    one_time_keyboard=True
)
arbain_roviylar_buttons.insert("⏮ Олдинги")
arbain_roviylar_buttons.insert("🏡 Бош меню")
arbain_roviylar_buttons.add("1")
for n in arbain_roviylar_dict.keys():
    if n == "1":
        pass
    else:
        arbain_roviylar_buttons.insert(n)
