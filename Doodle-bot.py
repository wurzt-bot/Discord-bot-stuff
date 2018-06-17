import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
import asyncio
import random

Client = discord.Client()
client = commands.Bot(command_prefix='=')
client.commanderid = 357596253472948224
user = discord.Member
startup_extensions = ['moderation', 'general', 'on_message_stuff']
client.data = {'test' : 'test object'}

def stafforcomm(inp):
    if client.commanderid == inp.author.id:
        return True
    if client.data[str(inp.guild)]['stfrole'] == discord.utils.get(inp.author.roles, id=self.client.staffrole.id):
        return True
    else:
        return False


def ifcomm(inp):
    if client.commanderid == inp.author.id:
        return True
    else:
        return False


@client.command(brief="Comm Only: sets the bot's name", hidden=True)
async def botname(ctx, *, botname: str):
    if ifcomm(ctx.message) == False:
        return
    await client.user.edit(username=botname)
    msg = 'Username has now been set to ' + botname
    await ctx.channel.send(msg)
    print((str(ctx.author) + ': ') + msg)

@client.command(hidden=True)
async def play(ctx, *, gamename : str):
    if ifcomm(ctx.message) == False:
        return
    game = discord.Game("with the API")
    await client.change_presence(activity=game)
    await ctx.channel.send("I'm now playing: " + gamename)

@client.event
async def on_message_edit(before, after):
    if before.author.bot == True:
        return
    fmt = '**{0.author}** edited their message from "{1.content}" to "{0.content}"'
    print(fmt.format(after, before))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("with katana")
    await client.change_presence(activity=game)


if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
client.run('NDI5NzgxODg3NDg2MDAxMTYz.DaGpLg.JAKgbUYCVdaXQ0-nUr9-am_95Fk')