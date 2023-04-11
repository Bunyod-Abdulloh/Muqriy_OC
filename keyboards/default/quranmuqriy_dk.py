from aiogram.types import ReplyKeyboardMarkup

muqriy_list = ["1 - 10 суралар","11 - 20 суралар","21 - 30 суралар","31 - 40 суралар","41 - 50 суралар","51 - 60 суралар",
               "61 - 70 суралар","71 - 80 суралар","81 - 90 суралар","91 - 100 суралар","101 - 114 суралар"]

r01 = list(range(1005,1015))
r02 = list(range(1015,1025))
r03 = list(range(1025,1035))
r04 = list(range(1035,1045))
r05 = list(range(1045,1055))
r06 = list(range(1055,1065))
r07 = list(range(1065,1075))
r08 = list(range(1075,1085))
r09 = list(range(1085,1095))
r010 = list(range(1095,1105))
r011 = list(range(1105,1119))

r_1 = [r01,r02,r03,r04,r05,r06,r07,r08,r09,r010,r011]
muqriy_dict = {}
for i in range(0,len(muqriy_list)):
    muqriy_dict[muqriy_list[i]] = r_1[i]

async def muqriy_dk():
    full = ReplyKeyboardMarkup(row_width=2,
                               resize_keyboard=True,
                               one_time_keyboard=True)
    full.add("🏡 Бош меню")
    full.add("1 - 10 суралар")
    for n in muqriy_list:
        if n == "1 - 10 суралар":
            pass
        else:
            full.insert(n)
    return full