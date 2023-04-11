from loader import bot

async def text_func(call, chat_id, data):
    await call.message.delete()
    matn = data['matn']
    user_id = call.from_user.id
    if call.data == "yes":
        await bot.send_message(chat_id=chat_id,
                               text=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                    f"\n\n{matn}"
                               )
        await call.message.answer(f"Саволингиз юборилди! Жавоб админларимиз томонидан ботни ўзига юборилади!"
                                  )

async def photo_func(call, chat_id, data):
    await call.message.delete()
    rasm = data['rasm']
    caption = data['caption']
    user_id = call.from_user.id

    if call.data == "yes":
        if caption == None:
            await bot.send_photo(chat_id=chat_id,
                                 photo=rasm,
                                 caption=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                 )
        else:
            await bot.send_photo(chat_id=chat_id,
                                 photo=rasm,
                                 caption=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                         f"\n\n{caption}"
                                 )
        await call.message.answer("Саволингиз юборилди! Жавоб админларимиз томонидан ботни ўзига юборилади!")

async def audio_func(call, chat_id, data):
    await call.message.delete()
    audio = data['audio']
    caption = data['caption']
    user_id = call.from_user.id

    if call.data == "yes":
        if caption == None:
            await bot.send_audio(chat_id=chat_id,
                                 audio=audio,
                                 caption=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                 )
        else:
            await bot.send_audio(chat_id=chat_id,
                                 audio=audio,
                                 caption=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                         f"\n\n{caption}"
                                 )
        await call.message.answer("Саволингиз юборилди! Жавоб админларимиз томонидан ботни ўзига юборилади!")

async def video_func(call, chat_id, data):
    await call.message.delete()
    video = data['video']
    caption = data['caption']
    user_id = call.from_user.id

    if call.data == "yes":
        if caption == None:
            await bot.send_video(chat_id=chat_id,
                                 video=video,
                                 caption=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                 )
        else:
            await bot.send_video(chat_id=chat_id,
                                 video=video,
                                 caption=f"#ID{user_id}|<b>савол фойдаланувчи {call.from_user.get_mention(as_html=True)} дан қабул қилинди!</b>"
                                         f"\n\n{caption}"
                                 )
        await call.message.answer("Саволингиз юборилди! Жавоб админларимиз томонидан ботни ўзига юборилади!")