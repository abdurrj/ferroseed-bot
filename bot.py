import discord
intents = discord.Intents.all()
from discord.ext import tasks, commands
from discord.ext.commands import Cog
from discord.ext.commands.cooldowns import BucketType
from discord.utils import find, get
from discord import Member
from random import randint, randrange
from io import StringIO, BytesIO
import pandas as pd
import asyncio
import time
import random

TOKEN = open("token.txt","r").readline()

#                      Abdur
admin_users_id = [138411165075243008]
client = commands.Bot(command_prefix = '!', intents=intents)
client.remove_command('help')

extensions = ['RaidCommands', 'Den', 'Dexter', 'Fun', 'Functions', 'test_module', 'Reactions', 'Hosting', 'fc', 'countdown']


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.guild is None:
        await message.channel.send("Hey there!")
    else:
        await client.process_commands(message)


# To embed a message, this will also delete user command message
@client.command()
async def embed(ctx, name, *, text):
    embed = discord.Embed(
    colour = discord.Colour.green())
    embed.add_field(name=' ' + name + ' ', value=" " + text + " ")
    await ctx.send(embed=embed)
    await discord.Message.delete(ctx.message)


########################################################
########################################################
# Work in progress:

@client.command()
async def divide(ctx, DRAFT_COUNT:int=10):
    ladder_agree = []
    ladder_team_a = []
    ladder_team_b = []

    ladder = await ctx.send("Would you like to join the team distribution?")
    await ladder.add_reaction("⭕")

    guide_text = await ctx.send("count : " + str(DRAFT_COUNT) + " sec")
    while DRAFT_COUNT>=1:
        DRAFT_COUNT -= 1
        await guide_text.edit(content=f"count : {DRAFT_COUNT} sec")
        await asyncio.sleep(1)
    
    await guide_text.edit(content="done")
    ladder = await ctx.channel.fetch_message(ladder.id)
    ladder_agree = [u.mention for u in await ladder.reactions[0].users().flatten() if u != client.user]

    if len(ladder_agree)>1:
        while len(ladder_agree) > 1:
            if len(ladder_agree)>0:
                temp1 = random.choice(ladder_agree)
                ladder_team_a.append(temp1)
                ladder_agree.remove(temp1)

            if len(ladder_agree)>0:
                temp2 = random.choice(ladder_agree)
                ladder_team_b.append(temp2)
                ladder_agree.remove(temp2)

        text = ""
        for i in range(0, len(ladder_team_a)):
            text = text + ladder_team_a[i] + ", " 
        await ctx.send("\n\n Team A : " + text)

        text2 = ""
        for i in range(0, len(ladder_team_b)):
            text2 = text2 + ladder_team_b[i] + ", "
        await ctx.send("\n\n Team B : " + text2)
    else:
        await ctx.send("Not enough entrants")


# Add custom commands over this
########################################################
########################################################




#Command used for bot admin to turn their bot off
#Please put the admin's discord ID where indicated

@client.command()
async def ext_names(ctx):
    await ctx.send(extensions)

@client.command()
async def logout(ctx):
    if ctx.message.author.id in admin_users_id:
        await ctx.send('```Shutting down...```')
        await client.logout()
    else:
        await ctx.send('No......')


@client.command()
async def test(ctx):
    while True:
        print("Hello!")
        await asyncio.sleep(1)
        return
    

@client.command()
async def load(ctx, extension):
    if ctx.message.author.id in admin_users_id:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
            await ctx.send('Loaded {}'.format(extension))
    else:
        await ctx.send("Loadi... Wait a minute, you're not Abdur! <:ferroSquint:735703818205134859>")


@client.command()
async def reload(ctx, extension):
    if ctx.message.author.id in admin_users_id:
        try:
            client.reload_extension(extension)
            print('Reloaded {}'.format(extension))
            await ctx.send('Reloaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be reloaded. [{}]'.format(extension, error))
    else:
        await ctx.send("Reloadi... wait a minute, you're not Abdur! <:ferroSquint:735703818205134859>")


@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id in admin_users_id:
        try:
            client.unload_extension(extension)
            print('Unloaded {}'.format(extension))
            await ctx.send('Unloaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be unloaded. [{}]'.format(extension, error))
    else:
        await ctx.send("Unloadi... wait a minute, you're not Abdur! <:ferroSquint:735703818205134859>")

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

    #client.loop.create_task(test())
    client.run(TOKEN)
