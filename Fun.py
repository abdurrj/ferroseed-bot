from bot import *
from datetime import date, timedelta, datetime
import pytz
import time

class Fun(commands.Cog):
    def __init__(self, client):
        self.userChannel = None
        self.user = None
        self.id = None
        self.person = None
        self.idInt = None


    # Caught
    @commands.command(pass_context=True, name = 'caught', aliases=['c', 'catch', 'CAUGHT', 'CATCH', 'CAUGHT!', 'caught!', 'catch!', 'CATCH!'])
    async def caught(self, ctx, *ball):
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
    @commands.command(pass_context=True, name = 'naught', aliases=['not'])
    async def naught(self, ctx):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        embed = discord.Embed(
        colour = discord.Colour.red())
        embed.add_field(name='<:sherbSad:732994987683217518> escaped', value="<@"+str(id)+"> did not catch the pokemon.", inline=True)
        a = await ctx.send(embed=embed)
        await discord.Message.add_reaction(a, "<:ferroSad:735707312420945940>")


    @commands.command()
    async def hi(self, ctx):
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


    @commands.command(pass_context=True)
    async def pet(self, ctx):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        petpet = randrange(12)  # randrange(*), increase * value to increase chance of petting Ferroseed
        if petpet >= 5:         # petpet >= **: Lower the number on ** to increase chance of petting Ferroseed (standard is 6)
            with open(r"data/txt/ferropet.txt", "r+") as fpet:
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
            with open(r"data/txt/ferrohurt.txt", "r+") as fhurt:
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


    @commands.command()
    async def pets(self, ctx):
        with open(r"data/txt/ferropet.txt", "r+") as fpet:
            petcount = fpet.read()
        with open(r"data/txt/ferrohurt.txt", "r+") as fhurt:
            hurtcount = fhurt.read()
        await ctx.send("I've been pet **"+petcount+"x** times and I've hurt you **"+hurtcount+"x** times")


    @commands.command()
    async def birbpet(self, ctx):
        await ctx.send("<a:PetTheBirb:754269160598536214>")


    # Go to sleep commands
    @commands.command()
    async def sleep(self, ctx, str):
        await ctx.send("Go to sleep, "+str+" <a:RBops2:718139698912034937>")


    # Work command
    @commands.command(name = 'work', aliases=['homework'])
    async def work(self, ctx, str):
        choice = [1,2,3,4,5,6,7,8,9,10]
        selection = random.choice(choice)
        if selection >= 6:
            await ctx.send("<a:RBops:718139734693773330> "+str+"! Go be productive.")
        else:
            await ctx.send(str+"! Go do the things. <:RStudy:762627515747008512>")


    @commands.command()
    async def absleep(self, ctx):
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


    # Write a better code!
    @commands.command()
    async def time(self, ctx):
        timezones = ['Singapore', 'Europe/Oslo', 'Europe/Lisbon','Canada/Newfoundland', 'US/Eastern', 'US/Central','US/Pacific']
        timezone_names = ['Malaysia', 'Central Europe', 'West Europe', 'Newfoundland', 'US Eastern', 'US Central', 'US Pacific']

        output = []
        # only_tz_name = []
        # only_tz_time = []
        for i in range(0,len(timezones)):
            tz = timezones[i]
            tz = pytz.timezone(tz)
            tz_name = timezone_names[i]
            tz_hour = datetime.now(tz).strftime("%H")
            if int(tz_hour) < 5 or int(tz_hour)>22:
                time = datetime.now(tz).strftime("%I:%M %p") + ". <a:RSleep:718830355381223444>"
            else:
                time = datetime.now(tz).strftime("%I:%M %p") + ""
            
            timezone_time = tz_name + "\n" + time
            # only_tz_name.append(tz_name)
            # only_tz_time.append(time)
            output.append(timezone_time)

        times = '\n\n'.join(i for i in output)
        # only_tz_name = '\n'.join(i for i in only_tz_name)
        # only_tz_time = '\n'.join(i for i in only_tz_time)

        embed = discord.Embed(title='Afss time!  🌎🌍🌏', color=discord.Colour.green())
        embed.add_field(name='Time:', value=times, inline=True)
        # embed.add_field(name="Time zone:" value=only_tz_name)
        # embed.add_field(name="Time:", value=only_tz_time)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
