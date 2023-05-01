from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

is1_dict = {"Жонли суҳбатлар": "jonli", "Сурхондарё сафари": "surhon", "Тошкент вилояти": "toshvil",
            "Тошкент шаҳри (1-тўплам)": "tosh1", "Тошкент шаҳри (2-тўплам)": "tosh2",
            "Ҳаж ва курбонлик": "hajqurbonlik", "1-тўплам": "birt", "2-тўплам": "ikkit", "3-тўплам": "ucht",
            "4-тўплам": "tortt"}

is2_list = ["1-5 сyҳбатлар", "6-10 сyҳбатлар", "11-15 сyҳбатлар", "16-20 сyҳбатлар",
            "21-25 сyҳбатлар", "26-30 сyҳбатлар", "31-35 сyҳбатлар",
            "36-40 сyҳбатлар", "41-45 сyҳбатлар", "46-52 сyҳбатлар"]

r11 = list(range(772, 777))
r12 = list(range(777, 782))
r13 = list(range(782, 787))
r14 = list(range(787, 792))
r15 = list(range(792, 797))
r16 = list(range(797, 802))
r17 = list(range(802, 807))
r18 = list(range(807, 812))
r19 = list(range(812, 817))
r20 = list(range(817, 824))

r21 = list(range(720, 725))
r22 = list(range(725, 730))
r23 = list(range(730, 735))
r24 = list(range(735, 740))
r25 = list(range(740, 745))
r26 = list(range(745, 750))
r27 = list(range(750, 755))
r28 = list(range(755, 760))
r29 = list(range(760, 765))
r30 = list(range(765, 772))

r_2 = [r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]
r_3 = [r21, r22, r23, r24, r25, r26, r27, r28, r29, r30]

is2_dict = {}
for i in range(0, len(is2_list)):
    is2_dict[is2_list[i]] = r_2[i]

is3_dict = {}
for n in range(0, len(is2_list)):
    is3_dict[is2_list[n]] = r_3[n]


async def is2_dk():
    is_k = ReplyKeyboardMarkup(row_width=2,
                               resize_keyboard=True,
                               one_time_keyboard=True)
    is_k.add("⏮ Олдинги")
    is_k.insert("🏡 Бош меню")
    is_k.add("1-5 сyҳбатлар")
    for n in is2_list:
        if n == "1-5 сyҳбатлар":
            pass
        else:
            is_k.insert(n)
    return is_k


async def is1_dk():
    is1 = ReplyKeyboardMarkup(row_width=2,
                              resize_keyboard=True,
                              one_time_keyboard=True)
    is1.add("🏡 Бош меню"),
    is1.add("Жонли суҳбатлар")
    for n in is1_dict.keys():
        if n == "Жонли суҳбатлар":
            pass
        else:
            is1.insert(n)
    return is1


allk = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏮ Олдинги"),
            KeyboardButton(text="🏡 Бош меню"),
        ],
        [
            KeyboardButton(text="🎧 Ayдиo"),
            KeyboardButton(text="🎬 Видео"),

        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
