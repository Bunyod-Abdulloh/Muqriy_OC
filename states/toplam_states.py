from aiogram.dispatcher.filters.state import StatesGroup, State


class TortToplam(StatesGroup):
    one = State()
    audio_one = State()
    audio_two = State()
    video_one = State()
    video_two = State()
