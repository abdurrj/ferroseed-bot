import discord
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.emojis = True
intents.messages = True
intents.reactions = True
from discord.ext import tasks, commands
from discord.ext.commands import Cog
from discord.ext.commands.cooldowns import BucketType
from Person import *
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

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')

extensions = ['RaidCommands']

#                      Abdur
admin_users_id = [138411165075243008]

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
	channel = message.channel
	if message.guild is None:
		await message.channel.send("Hey there!")
	else:
	    await client.process_commands(message)

#Command used for bot admin to turn their bot off
#Please put the admin's discord ID where indicated
@client.command()
async def logout(ctx):
	if ctx.message.author.id in [138411165075243008]:
		await ctx.send('```Shutting down...```')
		await client.logout()
	else:
		await ctx.send('No......')

#Sends greet command
@client.command()
async def hi(ctx):
    id = ctx.message.author.id
    p = Person(id, ctx.message.channel, ctx.message.author)
    if ctx.message.author.id in [673257997191086080]: #Blank
        await ctx.send("Hello, Team Soul leader Tomador! <:ferroHappy:734285644817367050>")
    if ctx.message.author.id in [357179587073146893]: # Haywire
        await ctx.send(" :bug: :eyes:")
    elif ctx.message.author.id in [269225344572063754]: # Uni
        await ctx.send("Hi Uni <:shinyEis:736307511191404555>")
    else:
        await ctx.send("<:ferroHappy:734285644817367050>")

# Shows a list of dens on serebii website
@client.command()
async def denlist(ctx):
    await ctx.send("<https://www.serebii.net/swordshield/maxraidbattledens.shtml>")

# Links to specific den on serebii website. Adjust max number for CT when available
@client.command(pass_context=True)
async def den(ctx, a):
    id = ctx.message.author.id
    p = Person(id, ctx.message.channel, ctx.message.author)
    user = ctx.message.author.name
    # Checks if input is a numeric value, if yes: limits number between 1-157 for dens,
    # if no: Only works for the word promo

    poke_in_den = pd.read_excel('./poke_in_den.xlsx')
    for index, row in poke_in_den.iterrows():
        if row["Pokemon"] == (a.lower()).title():
            info = (row[0]+" is in these dens:\n"+row[1])
            poken = str(row[0])
            break
        else:
            poken = "crab"

    if a.isnumeric():
        b = int(a)
        if b >=1 and b <158:
            await ctx.send("<https://www.serebii.net/swordshield/maxraidbattles/den"+str(b)+".shtml>")
        else:
            await ctx.send("That's not a den, "+str(user)+"! <a:RBops2:718139698912034937>. Only from 1 to 157, or promo <a:RHype:708568633508364310>")
    else:
        if a.lower() == 'promo':
            await ctx.send("<https://www.serebii.net/swordshield/wildareaevents.shtml>")
        elif a.title() == poken:
            await ctx.send(info)
        else:
            await ctx.send("That's not a den, "+str(user)+"! <a:RBops2:718139698912034937>. Only from 1 to 157, or promo <a:RHype:708568633508364310>\nOr.. you an name a pokemon that is in a den")

# To get a random den number. from the available dens. Increase max number and add CT when available
@client.command()
async def newden(ctx, *args):
    if args:
        loc = args[0]
        if loc == "ioa":
                i = randint(94, 157)
        elif loc == "swsh":
                i = randint(1, 93)
    else:
        i = randrange(157)
    newden = str(i)
    await ctx.send("<https://www.serebii.net/swordshield/maxraidbattles/den"+newden+".shtml>")

