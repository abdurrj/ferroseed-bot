from bot import *
# 300 with the current queue and the reporting system
# will make sure everyone has a place and can see when they will be served
# q = ArrayQueue(300)

# until possible merge and improvement, setting it to 20 as from the previous commits

class Den(commands.Cog):
    def __init__(self, client):
        self.userChannel = None
        self.user = None
        self.id = None
        self.person = None
        self.idInt = None


    @commands.command()
    async def denlist(self, ctx):
        await ctx.send("<https://www.serebii.net/swordshield/maxraidbattledens.shtml>")


    @commands.command()
    async def newden(self, ctx, *args):
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


    @commands.command()
    async def den(self, ctx, pkmn, *form_input):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        user = ctx.message.author.name
        with open(r"data/json/pokemon.json", "r") as read_file:
            data = json.load(read_file)
        pokemon = str((pkmn.lower()).title())
        wrong_den_message = "That's not a den, "+str(user)+"! <a:RBops2:718139698912034937>. Only from 1 to 197, or promo <a:RHype:708568633508364310>"
        if form_input:
            if (form_input[0].lower()).title() in ["Galarian", "Galar"]:
                pokemon = "Galarian " + pokemon
            else:
                pokemon = pokemon
        else:
            pokemon = pokemon

        possible_names = []
        for i in range(0, len(data)):
            pkmn_info = data[i]
            if pkmn_info['name'].startswith(pokemon):
                poke_name = pkmn_info['name']
                possible_names.append(poke_name)
        
        if len(possible_names) != 0:
            pokemon_lookup = possible_names[0]
        else:
            pokemon_lookup = "notarealpokemon"
        

        if pkmn.isnumeric():
            b = int(pkmn)
            if b >=1 and b <198:
                await ctx.send("<https://www.serebii.net/swordshield/maxraidbattles/den"+str(b)+".shtml>")
            else:
                await ctx.send(wrong_den_message)
        else:
            if pkmn.lower() == 'promo':
                await ctx.send("<https://www.serebii.net/swordshield/wildareaevents.shtml>")
            elif len(possible_names) != 0:
                for i in range(0, len(data)):
                    pkmn_info = data[i]
                    if pokemon_lookup in (pkmn_info.values()):
                        pokemon_name = pkmn_info["name"]
                        dens = pkmn_info["dens"]
                        sword_dens_list = dens["sword"]
                        shield_dens_list = dens["shield"]
                        sword_dens = ', '.join(sword_dens_list[i] for i in range(0, len(sword_dens_list)) if len(sword_dens_list) is not None)
                        shield_dens = ', '.join(shield_dens_list[i] for i in range(0, len(shield_dens_list)) if len(shield_dens_list) is not None)
                        dencheck = sword_dens + shield_dens
                        if dencheck == "":
                            print("No dens")
                            await ctx.send("Sorry, I can't find it in any den")
                        else:
                            dens = pokemon_name.title() + " is in these dens:\nSword: " + sword_dens + "\nShield: " + shield_dens
                            await ctx.send(dens)
            else:
                await ctx.send(wrong_den_message + " " + 'Or if you ment a galarian form, please write "galarian pokemon_name"')






def setup(client):
    client.add_cog(Den(client))
