from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Ботни қайта ишга тушириш"),
            types.BotCommand("bot_admins", "Админлар учун тугмалар"),
            types.BotCommand("xatm_admins", "Хатм админлари учун тугмалар")
        ]
    )