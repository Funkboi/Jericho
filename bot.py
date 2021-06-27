import discord
from discord.ext import commands
import random
from random import choice
import os 

client = commands.Bot(command_prefix="+")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game(" type 'sus' for fun "))
    print("I am online")

@client.event
async def on_message(message):
   if "jericho" in message.content:
       await message.channel.send("Justin was banned")
   if "Jericho" in message.content:
       await message.channel.send("Justin was banned")
   if "JERICHO" in message.content:
       await message.channel.send("Justin was banned")
   if "Jeriho" in message.content:
       await message.channel.send("Justin was banned")
   if "Jerihco" in message.content:
       await message.channel.send("Justin was banned")
   if "jerico" in message.content:
       await message.channel.send("Justin was banned")
   if "Jerico" in message.content:
       await message.channel.send("Justin was banned")
   if "this bot sucks" in message.content:
       await message.channel.send("Justin was banned")
   if "This bot sucks" in message.content:
       await message.channel.send("Justin was banned")
   if "sus" in message.content:
       await message.channel.send("Justin was banned.")
   if "SUS" in message.content:
       await message.channel.send("Justin was banned.")
   if "+faggot" in message.content:
       await client.process_commands(message)
@client.command()
@commands.guild_only()
async def faggot(ctx):
    try:
        await ctx.send("whoever banned Justin is a faggot")
    except IndexError:
        await ctx.send("whoever banned Justin is a faggot")
@client.command()
async def clear(ctx, amount=20) :
    await ctx.channel.purge(limit=amount)


client.run(os.environ['DISCORD_TOKEN'])