import discord, asyncio
from discord.ext import commands

from dotenv import load_dotenv
import importlib
import os,sys
from env import encoding, networking, misc, steg
import config

load_dotenv('.env')

TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')
AZUREKEY = os.getenv('AZURE-COGNITIVE-KEY')
AZUREENDPOINT = os.getenv('AZURE-COGNITIVE-ENDPOINT')

# client = commands.Bot(command_prefix=PREFIX)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
intents.guild_messages = True
client = commands.Bot(intents=intents, command_prefix=PREFIX)

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
    else: await ctx.send(f"you shall not pass")

# z-ocr id [attachment]
@client.command()
async def ocr(ctx, *args):
    importlib.reload(steg)
    if args[0] == "help" or not args[0]:
        await ctx.send(steg.ocr.__doc__)
    else:
        try:
            await steg.ocr(ctx, args, AZUREKEY, AZUREENDPOINT)
        except Exception as e:
            await ctx.send(e)

@client.command()
async def su(ctx, *args):
    if str(ctx.author.id) in config.superusers:
        if "add" in args:
            config.superusers.append(str(args[1]))
            await ctx.send(f"added superuser: {ctx.author.id}")
        elif "rm" in args:
            config.superusers.remove(str(args[1]))
            await ctx.send(f"added superuser: {ctx.author.id}")
    else: await ctx.send(f"you shall not pass")






if __name__ == "__main__":
    print(TOKEN)
    sys.stdout.flush()        

    client.run(TOKEN)