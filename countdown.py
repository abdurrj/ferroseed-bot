from discord.ext import tasks, commands
import asyncio

class countdown(commands.Cog):
    def __init__(self, client):
        self.time_left = 0
        self.countdown.start()

    @commands.command(name='seconds')
    async def add_seconds(self, ctx, sec:int=0):
        self.time_left += sec

    @commands.command(name='minutes')
    async def add_minutes(self, ctx, minutes:int=0):
        self.time_left += minutes*60

    @commands.command()
    async def view_time(self, ctx):
        if self.time_left == 0:
            await ctx.send("00:00")
        else:
            minutes, seconds = divmod(self.time_left, 60)
            timeformat = "{:02d}:{:02d}".format(minutes, seconds)
            message = await ctx.send(timeformat)
            i = 5
            while i>0:
                i -= 1
                minutes, seconds = divmod(self.time_left, 60)
                timeformat = "{:02d}:{:02d}".format(minutes, seconds)
                await message.edit(content=timeformat)
                await asyncio.sleep(1)
            await message.delete()


    @tasks.loop(seconds=1)
    async def countdown(self):
        if self.time_left>0:
            self.time_left -= 1


def setup(client):
    client.add_cog(countdown(client))
