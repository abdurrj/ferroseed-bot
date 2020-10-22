# from discord.ext import tasks, commands
# import discord
from bot import *
# from seed.XoroShiro import *
# from seed.framecalc import framecalc
# from seed.seedgen import *
# from seed.GetPokeInfo import *
# from seed.Person import *
# from seed.ArrayQueue import *
# from datetime import date, timedelta
# from seed import XoroShiro
# import time

# 300 with the current queue and the reporting system
# will make sure everyone has a place and can see when they will be served
# q = ArrayQueue(300)

# until possible merge and improvement, setting it to 20 as from the previous commits
# q = ArrayQueue(20)

class RaidCommands(commands.Cog):
    def __init__(self, client):
        # self.checkDataReady.start()
        self.userChannel = None
        self.user = None
        self.id = None
        self.person = None
        self.idInt = None

    #Clears instance variables        Is this even necessary?
    # def clearData(self):
    #     self.userChannel = None
    #     self.user = None
    #     self.id = None
    #     self.idInt = None
    #     self.person = None

    #Generates the appropriate string based on your star and square frames
    def generateFrameString(self, starFrame, squareFrame):
        pass

    #Reports how many people are in the queue
    @commands.command(name="CheckQueueSize")
    async def checkQueueSize(self, ctx):
        pass

    #Reports where the sender is in the queue
    @commands.command(name="CheckMyPlace")
    async def checkMyPlace(self, ctx):
        pass

    @commands.command(name="seed") #CheckMySeed was the original code, then checkmyseed, use whatever is easiest
    async def checkMySeed(self, ctx):
        pass

    @tasks.loop(seconds=0.1)
    async def checkDataReady(self):
        pass

    @commands.command(name='GetSeed')
    async def obtainSeed(self, ctx, arg1=None, arg2=None, arg3=None):
        pass

    @commands.command(name='GetFrameData')
    async def obtainFrameData(self, ctx, arg1=None):
        pass
        

def setup(client):
    client.add_cog(RaidCommands(client))
