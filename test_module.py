from bot import *
import json

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
        print(self.user)

    @commands.command()
    async def emojiprint(self,ctx, *, message):
        print(message)

    @commands.command()
    async def fc_new(self, ctx, *usid):
        with open(r"data/json/fc.json", encoding='utf-8') as fc_dict:
            fc_dict = json.load(fc_dict)
        print(fc_dict)
        if usid:
            usid = int(''.join(i for i in usid[0] if i.isdigit()))
        else:
            usid = ctx.message.author.id

        if str(usid) in fc_dict:
            user_dict = fc_dict[str(usid)]
            user_dict_keys = list(user_dict.keys())
            # print(user_dict_keys)
            info = ""
            for i in user_dict_keys:
                info = info + "\n" + i + ": **" + user_dict[i] + "**" 
        
        print(info)
        await ctx.send(info)

    @commands.command()
    async def fcc(self, ctx, *, arg):
        arg_split = arg.split(" ")
        check = arg_split[0]
        text = arg.split(' ', 1)[1]
        key = (text.split(',')[0]).strip
        with open(r"data/json/fc.json", encoding='utf-8') as fc_dict:
            fc_dict = json.load(fc_dict)
        
        usid = str(ctx.message.author.id)

        if usid in fc_dict.keys():
            user_dict = fc_dict[str(usid)]
        else:
            fc_dict[str(usid)] = {}
            user_dict = fc_dict[str(usid)]
        
        if check == "change" or check == "add":
            value = (text.split(',', 1)[1]).strip()
            user_dict[key] = value
            # print(user_dict)
        elif check == "remove":
            del user_dict[key]
        
        else:
            print("nothing to do")

        fc_dict[str(usid)] = user_dict
        new_dict = fc_dict

        with open("data/json/fc.json", "w", encoding='utf-8') as fc_dict:
            json.dump(new_dict, fc_dict, indent=4, ensure_ascii=False)


def setup(client):
    client.add_cog(test_module(client))
