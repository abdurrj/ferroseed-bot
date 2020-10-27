import discord
intents = discord.Intents.all()
from discord.ext import tasks, commands
from discord.ext.commands import Cog
from discord.ext.commands.cooldowns import BucketType
from seed.Person import *
from discord.utils import find, get
from discord import Member
from random import randint, randrange
from io import StringIO, BytesIO
import random
import pandas as pd
import numpy as np
import argparse
import asyncio
import sys
import time
import csv
import re
import emoji
import json

TOKEN = open("token.txt","r").readline()

#                      Abdur
admin_users_id = [138411165075243008]

client = commands.Bot(command_prefix = '!', intents=intents)
client.remove_command('help')

extensions = ['RaidCommands', 'Den', 'Dexter', 'Fun', 'Functions', 'test_module']


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
@client.command(pass_context=True)
async def embed(ctx, name, *, text):
    id = ctx.message.author.id
    p = Person(id, ctx.message.channel, ctx.message.author)
    embed = discord.Embed(
    colour = discord.Colour.green())
    embed.add_field(name=' ' + name + ' ', value=" " + text + " ")
    await ctx.send(embed=embed)
    await discord.Message.delete(ctx.message)


# Lets users create a new channel by typing ".host x" where x is name the new channel.
# Name can contain spaces and unicode emojis (copy-paste, or phone keyboard emojis)
# Makes command only works in one channel, and creates the channel in the same category.
@client.command()
async def host(ctx, *, chaname):
    chnid = 739139612005630014
    if ctx.message.channel.id == chnid:
        a = str(chaname)
        b = str.replace(a, " ", "-")
        raid_category = client.get_channel(739139545202950161)
        await ctx.guild.create_text_channel(str(b), category=raid_category)
    else:
        return


# To end channels created in the category "A raid category", but also not allowing to close
# the channel "A raid category", which is the only channel .host command works
@client.command()
async def end(ctx):
    a = ctx.message.channel.id
    b = ctx.message.channel.category_id
    raidcat = 739139545202950161
    '''
    Channels and ID's
    #a-current-den-list = 735961355747590215
    #a-den-promo-pic-channel = 735170480545333308
    #a-raid-category = 739139612005630014
    '''
    raidchan = [739139612005630014, 735170480545333308, 735961355747590215]
    channeltest = all(channel != a for channel in raidchan)
    # To prevent deleting channels outside "A RAID CATEGORY"
    if raidcat == b: # Checks if the command is used inside "A RAID CATEGORY"
        if channeltest == True: # Prevents the command from working in the channel "a-raid-category"
            await ctx.message.channel.delete()
        else:
            await ctx.send("Not this channel, it's important! <a:RBops2:718139698912034937>")
    else:
        await ctx.send("Not this channel, it's important! <a:RBops2:718139698912034937>")



########################################################
########################################################
# Work in progress:




# Add custom commands over this
########################################################
########################################################


'''
#####################
Reaction events start

This includes:
Reaction role
React to pin
#####################
'''

@client.event
async def on_raw_reaction_add(payload):
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g :g.id == guild_id, client.guilds)
    #Reaction colour start
    message_id = payload.message_id
    if message_id == 756051702200664115: # Reaction colour roles
        # guild_id = payload.guild_id
        # guild = discord.utils.find(lambda g :g.id == guild_id, client.guilds)

        if payload.emoji.name == 'martin': # :name: for custom, but 😂 for unicode
            role = discord.utils.get(guild.roles, name='Martin')
        elif payload.emoji.name == '😈':
            role = discord.utils.get(guild.roles, name='Uniwinkle')
        elif payload.emoji.name == '🌸':
            role = discord.utils.get(guild.roles, name='Cherry')
        elif payload.emoji.name == 'ditto':
            role = discord.utils.get(guild.roles, name='Violet')
        elif payload.emoji.name == '💜':
            role = discord.utils.get(guild.roles, name='Lavender')
        elif payload.emoji.name == '🐤':
            role = discord.utils.get(guild.roles, name='Goldenrod')
        elif payload.emoji.name == '🌧️':
            role = discord.utils.get(guild.roles, name='Rain')
        elif payload.emoji.name == '💙':
            role = discord.utils.get(guild.roles, name='Forget-Me-Not')
        elif payload.emoji.name == '🌵':
            role = discord.utils.get(guild.roles, name='Saguaro')
        elif payload.emoji.name == '🌲':
            role = discord.utils.get(guild.roles, name='Evergreen')
        elif payload.emoji.name == '🍀':
            role = discord.utils.get(guild.roles, name='Mint')
        elif payload.emoji.name == '🌹':
            role = discord.utils.get(guild.roles, name='Rose')
        elif payload.emoji.name == '🍞':
            role = discord.utils.get(guild.roles, name='Cinnamon')
        # else:
        #     role = discord.utils.get(guild.roles, name=payload.emoji.name)    Use this if if emoji name = role names

        if role is not None:
            print(role.name)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            print(member)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


    # Reaction role start
    if message_id == 757997437213212826: # Reaction role
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g :g.id == guild_id, client.guilds)

        if payload.emoji.name == 'pogo': # :name: for custom, but 😂 for unicode
            role = discord.utils.get(guild.roles, name='PoGo raiders')
        # elif payload.emoji.name == '😈':
            # role = discord.utils.get(guild.roles, name='Uniwinkle')


        if role is not None:
            print(role.name)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


    # react to pin start
    pin_channel = client.get_channel(payload.channel_id)
    pin_msg = await pin_channel.fetch_message(payload.message_id)
    # pin_msg_user = [pin_msg.author.id]
    if payload.emoji.name == "📌":
        pin_guild_id = payload.guild_id
        pin_guild = discord.utils.find(lambda g :g.id == pin_guild_id, client.guilds)
        # pin_reactor = discord.utils.find(lambda m : m.id == payload.user_id, pin_guild.members)
        # pin_reactor_id = int(pin_reactor.id)
        # valid_users = pin_msg_user + admin_users_id
        # valid_users_test = all(user != pin_reactor_id for user in valid_users)
        # if valid_users_test == False:
        await pin_msg.pin()



    # Create voice channel
    if message_id == 770315723464638484:
        voice_category = client.get_channel(739139545202950161)
        channel_list = guild.channels
        channel_name_list = []
        for i in range(0, len(channel_list)):
            channel_name = channel_list[i].name
            channel_name_list.append(channel_name)
        
        if payload.emoji.name == '🟥':
            channel_name = "a-red-voice-channel"
            if channel_name in channel_name_list:
                print("Channel already created")
            else:
                await guild.create_voice_channel(channel_name, category=voice_category)
        elif payload.emoji.name == '🟩':
            channel_name = "a-green-voice-channel"
            if channel_name in channel_name_list:
                print("Channel already created")
            else:
                await guild.create_voice_channel(channel_name, category=voice_category)
        elif payload.emoji.name == '🟦':
            channel_name = "a-blue-voice-channel"
            if channel_name in channel_name_list:
                print("Channel already created")
            else:
                await guild.create_voice_channel(channel_name, category=voice_category)