# Caught
@client.command(pass_context=True, name = 'caught', aliases=['c', 'catch', 'CAUGHT', 'CATCH', 'CAUGHT!', 'caught!', 'catch!', 'CATCH!'])
async def caught(ctx, *ball):
    id = ctx.message.author.id
    ball_list = {'sport' : '<:xSport:733003042773008494>', 'safari' : '<:xSafari:733003042579808297>', 'beast' : '<:xNightmare:733002933473378435>',
                 'moon' : '<:xMoon:733003042705768518>', 'lure' : '<:xLure:733003042621751347>', 'love' : '<:xLove:733003042668150865>', 'level' : '<:xLevel:733003042244263938>',
                 'heavy' : '<:xHeavy:733002891341594674>', 'friend' : '<:xFriend:733002850933800991>', 'fast' : '<:xFast:733002797343047690>', 'dream' : '<:xDream:733002735749824695>'}
    
    # List of colours: (0)Light blue, (1)light green, (2)purple, (3)yellow, (4)white, (5)peach, (6)pink, (7)Blue, (8)Honey yellow
    colour_list = [0x96e6ff, 0x62eb96, 0x9662eb, 0xffe36f, 0xe5e5e5, 0xf7b897, 0xffb3ba, 0x21b1ff, 0xffd732]
    a = randint(0,8)
    colour = colour_list[a]
    if ball:
        ball_used = str(ball[0])
        if ball_used in ball_list.values():
            ball_emoji = ball_used
        else:
            ball_used = ball_used.lower()
            if ball_used in ball_list.keys():
                ball_emoji = ball_list[ball_used]
            else:
                ball_emoji = '<:xPoke:764576089275891772>'
    else:
        ball_emoji = '<:xPoke:764576089275891772>'
    
    embed = discord.Embed(
    colour = colour)
    embed.add_field(name=ball_emoji + " Caught!", value="<:RParty:706007725070483507> <@"+str(id)+"> has caught the pokemon! <:RParty:706007725070483507>", inline=True)
    a = await ctx.send(embed=embed)
    await discord.Message.add_reaction(a, "<:ferroHappy:734285644817367050>")
    await discord.Message.add_reaction(a, "<:sayHeart:741079360462651474>")
    if ball_emoji != '<:xPoke:764576089275891772>':
        await discord.Message.add_reaction(a, ball_emoji)

# Naught, for when you don't catch the pokemon
@client.command(pass_context=True, name = 'naught', aliases=['not'])
async def naught(ctx):
    id = ctx.message.author.id
    p = Person(id, ctx.message.channel, ctx.message.author)
    embed = discord.Embed(
    colour = discord.Colour.red())
    embed.add_field(name='<:sherbSad:732994987683217518> escaped', value="<@"+str(id)+"> did not catch the pokemon.", inline=True)
    a = await ctx.send(embed=embed)
    await discord.Message.add_reaction(a, "<:ferroSad:735707312420945940>")

# If you're brave enough, you can try and pet ferroseed.
# To increase/decrease the chance of "pet" change * or ** in code
@client.command(pass_context=True)
async def pet(ctx):
    id = ctx.message.author.id
    p = Person(id, ctx.message.channel, ctx.message.author)
    petpet = randrange(12)  # randrange(*), increase * value to increase chance of petting Ferroseed
    if petpet >= 5:         # petpet >= **: Lower the number on ** to increase chance of petting Ferroseed (standard is 6)
        with open("ferropet.txt", "r+") as fpet:
            petcount = fpet.read()
            i = int(petcount)
            b = str((i+1))
            fpet.seek(0)
            fpet.write(b)
        embed = discord.Embed(
        colour = discord.Colour.green())
        embed.add_field(name='Ferroseed anticipated this', value="<@"+str(id)+"> pet Ferroseed! <:ferroHappy:734285644817367050> \n"
                                                                    "\nFerroseed has been pet "+b+"x times!")
        await ctx.send(embed=embed)
    else:
        with open("ferrohurt.txt", "r+") as fhurt:
            hurtcount = fhurt.read()
            i = int(hurtcount)
            b = str((i+1))
            fhurt.seek(0)
            fhurt.write(b)
        embed = discord.Embed(
        colour = discord.Colour.red())
        embed.set_author(name='Ouch!')
        embed.add_field(name='*Sorry!*', value="<@"+str(id)+"> got hurt by Iron Barbs <:ferroSad:735707312420945940>\n"
                                                "\nI've hurt you all a total of "+ b +"x times.")
        await ctx.send(embed=embed)

