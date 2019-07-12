import os
from discord.ext import commands
from app.game_server_info import get_game_details

description = """A Dominions 5 Bot for keeping track of games and turn state"""
bot = commands.Bot(command_prefix="!", description=description)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


def fetch_alias(alias):
    if alias == 'newbie-knife-fight':
        return 604
    if alias == 'earlier-birds':
        return 643
    else:
        return


@bot.command()
async def details(ctx, alias):
    game_id = fetch_alias(alias)
    if game_id:
        block, response = await get_game_details(game_id)
        response.add_field(name="Players", value=block, inline=False)
        await ctx.send(embed=response)
    else:
        await ctx.send('error could not find game')


bot.run(os.getenv("TOKEN"))
