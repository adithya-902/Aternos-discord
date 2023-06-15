import discord
import random
import random
from discord.ext import commands
from aternosapi import AternosAPI
from example import cmd



client=commands.Bot(command_prefix='bro ')

'''
@client.command(aliases=['server list'])
async def server_list(ctx):
    embed=discord.Embed(title='Available servers',description="Enter the server number (1/2)\nDM Biju ( @adi902 ) for server address",color=discord.Colour.green())
    embed.add_field(name="1) 12A minecraft server")
    embed.add_field(name="2) Among peeps server")
    await ctx.send(embed=embed)
'''

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(' Your mom'))
    print('Bot is ready')


@client.command()
async def ping(ctx):
    p=round(client.latency*1000)
    if p>350:
        await ctx.send(f'Damn get better internet you peasant.\nYour ping is {p}ms')
    else:
        await ctx.send(f'Your ping is acceptable :).\nIt\'s {p}ms')

@client.command(aliases=["toss"])
async def coin(ctx):
    toss=random.choice(["heads","tails"])
    await ctx.send(toss)


@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    answers=['As I see it', 'yes.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.','Don’t count on it.','It is certain.','It is decidedly so.','Most likely.' ,'My reply is no.','My sources say no.','Outlook not so good.','Outlook good.', 'Reply hazy, try again.','Signs point to yes.','Very doubtful.','Without a doubt.','Yes.', 'Yes – definitely.', 'You may rely on it.']
    
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

@client.command()
async def start(ctx):
    
    await ctx.send(f'The server is starting :)')
    cmd("start",n=1)

@client.command()
async def spam(ctx,*,rip):
    for i in range(20):
        await ctx.send(rip)

@client.command()
async def hello(ctx):
    await ctx.send('Whomst has summoned the almighty one ')
'''

@client.command()
async def stop(ctx):
    await ctx.send(f'The server is stopping :(') 
    cmd("stop",n=1)
    
'''




client.run('Nzc1Njg1MTEyMTcxODU1ODg5.X6p7Dg.kMBorBVCMad6lpLBRV2N4cCr8Ag')



























































'''
@client.command()
async def clear(ctx, amount=0):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit= amount+1)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')

'''