from bot import *


class Dexter(commands.Cog):
    def __init__(self, client):

        self.userChannel = None
        self.user = None
        self.id = None
        self.person = None
        self.idInt = None

    @commands.command()
    async def sprite(self, ctx, pkmn, *shiny):
        with open(r"data/json/pokemon.json", "r") as read_file:
            data = json.load(read_file)
        pokemon = str((pkmn.lower()).title())
        possible_names = []
        for i in range(0, len(data)):
            pkmn_info = data[i]
            if pkmn_info['name'].startswith(pokemon):
                poke_name = pkmn_info['name']
                possible_names.append(poke_name)
        if len(possible_names) == 0:
            print("No match")
        else:
            pokemon = possible_names[0]
            
        for i in range(0, len(data)):
            pokemon_dict = data[i]
            if pokemon in (pokemon_dict.values()):
                if shiny:
                    if shiny[0] == "*" or shiny[0].lower() == "shiny":
                        folder = "shiny"
                    else:
                        folder = "normal"
                else:
                    folder = "normal"
                pokemon_url_name = pokemon.replace(" ", "-")
                await ctx.send("https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon_url_name.lower() +".png")


    @commands.command()
    async def ball(self, ctx, pkmn, *shiny):
        with open(r"data/json/pokemon.json", "r") as read_file:
            data = json.load(read_file)
            pokemon = str((pkmn.lower()).title())

        possible_names = []
        for i in range(0, len(data)):
            pkmn_info = data[i]
            if pkmn_info['name'].startswith(pokemon):
                poke_name = pkmn_info['name']
                possible_names.append(poke_name)
        if len(possible_names) == 0:
            print("No match")
        else:
            pokemon = possible_names[0]
    
        for i in range(0, len(data)):
            pokemon_dict = data[i]
            if pokemon in (pokemon_dict.values()):
                if shiny:
                    if shiny[0] == "*" or shiny[0].lower() == "shiny":
                        folder = "shiny"
                    else:
                        folder = "normal"
                else:
                    folder = "normal"
                pokemon_url_name = pokemon.replace(" ", "-")
                await ctx.send("https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon_url_name.lower() +".png")
                await ctx.send("<:bPoke:773668267331551294><:xSport:733003042773008494><:bRepeat:773668267227086909><:xFast:733002797343047690>")
                await ctx.send("<:bGreat:773668267327094804><:bDive:773668267310317578><:xLure:733003042621751347><:xMoon:733003042705768518>")
                await ctx.send("<:bNet:773668267322900590><:xNightmare:733002933473378435><:bQuick:773668267029692487><:xHeavy:733002891341594674>")
                await ctx.send("<:bNest:773668267310972980><:xFriend:733002850933800991><:xSafari:733003042579808297>")
                await ctx.send("<:bHeal:773668266979491902><:xLove:733003042668150865><:xDream:733002735749824695><:bMaster:773668267268898827>")
                await ctx.send("<:bPremier:773668267234820107><:bTimer:773668267452923935>")
                await ctx.send("<:bUltra:773668267306123284><:bLuxury:773668267323555850><:xLevel:733003042244263938>")


    @commands.command(name = 'dex', aliases = ['pokedex'])
    async def dex(self, ctx, pkmn, *form_input):
        ability_check = ['ability1', 'ability2', 'abilityH']
        egg_group_check = ['eggGroup1', 'eggGroup2']
        forms_check = ['Male', 'male', 'Female', 'female', 'M', 'm', 'F', 'f', 'Alolan', 'alolan', 'Gigantamax', 'Gmax', 'Mega', 'mega', 'MegaX', 'megax', 'MegaY', 'megay', 'Ice Rider', 'Ice', 'ice','Shadow Rider','Shadow','shadow']
        stat_changing_forms_name_first = ['Male', 'male', 'Female', 'female', 'M', 'm', 'F', 'f',]
        stat_changing_forms_name_last = ['Alolan', 'Mega', 'MegaX', 'MegaY', 'Ice Rider', 'Shadow Rider','ice','Ice','shadow','Shadow']
        typing_check = ['type1', 'type2']
        with open(r"data/json/pokemon.json", "r") as read_file:
            data = json.load(read_file)
        pokemon = str((pkmn.lower()).title())

        possible_names = []
        poke_dict_forms = []
        for i in range(0, len(data)):
            pkmn_info = data[i]
            if pkmn_info['name'].startswith(pokemon):
                poke_name = pkmn_info['name']
                possible_names.append(poke_name)
                poke_dict_forms = pkmn_info["forms"]
                # print(poke_dict_forms)
        if len(possible_names) == 0:
            print("No match")
        else:
            pokemon = possible_names[0]
        
        
        # print(poke_dict_forms)
        if len(poke_dict_forms) == 0:
            form = ""
        else:
            # Form check
            available_forms = []
            if form_input:
                form_input = list(form_input)
                for i in form_input:
                    if i in forms_check:
                        available_forms.append(i)

                if len(available_forms) == 0:
                    form = ""
                else:
                    form = available_forms[0]
                    if form == 'm' or form == 'M' or form == 'male':
                        form = 'Male'
                    elif form == 'f' or form == 'F' or form == 'female':
                        form = 'Female'
                    elif form == 'gmax' or form == 'Gmax':
                        form = 'Gigantamax'
                    elif form == 'megax':
                        form = 'MegaX'
                    elif form == 'megay':
                        form = 'MegaY'
                    elif form == 'mega':
                        form = 'Mega'
                    elif form == 'alolan':
                        form = 'Alolan'
                    elif form == 'ice' or form == 'Ice':
                        form = 'Ice Rider'
                    elif form == 'shadow' or form == 'Shadow':
                        form = 'Shadow Rider'
            else:
                form = ""

        if form in stat_changing_forms_name_first or form in stat_changing_forms_name_last:
            if form in stat_changing_forms_name_first:
                if form == 'Male':
                    pokemon_lookup = pokemon
                else:
                    pokemon_lookup = pokemon + " " + form
            elif form in stat_changing_forms_name_last:
                pokemon_lookup = form + " " + pokemon
        else:
            print("no form")
            pokemon_lookup = pokemon
        
        # print(pokemon_lookup)

        for i in range(0, len(data)):
            pkmn_info = data[i]
            if pokemon_lookup in (pkmn_info.values()):
                abilities_dict = pkmn_info["abilities"]
                ability_list = [abilities_dict[ability] for ability in ability_check if abilities_dict[ability] is not None]
                poke_dict_forms = pkmn_info["forms"]
                pokemon_name = pkmn_info["name"]
                # Construction depending on 1, 2 or 3 abilities
                if len(ability_list) == 3:
                    ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
                    ability_2 = "Ability 2: `" + ability_list[1] + "`\n"
                    ability_h = "Ability H: `" + ability_list[2] + "`"
                    ability = ability_1 + ability_2 + ability_h
                elif len(ability_list) == 2:
                    ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
                    ability_h = "Ability H: `" + ability_list[1] + "`\n"
                    ability = ability_1 + ability_h
                else:
                    ability = "Ability 1: `" + ability_list[0] + "`\n"
                
                typing_list = [pkmn_info[typing] for typing in typing_check if pkmn_info[typing] is not None]
                # Adjust for single or dual type
                if len(typing_list) == 1:
                    typing = "Type: `" + typing_list[0] + "`"
                else:
                    typing = "Type: `" + typing_list[0] + "/" + typing_list[1] + "`"
                
                egg_groups = ', '.join([pkmn_info[group] for group in egg_group_check if pkmn_info[group] is not None])
                catch_rate = "Catch rate: `" + str(pkmn_info["catchRate"]) + "`"
                base_stats = pkmn_info["baseStats"]
                stats = ["hp", "atk", "def", "spA", "spD", "spe", "tot"]
                stat_value = [base_stats[stat] for stat in stats]

                dens = pkmn_info["dens"]
                sword_dens_list = dens["sword"]
                sword_dens = ', '.join(sword_dens_list[i] for i in range(0, len(sword_dens_list)) if len(sword_dens_list) is not None)
                shield_dens_list = dens["shield"]
                shield_dens = ', '.join(shield_dens_list[i] for i in range(0, len(shield_dens_list)) if len(shield_dens_list) is not None)
                pokemon_forms = []
                if len(poke_dict_forms) !=0:
                    for i in range(0, len(poke_dict_forms)):
                        if poke_dict_forms[i] in forms_check:
                            i = poke_dict_forms[i]
                            pokemon_forms.append(i)
                    if pokemon_forms == ['Male', 'Female', 'm', 'f']:
                        pokemon_forms.remove('m')
                        pokemon_forms.remove('f')

                    pokemon_forms = "Forms: `" + ', '.join(pokemon_forms[i] for i in range(0, len(pokemon_forms))) + "`"
                else:
                    pokemon_forms = ""

                if form != "":
                    if form == 'MegaX':
                        pokemon_name = "Mega " + pokemon + " X"
                    elif form == 'MegaY':
                        pokemon_name = "Mega " + pokemon + " Y"
                    else:
                        pokemon_name = pokemon_name

                if 'shiny' in form_input or '*' in form_input:
                    folder = "shiny"
                else:
                    folder = "normal"


                pokemon_url_name = pokemon.replace(" ", "-")
                # print(pokemon_url_name)

                embed = discord.Embed(title="__#" + str(pkmn_info["dexId"]) +  " " + pokemon_name + "__", colour=0xFF0000)
                embed.add_field(name="Misc. Info", value=typing + "\n" + catch_rate + "\nEgg Groups: `" + egg_groups + "`\n" + pokemon_forms)
                embed.add_field(name="Abilities", value=ability, inline=True)
                embed.add_field(
                    name="Base stats: ",
                    value="__`HP     Atk     Def`__\n"+""
                    "__`"+ f"{str(stat_value[0]):<7}" + f"{str(stat_value[1]):<8}" + f"{str(stat_value[2]):<3}" + "`__\n"
                    "__`SpA    SpD     Spe`__\n"
                    "__`"+ f"{str(stat_value[3]):<7}" + f"{str(stat_value[4]):<8}" + f"{str(stat_value[5]):<3}" +"`__\n"
                    "__`Total: " + str(stat_value[6]) + "`__")
                if len(sword_dens_list) != 0 or len(shield_dens_list) != 0:
                    embed.add_field(name="Dens", value="Sword: " + str(sword_dens) + "\nShield: " + str(shield_dens) + "", inline=False)
                
                if pokemon_lookup == 'Ice Rider Calyrex':
                    url = 'https://www.serebii.net/swordshield/pokemon/898-i.png'
                    embed.set_image(url=url)
                elif pokemon_lookup == 'Shadow Rider Calyrex':
                    url = 'https://www.serebii.net/swordshield/pokemon/898-s.png'
                    embed.set_image(url=url)
                else:
                    embed.set_image(url="https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon_url_name.lower() + form + ".png")
            
                await ctx.send(embed=embed)


""" Old dex command    
    @commands.command(name = 'dex', aliases = ['pokedex'])
    async def dex(self, ctx, *, pkmn):
        ability_check = ['ability1', 'ability2', 'abilityH']
        egg_group_check = ['eggGroup1', 'eggGroup2']
        typing_check = ['type1', 'type2']
        with open(r"data/json/pokemon.json", "r") as read_file:
            data = json.load(read_file)
        pokemon = str((pkmn.lower()).title())
        for i in range(0, len(data)):
            pkmn_info = data[i]
            if pokemon in (pkmn_info.values()):
                # print(pkmn_info)
                abilities_dict = pkmn_info["abilities"]
                ability_list = [abilities_dict[ability] for ability in ability_check if abilities_dict[ability] is not None]
                # Construction depending on 2 or 3 abilities
                if len(ability_list) == 3:
                    ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
                    ability_2 = "Ability 2: `" + ability_list[1] + "`\n"
                    ability_h = "Ability H: `" + ability_list[2] + "`"
                    ability = ability_1 + ability_2 + ability_h
                elif len(ability_list) == 2:
                    ability_1 = "Ability 1: `" + ability_list[0] + "`\n"
                    ability_h = "Ability H: `" + ability_list[1] + "`\n"
                    ability = ability_1 + ability_h
                else:
                    ability = "Ability 1: `" + ability_list[0] + "`\n"
                
                typing_list = [pkmn_info[typing] for typing in typing_check if pkmn_info[typing] is not None]
                # Adjust for single or dual type
                if len(typing_list) == 1:
                    typing = "Type: `" + typing_list[0] + "`"
                else:
                    typing = "Type: `" + typing_list[0] + "/" + typing_list[1] + "`"
                
                egg_groups = ', '.join([pkmn_info[group] for group in egg_group_check if pkmn_info[group] is not None])
                catch_rate = "Catch rate: `" + str(pkmn_info["catchRate"]) + "`"
                base_stats = pkmn_info["baseStats"]
                stats = ["hp", "atk", "def", "spA", "spD", "spe", "tot"]
                stat_value = [base_stats[stat] for stat in stats]

                dens = pkmn_info["dens"]
                sword_dens_list = dens["sword"]
                sword_dens = ', '.join(sword_dens_list[i] for i in range(0, len(sword_dens_list)) if len(sword_dens_list) is not None)
                shield_dens_list = dens["shield"]
                shield_dens = ', '.join(shield_dens_list[i] for i in range(0, len(shield_dens_list)) if len(shield_dens_list) is not None)
                folder = "normal"

                embed = discord.Embed(title="__#" + str(pkmn_info["dexId"]) +  " " + pokemon.title() + "__", colour=0xFF0000)
                embed.add_field(name="Misc. Info", value=typing + "\n" + catch_rate + "\nEgg Groups: `" + egg_groups + "`\n")
                embed.add_field(name="Abilities", value=ability, inline=True)
                embed.add_field(
                    name="Base stats: ",
                    value="__`HP     Atk     Def`__\n"+""
                    "__`"+ f"{str(stat_value[0]):<7}" + f"{str(stat_value[1]):<8}" + f"{str(stat_value[2]):<3}" + "`__\n"
                    "__`SpA    SpD     Spe`__\n"
                    "__`"+ f"{str(stat_value[3]):<7}" + f"{str(stat_value[4]):<8}" + f"{str(stat_value[5]):<3}" +"`__\n"
                    "__`Total: " + str(stat_value[6]) + "`__")
                if len(sword_dens_list) != 0 or len(shield_dens_list) != 0:
                    embed.add_field(name="Dens", value="Sword: " + str(sword_dens) + "\nShield: " + str(shield_dens) + "", inline=False)
                
                pokemon_url_name = pokemon.replace(" ", "-")
                embed.set_image(url="https://img.pokemondb.net/sprites/home/" + folder +"/"+ pokemon_url_name.lower() +".png")
                
                await ctx.send(embed=embed) """

def setup(client):
    client.add_cog(Dexter(client))
