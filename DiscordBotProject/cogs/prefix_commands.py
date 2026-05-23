from discord import app_commands
import discord

def setup_commands(bot):

    @bot.command()
    async def hello(ctx):
        await ctx.send("hi")

    @bot.command()
    async def cheese(ctx):
        await ctx.send("cheese")
