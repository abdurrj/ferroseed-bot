from bot import *

class test_module(commands.Cog):
    def __init__(self, client):
        # self.checkDataReady.start()
        self.userChannel = None
        self.user = None
        self.id = None
        self.person = None
        self.idInt = None

    @commands.command()
    async def testcommand(self, ctx):
        print("testing, testing.. 1.. 2... 3... 4?")

def setup(client):
    client.add_cog(test_module(client))
