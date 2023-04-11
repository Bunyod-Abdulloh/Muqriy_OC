from aiogram import Dispatcher

from loader import dp
from .savol_filters import TextReply, PhotoReply, VoiceReply, VideoReply, AudioReply

# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(TextReply)
    dp.filters_factory.bind(PhotoReply)
    dp.filters_factory.bind(VoiceReply)
    dp.filters_factory.bind(AudioReply)
    dp.filters_factory.bind(VideoReply)
    pass
