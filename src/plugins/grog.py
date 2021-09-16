from random import choice
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to, respond_to
from httpx import get

grog_response_list = [
    "grog",
    "grog?",
    "grog!!",
    ":freak_lord:",
    ":_g: :_r: :_o: :_g:",
    ":sumpyee: :sumpyee2:",
    ":ref:",
]


class Grog(MachineBasePlugin):
    @listen_to(r"grog")
    def grog_responder(self, msg):
        random_grog = choice(grog_response_list)
        msg.say(text=random_grog)


class ValheimServer(MachineBasePlugin):
    @respond_to(r"vikings")
    def status(self, msg):
        status = get("http://167.172.8.35:32418/status.json").json()
        players = len(status.get("players"))
        server = status.get("server_name")
        msg.say(
            text=f"server: {server} has {players} players online, direct connect: 167.172.8.35:32420 / pw: onlytims"
        )
