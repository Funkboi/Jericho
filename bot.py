import discord
from discord.ext import commands
import random
from random import choice
import os 

client = commands.Bot(command_prefix="+")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game(" with your heart <3"))
    print("I am online")

@client.event
async def on_message(message):
   if "jericho" in message.content:
       responses = ["bro don't talk", "seriously fuck off", "Sorry, I don’t understand what you’re saying. I don’t speak retard", "don't fucking talk about me retard", "how long did it take your fat fingers to type that dogshit message out?", "wanna try again, retard?", "just type '+faggot' already", "deadass? Shut the fuck up", "It's not a dumb name", "You're a fucking cunt dude, fuck off", "Don't fucking at me because I won't respond because the retard who programmed me doesn't know how to program a bot that responds to @s yet" ]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "Jericho" in message.content:
       responses = ["bro don't talk", "seriously fuck off", "Sorry, I don’t understand what you’re saying. I don’t speak retard", "don't fucking talk about me retard", "how long did it take your fat fingers to type that dogshit message out?", "wanna try again, retard?", "just type '+faggot' already", "deadass? Shut the fuck up", "It's not a dumb name", "You're a fucking cunt dude, fuck off", "Don't fucking at me because I won't respond because the retard who programmed me doesn't know how to program a bot that responds to @s yet" ]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "Jeriho" in message.content:
       responses = ["nice spelling retard", "retard cant spell", "look at this idiot"]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "Jerihco" in message.content:
       responses = ["nice spelling retard", "retard cant spell", "look at this idiot"]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "jerico" in message.content:
       responses = ["nice spelling retard", "retard cant spell", "look at this idiot"]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "Jerico" in message.content:
       responses = ["nice spelling retard", "retard cant spell", "look at this idiot"]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "this bot sucks" in message.content:
       responses = ["I dont see you programming a bot retard", "im sentient, moron", "Turing test my ass", "python is such a dogshit language"]
       random_Response = random.choice(responses)
       await message.channel.send(random_Response)
   if "+faggot" in message.content:
       await client.process_commands(message)
@client.command()
@commands.guild_only()
async def faggot(ctx):
    try:
        await ctx.send(choice(tuple(member.mention for member in ctx.guild.members if not member.bot)) + " is a faggot")
    except IndexError:
        await ctx.send("You are the faggot!")
@client.command()
async def clear(ctx, amount=20) :
    await ctx.channel.purge(limit=amount)


client.run(os.environ['DISCORD_TOKEN'])