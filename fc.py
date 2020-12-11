from bot import *
import json
from discord.utils import get, find
import re

class fc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fc_old(self, ctx, *args):
        filename = r"data/csv/friendcodes.csv"
        df = pd.read_csv(filename)
        if args:
            userid = int(''.join(i for i in args[0] if i.isdigit()))
        else:
            userid = ctx.message.author.id
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            if row["usid"] == int(userid):
                await ctx.send((row[2] + "\n" + row[3] + "\n" + row[4] + "\n" + row[5] +  "\n" + row[6] +  "\n" + row[7]))

    @commands.command()
    async def fc(self, ctx, *usid):
        with open(r"data/json/fc.json", encoding='utf-8') as fc_dict:
            fc_dict = json.load(fc_dict)

        if usid:
            usid = int(''.join(i for i in usid[0] if i.isdigit()))
        else:
            usid = ctx.message.author.id

        if str(usid) in fc_dict:
            user_dict = fc_dict[str(usid)]
            user_dict_keys = list(user_dict.keys())
            info = ""
            for i in user_dict_keys:
                info = info + "\n" + i + ": **" + user_dict[i] + "**" 

        await ctx.send(info)

    @commands.command()
    async def fcc(self, ctx, *, arg):
        arg_split = arg.split(" ")
        check = arg_split[0]
        text = arg.split(' ', 1)[1]
        key = (text.split(',')[0]).strip()
        with open(r"data/json/fc.json", encoding='utf-8') as fc_dict:
            fc_dict = json.load(fc_dict)
        
        usid = str(ctx.message.author.id)

        if usid in fc_dict.keys():
            user_dict = fc_dict[str(usid)]
        else:
            fc_dict[str(usid)] = {}
            user_dict = fc_dict[str(usid)]
        
        if check == "add" or check == "edit":
            value = (text.split(',', 1)[1]).strip()
            user_dict[key] = value

        elif check == "remove":
            check_del = await ctx.send("Are you sure you want to delete\n"+key+": **"+user_dict[key]+"**")
            emoji_list = ['✅','❌']
            for i in emoji_list:
                await check_del.add_reaction(i)

            def checker(reaction, user):
                return user == ctx.author and str(reaction.emoji) in emoji_list

            while True:
                try:
                    reaction, user = await self.client.wait_for("reaction_add", timeout=15, check=checker)

                    if str(reaction.emoji) == "✅":
                        await  discord.Message.delete(check_del)
                        del user_dict[key]
                        await ctx.send("Deleted")
                        break

                    elif str(reaction.emoji) == "❌":
                        await  discord.Message.delete(check_del)
                        await ctx.send("Not deleted")
                except:
                    print("nothing")
                        
        elif check == "key":
            list(user_dict.keys())
            for i in user_dict:
                if i.startswith(key):
                    key = i
            new_key = (text.split(',')[1]).strip()
            new_user_dict = user_dict
            dict_info = new_user_dict.pop(key)
            new_user_dict[new_key] = dict_info
            user_dict = new_user_dict
        else:
            print("nothing to do")
            await ctx.send(
                "I'm not sure what you want me to do <:thonk:733808013046972467>"
            )
            return

        fc_dict[str(usid)] = user_dict
        new_dict = fc_dict

        try:
            with open("data/json/fc_test.json", "w", encoding='utf-8') as fc_dict:
                json.dump(new_dict, fc_dict, indent=4, ensure_ascii=False)
                proceed = "yes"
        except:
            proceed = "false"
        
        if proceed == "yes":
            with open("data/json/fc.json", "w", encoding='utf-8') as fc_dict:
                json.dump(new_dict, fc_dict, indent=4, ensure_ascii=False, sort_keys=True)
            await ctx.send("fc updated")
        else:
            print("something went wrong, fc not updated")


def setup(client):
    client.add_cog(fc(client))