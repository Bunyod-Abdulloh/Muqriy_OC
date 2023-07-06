from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("BOT_ADMINS")
MAN_GROUP = env.str("MAN_GROUP")
WOMAN_GROUP = env.str("WOMAN_GROUP")
IP = env.str("IP")
CHANNELS = env.list("CHANNELS")

# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_NAME = env.str("DB_NAME")
# DB_HOST = env.str("DB_HOST")