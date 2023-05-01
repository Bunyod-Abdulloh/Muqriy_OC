from aiogram import executor

from loader import dp, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.help import AlbumMiddleware


async def on_startup(dispatcher):
    await db.create()
    await db.create_table_users()
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    dp.middleware.setup(AlbumMiddleware())
    executor.start_polling(dp, on_startup=on_startup, allowed_updates=["message", "callback_query", "chat_member"])
