from loader import bot

async def text_reply_func(message):
    if message.text:
        _v = message.reply_to_message
        text = _v.text
        user_id = text.split("|")[0][3::]
        user_caption = _v.text.split("дан қабул қилинди!")[-1]
        text_to_send = f"<b>Саволингизга берилган жавоб!</b>" \
                       f"\n\n{message.text}"

        await bot.send_message(
            chat_id=user_id,
            text=f"<b>Сизнинг саволингиз!</b>{user_caption}"
        )
        await bot.send_message(
            chat_id=user_id,
            text=text_to_send
        )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.voice:
        _v = message.reply_to_message
        user_id = _v.text.split("|")[0][3::]
        user_caption = _v.text.split("дан қабул қилинди!")[-1]
        voice_id = message.voice.file_id

        await bot.send_message(
            chat_id=user_id,
            text=f"<b>Сизнинг саволингиз!</b>{user_caption}"
        )
        await bot.send_voice(
            chat_id=user_id,
            voice=voice_id,
            caption="<b>Саволингизга берилган жавоб</b>"
        )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.photo:
        _v = message.reply_to_message
        user_id = _v.text.split("|")[0][3::]
        user_caption = _v.text.split("дан қабул қилинди!")[-1]
        photo_id = message.photo[-1].file_id
        photo_caption = message.caption

        await bot.send_message(
            chat_id=user_id,
            text=f"<b>Сизнинг саволингиз!</b>{user_caption}"
        )
        if photo_caption == None:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{photo_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.audio:
        _v = message.reply_to_message
        user_id = _v.text.split("|")[0][3::]
        user_caption = _v.text.split("дан қабул қилинди!")[-1]
        audio_id = message.audio.file_id
        audio_caption = message.caption

        await bot.send_message(
            chat_id=user_id,
            text=f"<b>Сизнинг саволингиз!</b>{user_caption}"
        )
        if audio_caption == None:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{audio_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.video:
        _v = message.reply_to_message
        user_id = _v.text.split("|")[0][3::]
        user_caption = _v.text.split("дан қабул қилинди!")[-1]
        video_id = message.video.file_id
        video_caption = message.caption

        await bot.send_message(
            chat_id=user_id,
            text=f"<b>Сизнинг саволингиз!</b>{user_caption}"
        )
        if video_caption == None:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{video_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )

async def photo_reply_func(message):
    if message.text:
        _v = message.reply_to_message
        text = _v.caption
        user_id = text.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        photo_id = _v.photo[-1].file_id
        text_to_send = f"<b>Саволингизга берилган жавоб!</b>" \
                       f"\n\n{message.text}"
        await bot.send_photo(
            chat_id=user_id,
            photo=photo_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        await bot.send_message(
            chat_id=user_id,
            text=text_to_send
        )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.photo:
        _v = message.reply_to_message
        text = _v.caption
        user_id = text.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_photo_id = _v.photo[-1].file_id
        photo_id = message.photo[-1].file_id
        caption = message.caption

        await bot.send_photo(
            chat_id=user_id,
            photo=user_photo_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆"
                    f"\n\n<b>Сизнинг саволингиз!</b>"
        )

        if caption == None:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга жавоб!</b>"
            )
        else:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга жавоб!</b>"
                        f"\n\n{caption}"
            )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.voice:
        _v = message.reply_to_message
        text = _v.caption
        user_id = text.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_photo_id = _v.photo[-1].file_id
        voice_id = message.voice.file_id

        await bot.send_photo(
            chat_id=user_id,
            photo=user_photo_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆"
                    f"\n\n<b>Сизнинг саволингиз!</b>"
        )
        await bot.send_voice(
            chat_id=user_id,
            voice=voice_id,
            caption="<b>Саволингизга берилган жавоб</b>"
        )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.audio:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_photo_id = _v.photo[-1].file_id
        audio_id = message.audio.file_id
        audio_caption = message.caption

        await bot.send_photo(
            chat_id=user_id,
            photo=user_photo_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆"
                    f"\n\n<b>Сизнинг саволингиз!</b>"
        )
        if audio_caption == None:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{audio_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.video:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_photo_id = _v.photo[-1].file_id
        video_id = message.video.file_id
        video_caption = message.caption

        await bot.send_photo(
            chat_id=user_id,
            photo=user_photo_id,
            caption=f"<b>Сизнинг саволингиз!</b>{user_caption}"
        )
        if video_caption == None:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{video_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )

async def audio_reply_func(message):
    if message.text:
        _v = message.reply_to_message
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_id = _v.caption.split("|")[0][3::]
        user_audio_id = _v.audio.file_id
        text_to_send = f"<b>Саволингизга берилган жавоб!</b>" \
                       f"\n\n{message.text}"

        await bot.send_audio(
            chat_id=user_id,
            audio=user_audio_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b> "
        )
        await bot.send_message(
            chat_id=user_id,
            text=text_to_send
        )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.photo:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_audio_id = _v.audio.file_id
        photo_id = message.photo[-1].file_id
        caption = message.caption

        await bot.send_audio(
            chat_id=user_id,
            audio=user_audio_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆"
                    f"\n\n<b>Сизнинг саволингиз!</b>"
        )

        if caption == None:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга жавоб!</b>"
            )
        else:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга жавоб!</b>"
                        f"\n\n{caption}"
            )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.voice:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_audio_id = _v.audio.file_id
        voice_id = message.voice.file_id

        await bot.send_audio(
            chat_id=user_id,
            audio=user_audio_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆"
                    f"\n\n<b>Сизнинг саволингиз!</b>"
        )
        await bot.send_voice(
            chat_id=user_id,
            voice=voice_id,
            caption="<b>Саволингизга берилган жавоб</b>"
        )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.audio:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_audio_id = _v.audio.file_id
        audio_id = message.audio.file_id
        audio_caption = message.caption

        await bot.send_audio(
            chat_id=user_id,
            audio=user_audio_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        if audio_caption == None:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{audio_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.video:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_audio_id = _v.audio.file_id
        video_id = message.video.file_id
        video_caption = message.caption

        await bot.send_audio(
            chat_id=user_id,
            audio=user_audio_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        if video_caption == None:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{video_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )

async def video_reply_func(message):
    if message.text:
        _v = message.reply_to_message
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_id = _v.caption.split("|")[0][3::]
        user_video_id = _v.video.file_id
        text_to_send = f"<b>Саволингизга берилган жавоб!</b>" \
                       f"\n\n{message.text}"

        await bot.send_video(
            chat_id=user_id,
            video=user_video_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        await bot.send_message(
            chat_id=user_id,
            text=text_to_send
        )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.photo:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_video_id = _v.video.file_id
        photo_id = message.photo[-1].file_id
        caption = message.caption

        await bot.send_video(
            chat_id=user_id,
            video=user_video_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        if caption == None:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга жавоб!</b>"
            )
        else:
            await bot.send_photo(
                chat_id=user_id,
                photo=photo_id,
                caption=f"<b>Саволингизга жавоб!</b>"
                        f"\n\n{caption}"
            )
        await message.reply(
            text=f"#ID{user_id} жавоб муваффаққиятли юборилди!"
        )
    elif message.voice:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_video_id = _v.video.file_id
        voice_id = message.voice.file_id

        await bot.send_video(
            chat_id=user_id,
            video=user_video_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        await bot.send_voice(
            chat_id=user_id,
            voice=voice_id,
            caption="<b>Саволингизга берилган жавоб</b>"
        )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.audio:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_video_id = _v.video.file_id
        audio_id = message.audio.file_id
        audio_caption = message.caption

        await bot.send_video(
            chat_id=user_id,
            video=user_video_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        if audio_caption == None:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_audio(
                chat_id=user_id,
                audio=audio_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{audio_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )
    elif message.video:
        _v = message.reply_to_message
        user_id = _v.caption.split("|")[0][3::]
        user_caption = _v.caption.split("дан қабул қилинди!")[-1]
        user_video_id = _v.video.file_id
        video_id = message.video.file_id
        video_caption = message.caption

        await bot.send_video(
            chat_id=user_id,
            video=user_video_id,
            caption=f"{user_caption}\n\n👆 👆 👆 👆 👆 👆\n\n<b>Сизнинг саволингиз!</b>"
        )
        if video_caption == None:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption="<b>Саволингизга берилган жавоб!</b>"
            )
        else:
            await bot.send_video(
                chat_id=user_id,
                video=video_id,
                caption=f"<b>Саволингизга берилган жавоб!</b>\n\n{video_caption}"
            )
        await message.reply(
            text=f"Жавоб #ID{user_id} га муваффаққиятли юборилди! "
        )