@client.command()
async def pets(ctx):
    with open("ferropet.txt", "r+") as fpet:
        petcount = fpet.read()
    with open("ferrohurt.txt", "r+") as fhurt:
        hurtcount = fhurt.read()
    await ctx.send("I've been pet **"+petcount+"x** times and I've hurt you **"+hurtcount+"x** times")

@client.command()
async def birbpet(ctx):
    await ctx.send("<a:PetTheBirb:754269160598536214>")

# Go to sleep commands
@client.command()
async def sleep(ctx, str):
    await ctx.send("Go to sleep, "+str+" <a:RBops2:718139698912034937>")

# Work command
@client.command(name = 'work', aliases=['homework'])
async def work(ctx, str):
    choice = [1,2,3,4,5,6,7,8,9,10]
    selection = random.choice(choice)
    # print(selection)
    if selection >= 6:
        await ctx.send("<a:RBops:718139734693773330> "+str+"! Go be productive.")
        # print("big")
    else:
        # print("smol")
        await ctx.send(str+"! Go do the things. <:RStudy:762627515747008512>")

@client.command()
async def absleep(ctx):
    if ctx.message.author.id in [138411165075243008]:
        embed = discord.Embed(
        colour = discord.Colour.green())
        embed.add_field(name='*Abdur is going to sleep*', value=":zzz: :zzz: :zzz:")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
        colour = discord.Colour.green())
        embed.add_field(name='ABDUR!!', value="Go to sleep! <a:RBops2:718139698912034937>")
        await ctx.send(embed=embed)

#Friend code check, document "friendcodes.csv" is saved locally.
@client.command()
async def fc(ctx, *args):
    p = Person(id, ctx.message.channel, ctx.message.author)
    filename = "friendcodes.csv"
    df = pd.read_csv(filename)
    if args:
        userid = int(''.join(i for i in args[0] if i.isdigit()))
    else:
        userid = ctx.message.author.id
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        if row["usid"] == int(userid):
            await ctx.send((row[2] + "\n" + row[3] + "\n" + row[4] + "\n" + row[5] +  "\n" + row[6] +  "\n" + row[7]))

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
        # guild = ctx.message.guild
        name = 'A Raid category'
        category = discord.utils.get(ctx.guild.categories, name=name)
        await ctx.guild.create_text_channel(str(b), category=category)
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
            await ctx.send("<:ferroSquint:735703818205134859>")
            time.sleep(0.5)
            await ctx.send("Not this channel! It's important!")
    else:
        await ctx.send("<:ferroSquint:735703818205134859>")
        time.sleep(0.5)
        await ctx.send("Not this channel, it's important! <a:RBops2:718139698912034937>")


# Lets the user create a poll, And add reactions for what the questions with the emojis in the question themselves. 
# Does not seem to work with different "tone" for skin. Only yellow ones
@client.command()
async def poll(ctx, *, text):
    # Get the User_ID
    id = ctx.message.author.id
    a = text
    # Two functions: 1) Get list of emoji information(location, emoji), 2) convert list to string
    emoji_init_string = str(emoji.emoji_lis(a))
    # Two functions: 1) Convert emoji to be :emoji_name: instead of unicode emoji, 2) Find string between : : 
    disc_emoji_sep = re.findall(r"':([^:']*):'", emoji.demojize(emoji_init_string))
    # Three functions: 1) For every element in the list "disc_emoji_sep", add : to either side, 2) Turn that list in to a string,
    # 3) use emoji.emojize function, to turn emojis in that string back to unicode emoji
    disc_emoji_string = emoji.emojize(str([''.join(':' + demoji + ':') 
                                      for demoji in disc_emoji_sep]))
    # Read the string that looks like(for your emojis): ['�👀', 🙂🙂' '😀�', '🤪🤪'], and turn it to a list of unicode emojis
    disc_emoji = re.findall(r"'([^']*)'", disc_emoji_string)
    ####################
    # Step for Custom emojis: Find all elements in the strings that are like <:emoji_name:emoji_id>, or <a:emoji_name:emoji_id>
    custom_emojis = re.findall(r'<([^>]*)>', a)
    # Previous step makes a list, but list does not contain "< >" around the emojis, it looks like [:emoji_name:emoji_id, a:emoji_name:emoji_id]
    # So we get a new list with "< >" added 
    cemojilist = [''.join('<' + cemoji + '>') for cemoji in custom_emojis]
    # Combine list of custom emojis and discord emojis
    all_emojis = disc_emoji + cemojilist
    # Send a message in the chat, call it "poll"
    poll = await ctx.send("**Poll from** <@" + str(id) + ">**!!**\n"
                          ""+ a)
    # Add all the reactions in the list all_emojis to that message
    for i in all_emojis:
        try:
            await discord.Message.add_reaction(poll, i)
        except:
            print("Emoji " + i + " not found")


