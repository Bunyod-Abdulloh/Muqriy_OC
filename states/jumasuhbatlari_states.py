from aiogram.dispatcher.filters.state import StatesGroup, State


class JumaSuhbatlari(StatesGroup):
    juma_one = State()
    juma_audio_one = State()
    juma_audio_two = State()
    juma_video_one = State()
    juma_video_two = State()
