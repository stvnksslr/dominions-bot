from dotenv import load_dotenv

load_dotenv()

PLUGINS = ["machine.plugins.builtin.help.HelpPlugin", "plugins.dominions.TurnStatus"]

# Should the HTTP server be enabled?
DISABLE_HTTP = True

# ALIASES = '!'
