

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

suralar_default = 'Суралар'
bosh_menu = '🏡 Бош меню'

suralar_dict = {'fotiha':{'toliq':9,'zip':10,'oyat_soni':7,'sura':'Фотиҳа','audio':{'basmala':35,'1':37,'2':39,'3':41,'4':43,'5':45,'6':47,'7':48},
						  'screen':{'basmala':34,'1':36,'2':38,'3':40,'4':42,'5':44,'6':46,'7':46},'link':'http://tafsirihilol.uz/main/read/30'},
				'fil':{'toliq':173,'zip':174,'oyat_soni':5,'sura':'Фил','audio':{'1':176,'2':178,'3':180,'4':182,'5':184},
					   'screen':{'1':175,'2':177,'3':179,'4':181,'5':183},'link':'http://tafsirihilol.uz/main/read/92'},
				'quraysh':{'toliq':185,'zip': 186,'oyat_soni': 4,'sura':'Қурайш','audio':{'1':188,'2':190,'3':192,'4':194},
						   'screen':{'1': 187, '2': 189, '3': 191, '4': 193},'link':'http://tafsirihilol.uz/main/read/47'},
				'maauun':{'toliq':195,'zip':196,'oyat_soni':7,'sura':'Мааъуун','audio':{'1': 198,'2':200,'3':202,'4':204,'5':206,'6':208,'7': 210},
						  'screen':{'1': 197, '2': 199, '3': 201, '4': 203, '5': 205, '6': 207, '7': 209},'link':'http://tafsirihilol.uz/main/read/40'},
				'kavsar':{'toliq':211,'zip':212,'oyat_soni':3,'sura':'Кавсар','audio':{'1':214,'2':216,'3':218},
						  'screen':{'1':213,'2':215,'3':217},'link':'http://tafsirihilol.uz/main/read/38'},
				'kaafirun':{'toliq':219,'zip':220,'oyat_soni':6,'sura':'Каафирун','audio':{'1':222,'2':224,'3':226,'4':228,'5':230,'6':232},
							'screen':{'1':221,'2':223,'3':225,'4':227,'5':229,'6':231},'link':'http://tafsirihilol.uz/main/read/96'},
				'nasr':{'toliq':233,'zip':234,'oyat_soni':3,'sura':'Наср','audio':{'1':236,'2':238,'3':240},
						'screen':{'1':235,'2':237,'3':239},'link':'http://tafsirihilol.uz/main/read/101'},
				'masad':{'toliq':241,'zip':242,'oyat_soni':5,'sura':'Масад','audio':{'1':244,'2':246,'3':248,'4':250,'5':252},
						 'screen':{'1':243,'2':245,'3':247,'4':249,'5':251},'link':'http://tafsirihilol.uz/main/read/97'},
				'ixlos':{'toliq':253,'zip':254,'oyat_soni':3,'sura':'Ихлос','audio':{'1':256,'2':258,'3':260,'4':262},
						 'screen':{'1':255,'2':257,'3':259,'4':261},'link':'http://tafsirihilol.uz/main/read/50'},
				'falaq':{'toliq':263,'zip':264,'oyat_soni':5,'sura':'Фалақ','audio':{'1':266,'2':268,'3':270,'4':272,'5':274},
						 'screen':{'1':265,'2':267,'3':269,'4':271,'5':273},'link':'http://tafsirihilol.uz/main/read/71'},
				'naas':{'toliq':275,'zip':276,'oyat_soni':6,'sura':'Наас','audio':{'1':278,'2':280,'3':282,'4':284,'5':286,'6':288},
						'screen':{'1':277,'2':279,'3':281,'4':283,'5':285,'6':287},'link':'http://tafsirihilol.uz/main/read/2'}}

suralar_keyboard = InlineKeyboardMarkup(row_width=3)
for k, v in suralar_dict.items():
	suralar_keyboard.insert(InlineKeyboardButton(text=v['sura'],
												 callback_data=k))

suralar_default_keys = ReplyKeyboardMarkup(resize_keyboard=True)
suralar_default_keys.row(suralar_default,bosh_menu)

