import discord
from discord.ext import commands
import math 

TOKEN = 'NzAxNDk3Mzg2NzEwNzI4Nzg1.XpyWdQ.KZWRtd6GujNIgv5o22D-Av3ghlY'
BOT_PREFIX = ('!','$')

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi there, (ctx.message.author.mention) !")

@bot.command()
async def sqrt(ctx, num):
    num = float(num)
    if num >=0:
        await ctx.send(f"The square root of (num) is {math.sqrt(num)}")
    else:
        await ctx.send("I can't take a square root of a negative number!")

@bot.command()
async def party(ctx):
    await ctx.message.add_reaction("🎉")
    await ctx.send(f"🎉 Let's party, {ctx.message.author.mention} 🎉")




bot.run(TOKEN)
