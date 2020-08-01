from dotenv import load_dotenv

load_dotenv()

PLUGINS = ["machine.plugins.builtin.help.HelpPlugin",
           "plugins.dominions.TurnStatus",
           "plugins.grog.Grog"]

# Should the HTTP server be enabled?
DISABLE_HTTP = True

ALIASES = "!"
