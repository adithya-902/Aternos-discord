import discord
import random
from discord.ext import commands
from aternosapi import AternosAPI
from example import cmd

client=commands.Bot(command_prefix='steve ')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(' Minecraft'))
    print('Among peeps is ready')

@client.command()
async def start(ctx):
    await ctx.send(f' The server is starting :)')
    cmd("start",n=2)

@client.command()
async def stop(ctx):
    await ctx.send(f'The server is stopping :(') 
    cmd("stop",n=2)

client.run('Nzc3ODE3MzA5NTQwNjQ2OTIy.X7I80Q.F1K6gmSUxUWlP7P3nSwwUIm9lwo')
    