from environs import Env

env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
BOT_ID: str = BOT_TOKEN.split(":")[0]
ADMINS: list = env.str("ADMINS").split(",")

