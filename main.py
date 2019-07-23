import os
from discord.ext import commands

from app.game_crud import add_game, fetch_game
from app.game_server_info import format_game_details

description = """A Dominions 5 Bot for keeping track of games and turn state"""
bot = commands.Bot(command_prefix="!", description=description)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command()
async def add(ctx, server_address):
    add_game(server_address)
    await ctx.send('Added Server')


@bot.command()
async def details(ctx, game_id):
    if game_id:
        game_info = fetch_game(game_id)
        block, response = format_game_details(game_info)
        response.add_field(name="Players", value=block, inline=False)
        await ctx.send(embed=response)


bot.run(os.getenv("TOKEN"))
