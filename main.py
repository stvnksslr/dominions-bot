import os
from discord.ext import commands
from old_app.game_server_info import get_game_details, fetch_alias

description = """A Dominions 5 Bot for keeping track of games and turn state"""
bot = commands.Bot(command_prefix="!", description=description)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command()
async def add_server(ctx, server_addres):
    await ctx.send('Added Server')


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
