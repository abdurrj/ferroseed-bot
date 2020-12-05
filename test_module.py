from bot import *
from discord.utils import get, find
import datetime
import random

class test_module(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def nicktest(self, ctx):
        user = ctx.message.author
        if user.nick:
            print(user.nick)
        else:
            print(user.name)


    @commands.command()
    async def testcommand(self, ctx):
        print("testing, testing.. 1.. 2... 3... 4?")

    @commands.command()
    async def emojiprint(self,ctx, *, message):
        print(message)

    @commands.command()
    async def user_react(self, ctx):
        message = ctx.message
        embed = discord.Embed(title='General Information', color=16769251)
        embed.set_footer(text='General information')
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name='Text Header ', value="all_lines[1]", inline=False)
        embed.add_field(name='Text Header 2: ', value="all_lines[2]", inline=False)
        embed.add_field(name='Accepted Users: ', value='HERE ALL USERS WITH ✅', inline=False)
        mess = await ctx.send(embed=embed)
        emoji_list = ['✅', '❌']
        for i in emoji_list:
            await mess.add_reaction(i)

        while True:
            users = ""
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=60)
                if str(reaction) == "✅":
                    mess = await ctx.channel.fetch_message(mess.id)
                    for reactions in mess.reactions:
                        if str(reactions) == "✅":
                            user_list = [user async for user in reactions.users() if user != self.client.user]
                            for user in user_list:
                                users = users + user.mention + "\n"

                    embed_1 = discord.Embed(title='General Information', color=16769251)
                    embed_1.set_footer(text='General information')
                    embed_1.set_thumbnail(url=message.guild.icon_url)
                    embed_1.add_field(name='Text Header ', value="all_lines[1]", inline=False)
                    embed_1.add_field(name='Text Header 2: ', value="all_lines[2]", inline=False)
                    embed_1.add_field(name='Accepted Users: ', value='HERE ALL USERS WITH ✅\n'+users, inline=False)
                    await mess.edit(embed = embed_1)
            except asyncio.TimeoutError:
                await mess.edit(embed = embed_1)
                break


    @commands.command()
    async def alarm(self, ctx, m:int=0, s:int=0):
        message = await ctx.send("alarm will ring in: {:02d}:{:02d}".format(m,s))
        alarmtime = m*60 + s
        while alarmtime>0:
            minutes, seconds = divmod(alarmtime, 60)
            timeformat = "{:02d}:{:02d}".format(minutes, seconds)
            alarmtime -=5
            await message.edit(content="alarm will ring in: "+timeformat)
            await asyncio.sleep(5)
        
        minutes, seconds = divmod(alarmtime, 60)
        timeformat = "{:02d}:{:02d}".format(minutes, seconds)
        await message.edit(content="alarm will ring in: "+timeformat)
        await ctx.send("ringringring {}".format(ctx.author.mention))

    @commands.command()
    async def reactiontest(self, ctx, set_time:int):
        my_msg = await ctx.send("Hello")
        await my_msg.add_reaction("🎉")
        await asyncio.sleep(set_time)
        new_msg = await ctx.channel.fetch_message(my_msg.id)
        user_list = [u for u in await new_msg.reactions[0].users().flatten() if u != self.client.user]
        if len(user_list) == 0:
            await ctx.send("No one reacted.")
        else:
            winner = random.choice(user_list)
            # await ctx.send(f"{winner.mention}")
            e = discord.Embed()
            e.title = "Giveaway ended!"
            e.description = f"You won:"
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text=f'{self.client.user.name}',
                         icon_url=self.client.user.avatar_url)
            await ctx.send(f"{winner.mention}", embed=e)


    @commands.command()
    async def channeltester(self, ctx, channel_name:str):
        guild = ctx.message.guild
        raider_role = guild.get_role(746168865737932831)
        # bot_user = guild.get_role(741695006221271130)
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        raider_role: discord.PermissionOverwrite(read_messages=True),
        self.client.user: discord.PermissionOverwrite(read_messages=True)
        }
        raid_category = self.client.get_channel(734492166365380608)
        await guild.create_text_channel(channel_name, category=raid_category, overwrites=overwrites)




"""     @commands.command()
    async def reactrole(self, ctx, reaction, role):
        guild = ctx.message.guild
        with open(r"data/json/reactrole.json", encoding='utf-8') as react_role_dict:
            react_role_dict = json.load(react_role_dict)

        if reaction.startswith('<'):
            reaction_name = re.findall(r":([^:]*):", reaction)
            reaction_name = reaction_name[0]
        
        key = reaction_name
        if key in react_role_dict.keys():
            await ctx.send("Emoji already in use")
        else:
            value = ''.join(i for i in role if i.isdigit())
            try:
                role = discord.utils.get(guild.roles, id = int(value))
            except:
                await ctx.send("No role found")
                role = None
            
            if role is not None:
                role_name = role.name
                role_info_list = [role_name, value]
                if role_info_list in react_role_dict.values():
                    await ctx.send("This role is already registered")
                else:
                    react_role_dict[key] = role_info_list
                    new_dict = react_role_dict

                    with open(r"data/json/reactrole.json", "w", encoding='utf-8') as react_role_dict:
                        json.dump(new_dict, react_role_dict, indent=4, ensure_ascii=False)

                    react_channel = self.client.get_channel(734492297206431753)
                    react_message = await react_channel.fetch_message(774606488701763584)
                    try:
                        await discord.Message.add_reaction(react_message, reaction)
                    except:
                        await ctx.send("I can't react with that emoji. It's been added to the system, but you have to react manually")
            else:
                print("operatio rolereact cancelled, no role found")
        # print(message.content)  """


"""     @commands.command()
    async def reactrolechange(self, ctx, oldkey, newkey):
        with open(r"data/json/reactrole.json", encoding='utf-8') as react_role_dict:
            react_role_dict = json.load(react_role_dict)
        
        if oldkey.startswith('<'):
            oldkey = re.findall(r":([^:]*):", oldkey)
            oldkey = oldkey[0]

        if newkey.startswith('<'):
            newkey = re.findall(r":([^:]*):", newkey)
            newkey = newkey[0]

        new_rr_dict = react_role_dict
        dict_info = new_rr_dict.pop(oldkey)
        new_rr_dict[newkey] = dict_info

        with open(r"data/json/reactrole.json", "w", encoding='utf-8') as react_role_dict:
            json.dump(new_rr_dict, react_role_dict, indent=4, ensure_ascii=False) 

 """


def setup(client):
    client.add_cog(test_module(client))