"""
############################################
"""




# remove react to remove role
@client.event
async def on_raw_reaction_remove(payload):

    # Remove react to remove colour
    message_id = payload.message_id
    if message_id == 756051702200664115: # Reaction colour roles
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g :g.id == guild_id, client.guilds)

        if payload.emoji.name == 'martin': # :name: for custom, but 😂 for unicode
            role = discord.utils.get(guild.roles, name='Martin')
        elif payload.emoji.name == '😈':
            role = discord.utils.get(guild.roles, name='Uniwinkle')
        elif payload.emoji.name == '🌸':
            role = discord.utils.get(guild.roles, name='Cherry')
        elif payload.emoji.name == 'ditto':
            role = discord.utils.get(guild.roles, name='Violet')
        elif payload.emoji.name == '💜':
            role = discord.utils.get(guild.roles, name='Lavender')
        elif payload.emoji.name == '🐤':
            role = discord.utils.get(guild.roles, name='Goldenrod')
        elif payload.emoji.name == '🌧️':
            role = discord.utils.get(guild.roles, name='Rain')
        elif payload.emoji.name == '💙':
            role = discord.utils.get(guild.roles, name='Forget-Me-Not')
        elif payload.emoji.name == '🌵':
            role = discord.utils.get(guild.roles, name='Saguaro')
        elif payload.emoji.name == '🌲':
            role = discord.utils.get(guild.roles, name='Evergreen')
        elif payload.emoji.name == '🍀':
            role = discord.utils.get(guild.roles, name='Mint')
        elif payload.emoji.name == '🌹':
            role = discord.utils.get(guild.roles, name='Rose')
        elif payload.emoji.name == '🍞':
            role = discord.utils.get(guild.roles, name='Cinnamon')
        # else:
        #     role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            print(role.name)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")
    

    # Remove react to remove role start
    if message_id == 757997437213212826: # Reaction roles
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g :g.id == guild_id, client.guilds)

        if payload.emoji.name == 'pogo': # :name: for custom, but 😂 for unicode
            role = discord.utils.get(guild.roles, name='PoGo raiders')
        # elif payload.emoji.name == '😈':
            # role = discord.utils.get(guild.roles, name='Uniwinkle')

        if role is not None:
            print(role.name)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")
    

    # Remove react to remove pin start
    pin_channel = client.get_channel(payload.channel_id)
    pin_msg = await pin_channel.fetch_message(payload.message_id)
    # pin_msg_user = [pin_msg.author.id]
    if payload.emoji.name == "📌": 
        pin_guild_id = payload.guild_id
        pin_guild = discord.utils.find(lambda g :g.id == pin_guild_id, client.guilds)
        # pin_reactor = discord.utils.find(lambda m : m.id == payload.user_id, pin_guild.members)
        # pin_reactor_id = int(pin_reactor.id)
        # valid_users = pin_msg_user + admin_users_id
        # valid_users_test = all(user != pin_reactor_id for user in valid_users)
        # if valid_users_test == False: # use this if you want only message author and admins to be able to unpin
        await pin_msg.unpin()



    if message_id == 770315723464638484:
        voice_category = client.get_channel(770314988170248222)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g :g.id == guild_id, client.guilds)
        if payload.emoji.name == '🟥':
            channel_name = "a-red-voice-channel"
            channel = discord.utils.get(guild.voice_channels, name=channel_name)
            await discord.VoiceChannel.delete(channel)
        elif payload.emoji.name == '🟩':
            channel_name = "a-green-voice-channel"
            channel = discord.utils.get(guild.voice_channels, name=channel_name)
            await discord.VoiceChannel.delete(channel)
        elif payload.emoji.name == '🟦':
            channel_name = "a-blue-voice-channel"
            channel = discord.utils.get(guild.voice_channels, name=channel_name)
            await discord.VoiceChannel.delete(channel)





'''
#####################
Reaction events end
#################
'''

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