""" This function is to grab emojis out of text in a message and an example is shown on how to use it
def grab_emojis(message):
    demojized = emoji.demojize(message, use_aliases = True)
    custom_emojis = [''.join('<' + cemoji + '>') for cemoji in re.findall(r'<([^>]*)>', message)]
    only_disc_emojis = ' '.join([word for word in demojized.split() if word not in custom_emojis])
    discord_emoji_sep = re.findall(r":([^:]*):", only_disc_emojis)
    disc_emojis = [emoji.emojize(''.join(':' + dem + ':'), use_aliases=True) for dem in discord_emoji_sep]
    all_emojis = disc_emojis + custom_emojis
    return [emojis for emojis in all_emojis]
""" 

""" An example of how to use the function grab_emojis() from above
@client.command()
async def emojiprint(ctx, *, message):
    # grab_emojis(message)
    # print(message)
    emojis = grab_emojis(message)
    print(emojis)
    for i in emojis:
        print(i)
    msg = await ctx.send(message)
    for i in emojis:
        await discord.Message.add_reaction(msg, i)

""" 

""" Rewrite of poll command to work for flags and numbers,
not implemented because as it is it's good for laughs
@client.command()
async def pollest(ctx, *, text):
    demojized = emoji.demojize(text, use_aliases = True)
    custom_emojis = [''.join('<' + cemoji + '>') for cemoji in re.findall(r'<([^>]*)>', text)]
    only_disc_emojis = ' '.join([word for word in demojized.split() if word not in custom_emojis])
    discord_emoji_sep = re.findall(r":([^:]*):", only_disc_emojis)
    disc_emojis = [emoji.emojize(''.join(':' + dem + ':'), use_aliases=True) for dem in discord_emoji_sep]
    all_emojis = disc_emojis + custom_emojis
    msg = await ctx.send(text)
    for i in all_emojis:
        try:
            await discord.Message.add_reaction(msg, i)
        except:
            print("Emoji " + i + " not found") """
 

""" First draft of new poll command 
    demojized = emoji.demojize(text, use_aliases = True)
    custom_emojis = re.findall(r'<([^>]*)>', text)
    custom_emojis = [''.join('<' + cemoji + '>') for cemoji in custom_emojis]
    word_list = demojized.split()
    only_disc_emojis = ' '.join([word for word in word_list if word not in custom_emojis])
    discord_emoji_sep = re.findall(r":([^:]*):", only_disc_emojis)
    disc_emojis = [''.join(':' + dem + ':') for dem in discord_emoji_sep]
    emojized = [emoji.emojize(i, use_aliases=True) for i in disc_emojis]
    all_emojis = emojized + custom_emojis
    msg = await ctx.send(text)
    for i in all_emojis:
        try:
            await discord.Message.add_reaction(msg, i)
        except:
            print(i)
            print("not valid") """


