import logging

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    try:
        pass
    except Exception as err:
        logging.exception(err)
