from bot import *
import random
import emoji
import re
import asyncio
import sys

class Functions(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearup(self, ctx, amount:int=0):
        await ctx.message.delete()
        await ctx.message.channel.purge(limit=amount)


    @commands.command()
    async def flip(self, ctx):
        options = ['Heads','Tails','Heads','Tails','Heads','Tails','Heads','Tails','Heads','Tails']
        selection = random.choice(options)
        await ctx.send(selection) 


    @commands.command()
    async def poll(self, ctx, *, text):
        id = ctx.message.author.id
        a = text
        emoji_init_string = str(emoji.emoji_lis(a))
        disc_emoji_sep = re.findall(r"':([^:']*):'", emoji.demojize(emoji_init_string))
        disc_emoji_string = emoji.emojize(str([''.join(':' + demoji + ':') 
                                        for demoji in disc_emoji_sep]))
        disc_emoji = re.findall(r"'([^']*)'", disc_emoji_string)
        custom_emojis = re.findall(r'<([^>]*)>', a)
        cemojilist = [''.join('<' + cemoji + '>') for cemoji in custom_emojis]
        all_emojis = disc_emoji + cemojilist
        poll = await ctx.send("**Poll from** <@" + str(id) + ">**!!**\n"
                            ""+ a)
        for i in all_emojis:
            try:
                await poll.add_reaction(i)
            except:
                print("Emoji " + i + " not found")


    @commands.command()
    async def spoiler(self, ctx, *text):
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
        await ctx.message.delete()
        await ctx.send("Sent by <@"+str(poster)+">\n"+str(message_content), files=files)


    @commands.command()
    async def teams(self, ctx):
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


    @commands.command()
    async def gibroll(self, ctx, *wnr_amount):
        guild = ctx.message.guild
        raffle_channel = discord.Guild.get_channel(guild, channel_id=766277566934810634)
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
                        seed = random.randrange(sys.maxsize)
                        random.Random(seed)
                        user_list = [user async for user in reaction.users()]
                        print(user_list)
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


    # Check if this command is still in use. Remove if it is not
    @commands.command()
    async def roll(self, ctx, participants, winners):
        # command_user = ctx.message.author
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

    @commands.command()
    async def set_game(self, ctx, a=None):
        activity = discord.Game(a)
        await self.client.change_presence(activity=activity)

    @commands.command()
    async def stop_game(self, ctx):
        await self.client.change_presence(activity=None)

    @commands.command()
    async def set_watching(self, ctx, w=None):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=w))


    # Remove this if it has no more use
    @commands.command()
    async def oldroll(self, ctx, wnr_amount, msg_id):
        command_user = ctx.message.author
        print(command_user)
        guild = ctx.message.guild
        channel_id = 766277566934810634
        channel = discord.Guild.get_channel(guild, channel_id=channel_id)
        print(channel)
        message_id = msg_id
        message = await  channel.fetch_message(message_id)
        if wnr_amount.isnumeric():
            if int(wnr_amount) < 1:
                await ctx.send("why would you do that :(")
            else:
                await command_user.send("Thank you for being so awesome!")
                for reaction in message.reactions:
                    seed = random.randrange(sys.maxsize)
                    random.Random(seed)
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


def setup(client):
    client.add_cog(Functions(client))
