from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command, Text

from loader import dp
from states.data import Iqro
from keyboards.default.iqro_dk import iqro_keys
from keyboards.default.start_dk import main_keyboard

iqro_dict = {1:{'v':'BAACAgIAAxkBAAEDwehinNv9VQHYW_JKHJByJrTqzN3ipQACsgIAApzS2Ur8yrtog_6XziQE','c':'"Иқро" кўрсатувининг 1-сони: Кириш.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},2:{'v':'BAACAgIAAxkBAAEDwe9inNwse_h950ti-hq9e1NyeSj_4gACOgMAAlmmIEuqnYWBcS25jiQE','d':'BQACAgIAAxkBAAEDwfdinNwvBDvu8VO7-wx8TSyw6C9_HwAC8gIAAskrmEjL794m3-xJuiQE','c':'"Иқро" кўрсатувининг 2-сони: 1-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},3:{'v':'BAACAgIAAxkBAAEDwhFinNw0buqOV2rr4bQbNAAB1g92PhEAAtgCAAIaMWhLfWg_Xl4euBskBA','d':'BQACAgIAAxkBAAEDwh9inNw3J1F3phFx2VrnOGZ81OxxlwACVwMAAq2DkEhlYHxxSQOPeCQE','c':'"Иқро" кўрсатувининг 3-сони: 2-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},4:{'v':'BAACAgIAAxkBAAEDwjNinNw7NQZMVDM18ChRwaKlRD86tgACjwIAAjewkUu5G0dNwoINaSQE','d':'BQACAgIAAxkBAAEDwjdinNw-2ViIJMS-U_dcCITmPrY86QACRwMAAt57kEsIYXx4SRKo2yQE','c':'"Иқро" кўрсатувининг 4-сони: 3-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},5:{'v':'BAACAgIAAxkBAAEDwk1inNxCbBP-jxctRA21jXpu9dzI9AAC1gMAAnqawUsvfGrpv5FbECQE','d':'BQACAgIAAxkBAAEDwllinNxF0mrN2yc5xDYtLh_ULlAAAWcAAvMCAAIETbhLHaVu3YEtn1AkBA','c':'"Иқро" кўрсатувининг 5-сони: 4-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},6:{'v':'BAACAgIAAxkBAAEDwm9inNxQR0fMdrhjDgE9jVE6oGrcagACbwMAAikyCEjrkq7aQLGk3yQE','d':'BQACAgIAAxkBAAEDwntinNxTNLUju8FanY13qQ3EWDwyYAACwgQAAiLjCEjPILF74mjtHyQE','c':'"Иқро" кўрсатувининг 6-сони: 5-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},7:{'v':'BAACAgIAAxkBAAEDwn9inNxY679meEIgsRPS7Dt1cweuWwACNgQAApkzKEj6DCNtTxXhjyQE','d':'BQACAgIAAxkBAAEDwoFinNxb_9JvVUyP92SygkyqECRLhgACXwMAAjydKEgOTsLZ7r7ZXCQE','c':'"Иқро" кўрсатувининг 7-сони: 6-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},8:{'v':'BAACAgIAAxkBAAEDwpVinNxhcBOeFUz2IePRPSxfgj6cYgACbQQAAv8AAUhI8KYL9LyDbVMkBA','d':'BQACAgIAAxkBAAEDwqJinNxka3sbvwTkASppdtn82pUmUAAC7AIAAgWhSEgMMRxShkNoTSQE','c':'"Иқро" кўрсатувининг 8-сони: 7-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},9:{'v':'BAACAgIAAxkBAAEDwrBinNxp4ysyDoPnd_MQEpjM5ExhGgACEAUAAgfCcEjjP8gb67RKcCQE','d':'BQACAgIAAxkBAAEDwrlinNxs16wYfejr0PFGm86pQ8oPcgACHQUAAgfCcEimEBJgLmNeJyQE','c':'"Иқро" кўрсатувининг 9-сони: 8-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},10:{'v':'BAACAgIAAxkBAAEDwudinNx-n1xXMy8rT5MIv9VPUehCDgAC_wIAAr8LoUgdkBZb-ND6viQE','d':'BQACAgIAAxkBAAEDwvpinNyCXnd2nmM5H5YV9p-f-JoS0wACHgUAAoIcmEgeuMJWtDHppSQE','c':'"Иқро" кўрсатувининг 10-сони: 9-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},11:{'v':'BAACAgIAAxkBAAEDwv1inNyGJYLiQSfe3S6Oh5J_EiFl_gACTQMAAsmm8EiTE7YuxZQ3YCQE','d':'BQACAgIAAxkBAAEDwwFinNyOGz0dePeBuCuesg7mDjubDwACfAQAAs236Uizv2uDNNU3OyQE','c':'"Иқро" кўрсатувининг 11-сони: 10-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},12:{'v':'BAACAgIAAxkBAAEDwwZinNySiRJZDh0youG2KXmJD3p_ewACDwMAAooAATBJ2nGxofYZ9qskBA','d':'BQACAgIAAxkBAAEDwwhinNyVznXFfFKuzhFL3_XX60GQ1wACxQMAAoR4KEmCRHAhTCFpkyQE','c':'"Иқро" кўрсатувининг 12-сони: 11-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},13:{'v':'BAACAgIAAxkBAAEDwwpinNyZ-WEKwNy6940BFjivUVSTywACLgQAApInyEldQHyLZuEsMSQE','d':'BQACAgIAAxkBAAEDwwxinNyco7nrM9kjBs3Y3M2RbP9pQQAC1wMAAn570ElbdSSzSiIp5yQE','c':'"Иқро" кўрсатувининг 13-сони: 12-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},14:{'v':'BAACAgIAAxkBAAEDww5inNygEvdcZ4Owkvba4411ff-lKwACPwMAAgpj6EkOSXj8E3pKeyQE','d':'BQACAgIAAxkBAAEDwxBinNyjNMYqI3xWLzOM--v-Jj-XEwACugMAAlZd4UlV3d3yrV7bpCQE','c':'"Иқро" кўрсатувининг 14-сони: 13-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},15:{'v':'BAACAgIAAxkBAAEDwxJinNynJpQ5lBrsMFYs8gO0wTKxhAAC3wMAAhe9KUqmmaiLDedVsyQE','d':'BQACAgIAAxkBAAEDwxRinNypsgN85NdQbq21z2-8Kd6rfwACZAMAAuMQKUrJEgLSdR50ASQE','c':'"Иқро" кўрсатувининг 15-сони: 14-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},16:{'v':'BAACAgIAAxkBAAEDwxZinNytP89ync817sjdWwnIdDS1LgACJwQAAjmYoUq1G7g1RX_ROSQE','d':'BQACAgIAAxkBAAEDwxpinNywV1-vjJ4w3P583elbBRz9cQACCQQAAnRCoEp3TFHbXdqNAiQE','c':'"Иқро" кўрсатувининг 16-сони: 15-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},17:{'v':'BAACAgIAAxkBAAEDwx9inNy0K5Q4jkQC-GmS30I1byfq1gACBAUAAlGXIUnYnQiRCJph1yQE','d':'BQACAgIAAxkBAAEDwyFinNy3VsTxOwg5XSdcKp58o2VBegACRwQAAl86IUmixuCWfXNNqiQE','c':'«Иқро» кўрсатувининг 17-сони: 16-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},18:{'v':'BAACAgIAAxkBAAEDwydinNy-KDPsEL3UMKWcPFs74bcfOgACLQUAAjTwQEmjb5gDkD5t3CQE','d':'BQACAgIAAxkBAAEDwylinNzC4rNDLtWAxKv-usGjnO_cxAACDgUAAmgtQEknbA2-EyFAByQE','c':'«Иқро» кўрсатувининг 18-сони: 17-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},19:{'v':'BAACAgIAAxkBAAEDwytinNzGsf6Lk38tiCme4EFxrYptjwACRwQAAjZAaUm0Se6U3i_ZmCQE','d':'BQACAgIAAxkBAAEDwy1inNzJCe9ouPbVId6hiqo_zbyL5wACbQQAAu6zaUmJ7ObaCl0lEiQE','c':'«Иқро» кўрсатувининг 19-сони: 18-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},20:{'v':'BAACAgIAAxkBAAEDwy9inNzN7hcQYHYy1nW3Ai-nAAFwgY4AAoAEAAKICGFKEdb-xn15Dw4kBA','d':'BQACAgIAAxkBAAEDwzFinNzPfpdj7zlJuYGMSW0jONLgDQAC5AUAAiGiYUoFWopUgRun0iQE','c':'«Иқро» кўрсатувининг 20-сони: 19-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},21:{'v':'BAACAgIAAxkBAAEDwzNinNzUAhKNLA1uoIXjigbmacFy1AACzQQAAg1XoUp8zfJrnDDxAiQE','d':'BQACAgIAAxkBAAEDwzVinNzWjp6nCVyZ3OzQ3VHuMC5IAgACwQQAAiQRqUoiu33bwLjUzSQE','c':'«Иқро» кўрсатувининг 21-сони: 20-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'},22:{'v':'BAACAgIAAxkBAAEDwzdinNzaYZPLq1h4fnLXHO65FNhORgACNAQAAlbZ8UoO44eGEas4wCQE','d':'BQACAgIAAxkBAAEDwzlinNziGsFeJ3NGn-qzWf7PXCQ0pgACjgMAAvsh-UqJ_sbhzT7lPCQE','c':'«Иқро» кўрсатувининг 22-сони: 21-дарс.\n\n<a href=\'https://www.facebook.com/azontv/\'>Facebook</a> | <a href=\'https://www.instagram.com/azonuztv/\'>Instagram</a> | <a href=\'https://t.me/joinchat/AAAAAFMZ2VS3jQPMCQJ0uQ\'>Telegram</a> | <a href=\'https://www.youtube.com/channel/UCneJYS2Xf_a2a1ealwZb7mQ\'>Youtube</a>'}}