# Simple coin flip
@client.command()
async def flip(ctx):
    options = ['Heads','Tails','Heads','Tails','Heads','Tails','Heads','Tails','Heads','Tails']
    selection = random.choice(options)
    await ctx.send(selection) 

# Old teams command
""" @client.command()
async def teams(ctx):
    guild = ctx.message.guild
    tk = guild.get_role(746168865737932831)
    team1 = tk.name
    tkm = tk.members
    tkmembers = [member.name for member in tk.members]
    a = ', '.join(tkmembers)
    an = str(len(tkmembers))

    ts = guild.get_role(746169087347916851)
    team2 = ts.name
    tsm = ts.members
    tsmembers = [member.name for member in ts.members]
    b = ', '.join(tsmembers)
    bn = str(len(tsmembers))

    await ctx.send(team1 + " members: ("+an+")\n" + a + "\n \n And \n \n" + team2 + " members: ("+bn+")\n" + b) """

# command to chech who is currently in team1 and team2 in server wars
@client.command()
async def teams(ctx):
    guild = ctx.message.guild
    team1 = guild.get_role(746168865737932831)
    team1_name = team1.name
    team1_members = [member.id for member in team1.members]
    team1_size = str(len(team1_members))
    if team1_size == "0":
        team1_members_at = "None"
    else:
        team1_members_at = (''.join('<@' + str(team1_id) + '> \n' for team1_id in team1_members))

    team2 = guild.get_role(746169087347916851)
    team2_name = team2.name
    tsm = team2.members
    team2_members = [member.id for member in team2.members]
    team2_size = str(len(team2_members))
    if team2_size == "0":
        team2_members_at = "None"
    else:
        team2_members_at = (''.join('<@' + str(team2_id) + '> \n' for team2_id in team2_members))
    
    embed = discord.Embed(title="Territory war!", description="Team standings in territory war.", colour=0xFF0000)
    embed.add_field(name=team1_name + " (Members: " + team1_size + ")", value=team1_members_at, inline=True)
    embed.add_field(name=team2_name + " (Members: " + team2_size + ")", value=team2_members_at, inline=True)
    await ctx.send(embed=embed)


@client.command()
async def roll(ctx, participants, winners):
    command_user = ctx.message.author
    if participants.isnumeric() and winners.isnumeric():
        if int(participants) > 50:
            await ctx.send("We aren't that many on the server! <a:RSus:707927630787117157>")
        elif int(winners) == 0:
            await ctx.send("<a:RWalkAway:710069239607722065>")
        elif int(participants) == 0:
            if int(winners) > int(participants):
                await ctx.send("<a:RSadBye:718753982360584212> No one entered... and you still tried to pick a winner <a:RSus:707927630787117157>")
            else:
                await ctx.send("<a:RSadBye:718753982360584212> No one entered")
        else:
            if int(participants) < int(winners):
                await ctx.send("<:RJudge:703166590702714950> There aren't that many entrants.")
            elif int(participants) == int(winners):
                await ctx.send("<a:RSaber:710692428025299024> EVERYONE WINS! <a:RSaber:710692428025299024>")
            else:
                a = random.sample(range(1,(int(participants)+1)),int(winners))
                a = sorted(a, key=int)
                winner_numbers = [str(winner) for winner in a]
                winner_numbers = ', '.join(winner_numbers)
                ferro_message = await ctx.send("Congratulations to: "+ winner_numbers)
                await discord.Message.add_reaction(ferro_message, "<:RParty:706007725070483507>")
    else:
        await ctx.send("<a:RQuestion:713380476357705740> Did you input (positive) numbers?")

# Command to delete the last messages in a channel, specify in amount
# Only accessible to admins
@client.command()
async def clearup(ctx, amount):
    amount = int(amount)
    user = ctx.message.author.id
    a = ctx.message
    chan = ctx.channel
    if user in admin_users_id:
        await discord.Message.delete(a)
        await chan.purge(limit=amount)
    else:
        b = await ctx.send("Sorry, you can't do that")
        time.sleep(2)
        await discord.Message.delete(a)
        await discord.Message.delete(b)


