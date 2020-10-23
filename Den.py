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


    # Links to specific den on serebii website, or tells what den a pokemon is in.
    # Adjust max number for CT when available
    @commands.command()
    async def den(self, ctx, a):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        user = ctx.message.author.name
        poke_in_den = pd.read_excel(r'data/excel/poke_in_den.xlsx')
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





    # @commands.command(name = 'dex', aliases = ['pokedex'])
    # async def dex(self, ctx, *, pkmn):
    #     ability_check = ['ability1', 'ability2', 'abilityH']
    #     egg_group_check = ['eggGroup1', 'eggGroup2']
    #     typing_check = ['type1', 'type2']
    #     with open(r"data/json/pokemon.json", "r") as read_file:
    #         data = json.load(read_file)
    #     pokemon = str((pkmn.lower()).title())
    #     for i in range(0, len(data)):
    #         pkmn_info = data[i]
    #         if pokemon in (pkmn_info.values()):
    #             # print(pkmn_info)
    #             abilities_dict = pkmn_info["abilities"]
    #             ability_list = [abilities_dict[ability] for ability in ability_check if abilities_dict[ability] is not None]
    #             # Construction depending on 2 or 3 abilities
    #             if len(ability_list) == 3:
    #                 ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
    #                 ability_2 = "Ability 2: `" + ability_list[1] + "`\n"
    #                 ability_h = "Ability H: `" + ability_list[2] + "`"
    #                 ability = ability_1 + ability_2 + ability_h
    #             elif len(ability_list) == 2:
    #                 ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
    #                 ability_h = "Ability H: `" + ability_list[1] + "`\n"
    #                 ability = ability_1 + ability_h
    #             else:
    #                 ability = "Ability 1: `" + ability_list[0] + "`\n"
                
    #             typing_list = [pkmn_info[typing] for typing in typing_check if pkmn_info[typing] is not None]
    #             # Adjust for single or dual type
    #             if len(typing_list) == 1:
    #                 typing = "Type: `" + typing_list[0] + "`"
    #             else:
    #                 typing = "Type: `" + typing_list[0] + "/" + typing_list[1] + "`"
                
    #             egg_groups = ', '.join([pkmn_info[group] for group in egg_group_check if pkmn_info[group] is not None])
    #             catch_rate = "Catch rate: `" + str(pkmn_info["catchRate"]) + "`"
    #             base_stats = pkmn_info["baseStats"]
    #             stats = ["hp", "atk", "def", "spA", "spD", "spe", "tot"]
    #             stat_value = [base_stats[stat] for stat in stats]

    #             dens = pkmn_info["dens"]
    #             sword_dens_list = dens["sword"]
    #             sword_dens = ', '.join(sword_dens_list[i] for i in range(0, len(sword_dens_list)) if len(sword_dens_list) is not None)
    #             shield_dens_list = dens["shield"]
    #             shield_dens = ', '.join(shield_dens_list[i] for i in range(0, len(shield_dens_list)) if len(shield_dens_list) is not None)
    #             folder = "normal"

    #             embed = discord.Embed(title="__#" + str(pkmn_info["dexId"]) +  " " + pokemon.title() + "__", colour=0xFF0000)
    #             embed.add_field(name="Misc. Info", value=typing + "\n" + catch_rate + "\nEgg Groups: `" + egg_groups + "`\n")
    #             embed.add_field(name="Abilities", value=ability, inline=True)
    #             embed.add_field(
    #                 name="Base stats: ",
    #                 value="__`HP     Atk     Def`__\n"+""
    #                 "__`"+ f"{str(stat_value[0]):<7}" + f"{str(stat_value[1]):<8}" + f"{str(stat_value[2]):<3}" + "`__\n"
    #                 "__`SpA    SpD     Spe`__\n"
    #                 "__`"+ f"{str(stat_value[3]):<7}" + f"{str(stat_value[4]):<8}" + f"{str(stat_value[5]):<3}" +"`__\n"
    #                 "__`Total: " + str(stat_value[6]) + "`__")
    #             if len(sword_dens_list) != 0 or len(shield_dens_list) != 0:
    #                 embed.add_field(name="Dens", value="Sword: " + str(sword_dens) + "\nShield: " + str(shield_dens) + "", inline=False)
                
    #             pokemon_url_name = pokemon.replace(" ", "-")
    #             embed.set_image(url="https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon_url_name.lower() +".png")
                
    #             await ctx.send(embed=embed)


    # @commands.command(name = 'dexter', aliases = ['pokedexter'])
    # async def dexter(self, ctx, pkmn, *form_input):
    #     ability_check = ['ability1', 'ability2', 'abilityH']
    #     egg_group_check = ['eggGroup1', 'eggGroup2']
    #     forms_check = ['Male', 'male', 'Female', 'female', 'M', 'm', 'F', 'f', 'Alolan', 'alolan', 'Gigantamax', 'Gmax', 'Mega', 'mega', 'MegaX', 'megax', 'MegaY', 'megay']
    #     stat_changing_forms_name_first = ['Male', 'male', 'Female', 'female', 'M', 'm', 'F', 'f']
    #     stat_changing_forms_name_last = ['Alolan', 'Mega', 'MegaX', 'MegaY']
    #     typing_check = ['type1', 'type2']
    #     with open(r"data/json/pokemon.json", "r") as read_file:
    #         data = json.load(read_file)
    #     pokemon = str((pkmn.lower()).title())

    #     possible_names = []
    #     for i in range(0, len(data)):
    #         pkmn_info = data[i]
    #         if pkmn_info['name'].startswith(pokemon):
    #             poke_name = pkmn_info['name']
    #             possible_names.append(poke_name)
    #             poke_dict_forms = pkmn_info["forms"]
    #     if len(possible_names) == 0:
    #         print("No match")
    #     else:
    #         pokemon = possible_names[0]
        
    #     # print(poke_dict_forms)
    #     if len(poke_dict_forms) == 0:
    #         form = ""
    #     else:
    #         # Form check
    #         available_forms = []
    #         if form_input:
    #             form_input = list(form_input)
    #             for i in form_input:
    #                 if i in forms_check:
    #                     available_forms.append(i)

    #             if len(available_forms) == 0:
    #                 form = ""
    #             else:
    #                 form = available_forms[0]
    #                 if form == 'm' or form == 'M':
    #                     form = 'Male'
    #                 elif form == 'f' or form == 'F':
    #                     form = 'Female'
    #                 elif form == 'gmax' or form == 'Gmax':
    #                     form = 'Gigantamax'
    #                 elif form == 'megax':
    #                     form = 'MegaX'
    #                 elif form == 'megay':
    #                     form = 'MegaY'
    #                 elif form == 'mega':
    #                     form = 'Mega'
    #                 elif form == 'alolan':
    #                     form = 'Alolan'
    #         else:
    #             form = ""

    #     if form in stat_changing_forms_name_first or form in stat_changing_forms_name_last:
    #         if form in stat_changing_forms_name_first:
    #             if form == 'Male':
    #                 pokemon_lookup = pokemon
    #             else:
    #                 pokemon_lookup = pokemon + " " + form
    #         elif form in stat_changing_forms_name_last:
    #             pokemon_lookup = form + " " + pokemon
    #     else:
    #         print("no form")
    #         pokemon_lookup = pokemon
        
    #     for i in range(0, len(data)):
    #         pkmn_info = data[i]
    #         if pokemon_lookup in (pkmn_info.values()):
    #             abilities_dict = pkmn_info["abilities"]
    #             ability_list = [abilities_dict[ability] for ability in ability_check if abilities_dict[ability] is not None]
    #             poke_dict_forms = pkmn_info["forms"]
    #             pokemon_name = pkmn_info["name"]
    #             # Construction depending on 1, 2 or 3 abilities
    #             if len(ability_list) == 3:
    #                 ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
    #                 ability_2 = "Ability 2: `" + ability_list[1] + "`\n"
    #                 ability_h = "Ability H: `" + ability_list[2] + "`"
    #                 ability = ability_1 + ability_2 + ability_h
    #             elif len(ability_list) == 2:
    #                 ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
    #                 ability_h = "Ability H: `" + ability_list[1] + "`\n"
    #                 ability = ability_1 + ability_h
    #             else:
    #                 ability = "Ability 1: `" + ability_list[0] + "`\n"
                
    #             typing_list = [pkmn_info[typing] for typing in typing_check if pkmn_info[typing] is not None]
    #             # Adjust for single or dual type
    #             if len(typing_list) == 1:
    #                 typing = "Type: `" + typing_list[0] + "`"
    #             else:
    #                 typing = "Type: `" + typing_list[0] + "/" + typing_list[1] + "`"
                
    #             egg_groups = ', '.join([pkmn_info[group] for group in egg_group_check if pkmn_info[group] is not None])
    #             catch_rate = "Catch rate: `" + str(pkmn_info["catchRate"]) + "`"
    #             base_stats = pkmn_info["baseStats"]
    #             stats = ["hp", "atk", "def", "spA", "spD", "spe", "tot"]
    #             stat_value = [base_stats[stat] for stat in stats]

    #             dens = pkmn_info["dens"]
    #             sword_dens_list = dens["sword"]
    #             sword_dens = ', '.join(sword_dens_list[i] for i in range(0, len(sword_dens_list)) if len(sword_dens_list) is not None)
    #             shield_dens_list = dens["shield"]
    #             shield_dens = ', '.join(shield_dens_list[i] for i in range(0, len(shield_dens_list)) if len(shield_dens_list) is not None)
    #             folder = "normal"
    #             pokemon_forms = []
    #             if len(poke_dict_forms) !=0:
    #                 for i in range(0, len(poke_dict_forms)):
    #                     if poke_dict_forms[i] in forms_check:
    #                         i = poke_dict_forms[i]
    #                         pokemon_forms.append(i)
                    
    #                 pokemon_forms = "Forms: `" + ', '.join(pokemon_forms[i] for i in range(0, len(pokemon_forms))) + "`"
    #             else:
    #                 pokemon_forms = ""

    #             if form != "":
    #                 if form == 'MegaX':
    #                     pokemon_name = "Mega " + pokemon + " X"
    #                 elif form == 'MegaY':
    #                     pokemon_name = "Mega " + pokemon + " Y"
    #                 else:
    #                     pokemon_name = pokemon_name

    #             embed = discord.Embed(title="__#" + str(pkmn_info["dexId"]) +  " " + pokemon_name + "__", colour=0xFF0000)
    #             embed.add_field(name="Misc. Info", value=typing + "\n" + catch_rate + "\nEgg Groups: `" + egg_groups + "`\n" + pokemon_forms)
    #             embed.add_field(name="Abilities", value=ability, inline=True)
    #             embed.add_field(
    #                 name="Base stats: ",
    #                 value="__`HP     Atk     Def`__\n"+""
    #                 "__`"+ f"{str(stat_value[0]):<7}" + f"{str(stat_value[1]):<8}" + f"{str(stat_value[2]):<3}" + "`__\n"
    #                 "__`SpA    SpD     Spe`__\n"
    #                 "__`"+ f"{str(stat_value[3]):<7}" + f"{str(stat_value[4]):<8}" + f"{str(stat_value[5]):<3}" +"`__\n"
    #                 "__`Total: " + str(stat_value[6]) + "`__")
    #             if len(sword_dens_list) != 0 or len(shield_dens_list) != 0:
    #                 embed.add_field(name="Dens", value="Sword: " + str(sword_dens) + "\nShield: " + str(shield_dens) + "", inline=False)
                
    #             pokemon_url_name = pokemon.replace(" ", "-")
    #             embed.set_image(url="https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon_url_name.lower() + form + ".png")
            
    #             await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Den(client))
