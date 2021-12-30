import discord, asyncio
from discord.ext import commands

from dotenv import load_dotenv
import importlib
import os,sys
from env import encoding, networking, misc
import config

load_dotenv('.env')

TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

client = commands.Bot(command_prefix=PREFIX)

@client.command()
async def decode(ctx, *args):
    importlib.reload(encoding)
    if args[0] == 'base64':
        await encoding.base64ToAscii(ctx, args[1:])
    elif args[0] == 'hex':
        await encoding.hexToAscii(ctx, args[1:])
    elif args[0] == 'binary':
        await encoding.binaryToAscii(ctx, args[1:])

@client.command()
async def nc(ctx, *args):
    importlib.reload(networking)
    if args[0] == 'sendudp':
        await networking.sendudp(ctx,args[1:])

@client.command()
async def exec(ctx, *args):
    importlib.reload(misc)
    if str(ctx.author.id) in config.superusers:
        await misc.exec(ctx, args)








print(TOKEN)
sys.stdout.flush()        

client.run(TOKEN)