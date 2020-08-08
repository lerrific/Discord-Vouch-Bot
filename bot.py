import json
import os

import discord
from discord.ext import commands

import utils

bot = commands.Bot(command_prefix=[utils.prefix])

# Remove help command so we can add our custom one
bot.remove_command("help")

# Load our cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Data stuffs
if os.path.isfile('data.json'):
    with open('data.json', 'r') as file:
        bot.data = json.loads(file.read())
        if not bot.data:
            bot.data = {}
else:
    bot.data = {}


@bot.event
async def on_ready():  # This event gets fired repeatedly for some reason
    #print('Logged in as {0} and connected to Discord! (ID: {0.id})'.format(bot.user))
    await bot.change_presence(activity=discord.Game(name=utils.prefix + 'help'))

# NjYxMDA0NzgwMzk0NTEyNDA1.XglGrA.aMsMp85SPaHGG9-pBVM-IkklBws
bot.run('NzM5NzI0MjM2NzU4NzEyMzM1.Xyen4Q.eRLSBQ19bfYNm9ivnAs23LcHOxs')