# @client.command()
# async def gibway(ctx, *, message):
#     user = ctx.message.author
#     command_message = ctx.message
#     channel_id = ctx.message.channel.id
#     await discord.Message.delete(command_message)
#     if channel_id == 738391260662071359:
#         gibway_message = await ctx.send("**giveaway from <@"+str(user.id)+"> !!**\n"+message)
#         await gibway_message.pin()
#         await user.send("Thank you for doing the giveaway."
#                         "\n```"+message+"```\n"
#                         "When you want to select winner(s), use this command"
#                         "\n`command_name x message_id`, where x is the amount of winners you are selecting.\n"
#                         "\nThe message id you need to put in is:")
#         await user.send(gibway_message.id)
#     else:
#         await ctx.send("<a:RHype:708568633508364310> Thanks for wanting to do a giveaway, but you need to do it in <#738391260662071359>."
#                         "\nYour message was deleted, but I sent it to you so you can copy it to the right channel!")
#         await user.send(message)


@client.command()
async def oldroll(ctx, wnr_amount, msg_id):
    command_user = ctx.message.author
    channel_id = 738391260662071359
    channel = client.get_channel(channel_id)
    message_id = msg_id
    message = await  channel.fetch_message(message_id)
    if wnr_amount.isnumeric():
        if int(wnr_amount) < 1:
            await ctx.send("why would you do that :(")
        else:
            await command_user.send("Thank you for being so awesome!")
            for reaction in message.reactions:
                user_list = [user async for user in reaction.users()]
                participants = int(len(user_list))
                if int(wnr_amount) > int(participants):
                    winner = random.sample(user_list, k=int(participants))
                    winner_names = ', '.join([winner.name for winner in winner])
                    winner_id = ', '.join([''.join('<@' + str(winner.id) + '>') for winner in winner])
                else:
                    winner = random.sample(user_list, k=int(wnr_amount))
                    winner_names = ', '.join([winner.name for winner in winner])
                    winner_id = ', '.join([''.join('<@' + str(winner.id) + '>') for winner in winner])
                await command_user.send("\n"+str(participants) + " participants for the emoji: "+ str(reaction) + "\nWinner name(s):\n"
                            + str(winner_names)+"\nWinner ID:\n```"+str(winner_id) + "```")
    else:
        await ctx.send("What, you want **" + wnr_amount + "** winner(s)? Maybe try a (positive) number?")
    await message.unpin()


# Command to repost attachments but with spoiler, will delete command post
@client.command()
async def spoiler(ctx, *text):
    poster = ctx.message.author.id
    files = []
    for file in ctx.message.attachments:
        fp = BytesIO()
        await file.save(fp)
        files.append(discord.File(fp, filename=file.filename, spoiler=True))
    if text:
        message_content = text
        message_content = ' '.join(message_content)
    else:
        message_content = ""
    await discord.Message.delete(ctx.message)
    await ctx.send("Sent by <@"+str(poster)+">\n"+str(message_content), files=files)


@client.command()
async def gibroll(ctx, *wnr_amount):
    guild = ctx.message.guild
    raffle_channel = discord.Guild.get_channel(guild, channel_id=766277566934810634)
    # print(raffle_channel)
    command_user = ctx.message.author
    message = await  raffle_channel.history().find(lambda m: m.author.id == command_user.id)
    keyword = 'raffle time!'
    if wnr_amount:
        wnr_amount = wnr_amount[0]
    else:
        wnr_amount = "1"

    if wnr_amount.isnumeric():
        if keyword in message.content.lower():
            if int(wnr_amount) < 1:
                await ctx.send("why would you do that :(")
            else:
                await command_user.send("Thank you for being so awesome!")
                for reaction in message.reactions:
                    user_list = [user async for user in reaction.users()]
                    participants = int(len(user_list))
                    if int(wnr_amount) > int(participants):
                        winner = random.sample(user_list, k=int(participants))
                        winner_names = ', '.join([winner.name for winner in winner])
                        winner_id = ', '.join([''.join('<@' + str(winner.id) + '>') for winner in winner])
                    else:
                        winner = random.sample(user_list, k=int(wnr_amount))
                        winner_names = ', '.join([winner.name for winner in winner])
                        winner_id = ', '.join([''.join('<@' + str(winner.id) + '>') for winner in winner])
                    await command_user.send("\n"+str(participants) + " participants for the emoji: "+ str(reaction) + "\nWinner name(s):\n"
                                + str(winner_names)+"\nWinner ID:\n```"+str(winner_id) + "```")
        else:
            await ctx.send("Sorry, I can't find your message in <#766277566934810634>. Does it have the keyword: " + keyword + ""
                       "\nI can only see your last message, you can edit the message to add the keyword though!")
    else:
        await ctx.send("What, you want __**" + wnr_amount + "**__ winner(s)? Maybe try a (positive) number?")




