from discord.ext import commands, tasks
import discord
import os
import json
import time
import random
import asyncio
import requests
 
#--------------------------------

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=">>", case_insensitive=True,intents=intents )


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
             activity=discord.Game("Complementary!"))
    print("\nLogged in as", client.user, "\n")
client.remove_command('help')

@client.command()
async def ping(ctx):
    await ctx.reply('Pong !')



extensions  = [ 'commands.ban', 'commands.pick','commands.top','commands.warn','commands.voice','commands.mute','commands.hide','commands.unhide','commands.brodk','commands.kick','commands.help']
if __name__ == '__main__': 

  for ext in extensions : 
    client.load_extension(ext)

 
client.run(os.getenv('TOKEN'))