@dp.message_handler(text="🗞 Иқро")
async def iqrohands(msg: types.Message):
    await msg.answer("🗞 Иқро", reply_markup=iqro_keys)
    await Iqro.a.set()

@dp.message_handler(text="1-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[1]['v'], caption=iqro_dict[1]['c'])

@dp.message_handler(text="2-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[2]['v'], caption=iqro_dict[2]['c'])
    await msg.answer_document(document=iqro_dict[2]['d'])

@dp.message_handler(text="3-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[3]['v'], caption=iqro_dict[3]['c'])
    await msg.answer_document(document=iqro_dict[3]['d'])
    

@dp.message_handler(text="4-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[4]['v'], caption=iqro_dict[4]['c'])
    await msg.answer_document(document=iqro_dict[4]['d'])
    

@dp.message_handler(text="5-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[5]['v'], caption=iqro_dict[5]['c'])
    await msg.answer_document(document=iqro_dict[5]['d'])
    

@dp.message_handler(text="6-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[6]['v'], caption=iqro_dict[6]['c'])
    await msg.answer_document(document=iqro_dict[6]['d'])
    

@dp.message_handler(text="7-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[7]['v'], caption=iqro_dict[7]['c'])
    await msg.answer_document(document=iqro_dict[7]['d'])
    

@dp.message_handler(text="8-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[8]['v'], caption=iqro_dict[8]['c'])
    await msg.answer_document(document=iqro_dict[8]['d'])
    

@dp.message_handler(text="9-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[9]['v'], caption=iqro_dict[9]['c'])
    await msg.answer_document(document=iqro_dict[9]['d'])
    

@dp.message_handler(text="10-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[10]['v'], caption=iqro_dict[10]['c'])
    await msg.answer_document(document=iqro_dict[10]['d'])
    

@dp.message_handler(text="11-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[11]['v'], caption=iqro_dict[11]['c'])
    await msg.answer_document(document=iqro_dict[11]['d'])
    

@dp.message_handler(text="12-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[12]['v'], caption=iqro_dict[12]['c'])
    await msg.answer_document(document=iqro_dict[12]['d'])
    

@dp.message_handler(text="13-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[13]['v'], caption=iqro_dict[13]['c'])
    await msg.answer_document(document=iqro_dict[13]['d'])
    

@dp.message_handler(text="14-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[14]['v'], caption=iqro_dict[14]['c'])
    await msg.answer_document(document=iqro_dict[14]['d'])
    

@dp.message_handler(text="15-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[15]['v'], caption=iqro_dict[15]['c'])
    await msg.answer_document(document=iqro_dict[3]['d'])
    

@dp.message_handler(text="16-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[16]['v'], caption=iqro_dict[16]['c'])
    await msg.answer_document(document=iqro_dict[16]['d'])
    

@dp.message_handler(text="17-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[17]['v'], caption=iqro_dict[17]['c'])
    await msg.answer_document(document=iqro_dict[17]['d'])
    

@dp.message_handler(text="18-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[18]['v'], caption=iqro_dict[18]['c'])
    await msg.answer_document(document=iqro_dict[18]['d'])
    

@dp.message_handler(text="19-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[19]['v'], caption=iqro_dict[19]['c'])
    await msg.answer_document(document=iqro_dict[19]['d'])
    

@dp.message_handler(text="20-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[20]['v'], caption=iqro_dict[20]['c'])
    await msg.answer_document(document=iqro_dict[20]['d'])
    

@dp.message_handler(text="21-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[21]['v'], caption=iqro_dict[21]['c'])
    await msg.answer_document(document=iqro_dict[21]['d'])
    

@dp.message_handler(text="22-сон", state=Iqro.a)
async def iqrohands(msg: types.Message, state:FSMContext):
    await msg.answer_video(video=iqro_dict[22]['v'], caption=iqro_dict[22]['c'])
    await msg.answer_document(document=iqro_dict[22]['d'])