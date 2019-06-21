import os

from discord.ext import commands
from dotenv import load_dotenv

# Load Env
load_dotenv()

description = '''A Dominions 5 Bot for keeping track of games and turn state'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(os.getenv("TOKEN"))
