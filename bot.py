# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

with open("token.txt", "r") as f:
    data = [i.strip() for i in f.readlines()]
    TOKEN = data[0]


client = commands.Bot(command_prefix='..')


@client.event
async def on_ready():
    print("bot is ready")
    
#load cogs
@client.command()
async def load_cog(ctx, cog):
    try:
        client.load_extension(cog)
    except Exception as e:
       print(f"loading {cog} failed")
       print(e)

@client.command()
async def unload_cog(ctx, cog):
    try:
        client.unload_extension(cog)
    except Exception as e:
        print(f"unloading {cog} failed")
        print(e)

#shutdown
@client.command()
async def shutdown(ctx):
    #give shutdown command via cmd
    #temp via file
    open("shutdown", "a").close()
    await client.close()

#update
async def update(ctx):
    await client.close()   

client.run(TOKEN)









