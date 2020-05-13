# Discord Bot written in Python 3 by Elmo
# Edited by [PUT YOUR NAME HERE]

# This is just a simple bot, you can add a lot more to this if you understand the basics
# This bot does use several libraries to work


# Imports
# These are all the libraries we are using in the bot, pretty self explanatory but you don't need them all
import discord # Needed
from discord.ext import commands, tasks # commands is needed but tasks is not
from discord.utils import get # not needed
from discord_webhook import DiscordWebhook as DISCWEB # not needed

# Although some libraries are not needed to make a functioning bot
# I like to use them to make my bot look a little better
# Down below are some examples of events and functions for discord.py

# for functions you need 'async' before 'def' or it won't work, but only if it is under a decorator
# The decorators are `@bot.event` and '@bot.command()' and then also '@tasks.loop()'
# I hope this helps someone

bot = commands.Bot(command_prefix="!") # This line is required for the bot to work, but you can change the prefix inside the quotes
webhoook_id_welcome = "Webhook url here" # This is the webhook url


@bot.event # Tells discord that I am looking for an event
async def on_ready(): # This tells discord which event I am looking for
    print(bot.command_prefix) # This just prints out the command_prefix
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Minecraft')) # This sets the bot status and the activity (it isn't needed but it is cool)
    print("Bot Fired Event: on_ready()") # This just prints out that the bot is working and everything went well with no errors


#   - Member Joined event
@bot.event
async def on_member_join(member):
    print(f"{member} joined.") # Prints that a member joined and tells me the name of the member
    webhook = DISCWEB(url=webhook_id_welcome, content = f'{member.mention} welcome to the server!') # This uses a webhook which is just like a mini bot for discord, it can do simple things.  This one welcomes the new member to the server.
    webhook.execute() # This sends the data to discord for the webhook to work

@bot.command() # Tells the bot that I am looking for a message that starts with the command_prefix
async def ping(ctx): # Tells the bot the command name 'ping'.  Ex: !ping
    print(f"Pong! {round(bot.latency*1000)}ms") # This pings the bot and tells you the response speed in ms


# Run command
bot.run("Put your bot token here") # Prett self explanatory but it runs the bot with the token.