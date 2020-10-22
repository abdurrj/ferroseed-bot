

""" This function is to grab emojis out of text in a message and an example is shown on how to use it
def grab_emojis(message):
    demojized = emoji.demojize(message, use_aliases = True)
    custom_emojis = [''.join('<' + cemoji + '>') for cemoji in re.findall(r'<([^>]*)>', message)]
    only_disc_emojis = ' '.join([word for word in demojized.split() if word not in custom_emojis])
    discord_emoji_sep = re.findall(r":([^:]*):", only_disc_emojis)
    disc_emojis = [emoji.emojize(''.join(':' + dem + ':'), use_aliases=True) for dem in discord_emoji_sep]
    all_emojis = disc_emojis + custom_emojis
    return [emojis for emojis in all_emojis]

An example of how to use the function grab_emojis() from above
@client.command()
async def emojiprint(ctx, *, message):
    # grab_emojis(message)
    # print(message)
    emojis = grab_emojis(message)
    print(emojis)
    for i in emojis:
        print(i)
    msg = await ctx.send(message)
    for i in emojis:
        await discord.Message.add_reaction(msg, i)

""" 

""" Rewrite of poll command to work for flags and numbers,
not implemented because as it is it's good for laughs
@client.command()
async def pollest(ctx, *, text):
    demojized = emoji.demojize(text, use_aliases = True)
    custom_emojis = [''.join('<' + cemoji + '>') for cemoji in re.findall(r'<([^>]*)>', text)]
    only_disc_emojis = ' '.join([word for word in demojized.split() if word not in custom_emojis])
    discord_emoji_sep = re.findall(r":([^:]*):", only_disc_emojis)
    disc_emojis = [emoji.emojize(''.join(':' + dem + ':'), use_aliases=True) for dem in discord_emoji_sep]
    all_emojis = disc_emojis + custom_emojis
    msg = await ctx.send(text)
    for i in all_emojis:
        try:
            await discord.Message.add_reaction(msg, i)
        except:
            print("Emoji " + i + " not found") """


""" @client.command()
async def teams(ctx):
    guild = ctx.message.guild
    tk = guild.get_role(746168865737932831)
    team1 = tk.name
    tkm = tk.members
    tkmembers = [member.name for member in tk.members]
    a = ', '.join(tkmembers)
    an = str(len(tkmembers))

    ts = guild.get_role(746169087347916851)
    team2 = ts.name
    tsm = ts.members
    tsmembers = [member.name for member in ts.members]
    b = ', '.join(tsmembers)
    bn = str(len(tsmembers))

    await ctx.send(team1 + " members: ("+an+")\n" + a + "\n \n And \n \n" + team2 + " members: ("+bn+")\n" + b) """


""" 
@client.command()
async def gibway(ctx, *, message):
    user = ctx.message.author
    command_message = ctx.message
    channel_id = ctx.message.channel.id
    await discord.Message.delete(command_message)
    if channel_id == 738391260662071359:
        gibway_message = await ctx.send("**giveaway from <@"+str(user.id)+"> !!**\n"+message)
        await gibway_message.pin()
        await user.send("Thank you for doing the giveaway."
                        "\n```"+message+"```\n"
                        "When you want to select winner(s), use this command"
                        "\n`command_name x message_id`, where x is the amount of winners you are selecting.\n"
                        "\nThe message id you need to put in is:")
        await user.send(gibway_message.id)
    else:
        await ctx.send("<a:RHype:708568633508364310> Thanks for wanting to do a giveaway, but you need to do it in <#738391260662071359>."
                        "\nYour message was deleted, but I sent it to you so you can copy it to the right channel!")
        await user.send(message) """