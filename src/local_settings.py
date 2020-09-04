from dotenv import load_dotenv
from os import getenv

load_dotenv()

PLUGINS = [
    "machine.plugins.builtin.help.HelpPlugin",
    "plugins.dominions.TurnStatus",
    "plugins.grog.Grog",
]
STORAGE_BACKEND = "machine.storage.backends.redis.RedisStorage"
REDIS_URL = getenv("REDIS_URL")

# Should the HTTP server be enabled?
DISABLE_HTTP = True

ALIASES = "!"
