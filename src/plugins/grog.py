from random import choice
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to

grog_response_list = [
    "grog",
    "grog?",
    "grog!!",
    ":freak_lord",
    ":g: :r: :o: :g:",
    ":sumpyee: :sumpyee2:",
    ":ref"
]


class Grog(MachineBasePlugin):
    @listen_to(r"grog")
    def grog_responder(self, msg):
        random_grog = choice(grog_response_list)
        msg.reply(text=random_grog)
