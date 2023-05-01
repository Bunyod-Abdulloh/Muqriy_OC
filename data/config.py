from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
BOT_ADMINS = env.list("BOT_ADMINS")
ID_MEN_GROUP = env.list("ID_MEN_GROUP")
ID_WOMEN_GROUP = env.list("ID_WOMEN_GROUP")
IP = env.str("IP")
CHANNELS = env.list("CHANNELS")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")