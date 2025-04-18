import discord
from discord.ext import commands

bot = commands.bot(commands_prefix='/')

@bot.command()

async def echo(ctx, *arg):