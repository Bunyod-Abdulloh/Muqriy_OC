from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Ботни қайта ишга тушириш"),
            types.BotCommand("admins", "Админлар учун тугмалар"),
            types.BotCommand("man_questions", "Саволлар бўлими"),
            types.BotCommand("woman_questions", "Саволлар бўлими")
        ]
    )