########################################################
########################################################
# Work in progress:

@client.command()
async def sprite(ctx, pkmn, *shiny):
    with open(r"./data/pokemon.json", "r") as read_file:
        data = json.load(read_file)
    # print(type(data[0]))
    pokemon = (pkmn.lower()).title()
    for i in range(0, len(data)):
        pokemon_dict = data[i]
        # print(pokemon_dict)
        if pokemon in (pokemon_dict.values()):
            # print("Egg groups: " + pokemon_dict['eggGroup1'] + ", " + pokemon_dict['eggGroup2'])
            # print(pokemon)    
            if shiny:
                if shiny[0] == "*" or shiny[0].lower() == "shiny":
                    folder = "shiny"
                else:
                    folder = "normal"
            else:
                folder = "normal"
            await ctx.send("https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon.lower() +".png")

@client.command(name = 'dex', aliases = ['pokedex'])
async def dex(ctx, pkmn):
    ability_check = ['ability1', 'ability2', 'abilityH']
    egg_group_check = ['eggGroup1', 'eggGroup2']
    typing_check = ['type1', 'type2']
    with open(r"./data/pokemon.json", "r") as read_file:
        data = json.load(read_file)
    pokemon = (pkmn.lower()).title()
    for i in range(0, len(data)):
        pkmn_info = data[i]
        if pokemon in (pkmn_info.values()):
            abilities_dict = pkmn_info["abilities"]
            ability_list = [abilities_dict[ability] for ability in ability_check if abilities_dict[ability] is not None]
            # Construction depending on 2 or 3 abilities
            if len(ability_list) == 3:
                ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
                ability_2 = "Ability 2: `" + ability_list[1] + "`\n"
                ability_h = "Ability H: `" + ability_list[2] + "`"
                ability = ability_1 + ability_2 + ability_h
            elif len(ability_list) == 2:
                ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
                ability_h = "Ability H: `" + ability_list[1] + "`\n"
                ability = ability_1 + ability_h
            else:
                ability = "Ability 1: `" + ability_list[0] + "`\n"
            
            typing_list = [pkmn_info[typing] for typing in typing_check if pkmn_info[typing] is not None]
            # Adjust for single or dual type
            if len(typing_list) == 1:
                typing = "Type: `" + typing_list[0] + "`"
            else:
                typing = "Type: `" + typing_list[0] + "/" + typing_list[1] + "`"
            
            egg_groups = ', '.join([pkmn_info[group] for group in egg_group_check if pkmn_info[group] is not None])
            catch_rate = "Catch rate: `" + str(pkmn_info["catchRate"]) + "`"
            base_stats = pkmn_info["baseStats"]
            stats = ["hp", "atk", "def", "spA", "spD", "spe", "tot"]
            stat_value = [base_stats[stat] for stat in stats]

            dens = pkmn_info["dens"]
            sword_dens_list = dens["sword"]
            sword_dens = ', '.join(sword_dens_list[i] for i in range(0, len(sword_dens_list)) if len(sword_dens_list) is not None)
            shield_dens_list = dens["shield"]
            shield_dens = ', '.join(shield_dens_list[i] for i in range(0, len(shield_dens_list)) if len(shield_dens_list) is not None)
            folder = "normal"

            embed = discord.Embed(title="__#" + str(pkmn_info["dexId"]) +  " " + pokemon.title() + "__", colour=0xFF0000)
            embed.add_field(name="Misc. Info", value=typing + "\n" + catch_rate + "\nEgg Groups: `" + egg_groups + "`\n")
            embed.add_field(name="Abilities", value=ability, inline=True)
            embed.add_field(
                name="Base stats: ",
                value="__`HP     Atk     Def`__\n"+""
                "__`"+ f"{str(stat_value[0]):<7}" + f"{str(stat_value[1]):<8}" + f"{str(stat_value[2]):<3}" + "`__\n"
                "__`SpA    SpD     Spe`__\n"
                "__`"+ f"{str(stat_value[3]):<7}" + f"{str(stat_value[4]):<8}" + f"{str(stat_value[5]):<3}" +"`__\n"
                "__`Total: " + str(stat_value[6]) + "`__")
            # rewrite this part
            if len(sword_dens_list) != 0 or len(shield_dens_list) != 0:
                embed.add_field(name="Dens", value="Sword: " + str(sword_dens) + "\nShield: " + str(shield_dens) + "", inline=False)

            embed.set_image(url="https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon.lower() +".png")
            
            await ctx.send(embed=embed)







### SO Helping
# @client.command()
# async def comm(ctx):
    # guild = ctx.message.guild
    # general = discord.utils.get(client.get_all_channels(), name='a-bot-testing-channel')
    # general = discord.utils.get(ctx.guild.channels, name='a team kyle channel')
    # print(general)
    # name = 'A Seed Checking Category'
    # category = discord.utils.get(ctx.guild.categories, name=name)
    # print(category)
    # channels = category.channels
    # for channel in channels:
    #     print(channel.members)
    #     for member in channel.members:
    #         print(member)
            # await member.move_to(general)
        # await channel.delete()

# Add custom commands over this
########################################################
########################################################

@client.command()
async def test(ctx):
	while True:
		print("Hello!")
		await asyncio.sleep(1)
		return
	
@client.command()
async def load(extension):
	try:
		client.load_extension(extension)
		print('Loaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(extension):
	try:
		client.unload_extension(extension)
		print('Unloaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be unloaded. [{}]'.format(extension, error))

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
    
    #Reaction colour start
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
    pin_msg_user = [pin_msg.author.id]
    pin_msg_user = [pin_msg.author.id]
    if payload.emoji.name == "📌":
        pin_guild_id = payload.guild_id
        pin_guild = discord.utils.find(lambda g :g.id == pin_guild_id, client.guilds)
        pin_reactor = discord.utils.find(lambda m : m.id == payload.user_id, pin_guild.members)
        pin_reactor_id = int(pin_reactor.id)
        # valid_users = pin_msg_user + admin_users_id
        # valid_users_test = all(user != pin_reactor_id for user in valid_users)
        # if valid_users_test == False:
        await pin_msg.pin()


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
    pin_msg_user = [pin_msg.author.id]
    if payload.emoji.name == "📌": 
        pin_guild_id = payload.guild_id
        pin_guild = discord.utils.find(lambda g :g.id == pin_guild_id, client.guilds)
        pin_reactor = discord.utils.find(lambda m : m.id == payload.user_id, pin_guild.members)
        pin_reactor_id = int(pin_reactor.id)
        # valid_users = pin_msg_user + admin_users_id
        # valid_users_test = all(user != pin_reactor_id for user in valid_users)
        # if valid_users_test == False: # use this if you want only message author and admins to be able to unpin
        await pin_msg.unpin()

'''
#####################
Reaction events end
#################
'''



if __name__ == '__main__':
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print('{} cannot be loaded. [{}]'.format(extension, error))

	#client.loop.create_task(test())
	client.run(TOKEN)
