import subprocess  # noqa: S404
from environs import Env

# VERSION = (
#     subprocess.check_output(["git", "describe", "--always"])  # noqa: S603,S607
#     .strip()
#     .decode()
# )

env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
BOT_ID: str = BOT_TOKEN.split(":")[0]
ADMINS: list = env.str("ADMINS").split(",")

# LOGGING_LEVEL: int = env.int("LOGGING_LEVEL", 10)
