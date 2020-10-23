**Ferroseed bot**
First, a special thank you to my friends on the server Ferroseed bot was made for.
I entered this project with no knowledge of programming. They've helped me with problems I have
encountered and motivated me to learn more so I can make a better bot for them.

It's main feature is the seed checking feature, which I have had nothing to do with. See credits.

Additional features have been added, such as reaction roles, polls
and a giveaway that picks user(s) from reactions on your giveaway message

A couple of pokemon related commands, like dex and sprite lookup, ability to create raid channels, friendcode lookup
and getting links to different raid dens.

Some extra commands for fun.

There are a lot of things commented out in the code. Either thing I'm working on, or just comments left for myself.
Just ignore all that.

**Prerequisites:**
Please use by installing python3. 

You must have the latest discord python api installed

Use pip commands to install the following:

python -m pip install -U discord.py

Install all modules used by the bot:
- pandas
- xlrd
- numpy
- emoji
- json

If you want to use seed finder, please follow instructions [here](https://gitlab.com/fishguy6564/lanturn-bot-public-source-code)


**How to Run**
Ferroseed is designed as a single server bot, and the file needs to be tailored to the server..
If you just want the discord bot:
You only need `bot.py` file. Remove extensions extensions within the program and download only `bot.py` file and `data` folder.

If you are interested in running the sys-bot and seed checking, Please follow the repository [here](https://gitlab.com/fishguy6564/lanturn-bot-public-source-code)


**Current Features:**
List will be updated


**Questions?**
For questions regarding the sys-bot and seed checking, Please follow the repository [here](https://gitlab.com/fishguy6564/lanturn-bot-public-source-code)

For questions directed to Ferroseed bot and it's features, find me on discord: Abdur#0846


**Known Bugs**
- The current `poll` command does not work with flags and numbers. 
  Using flags in poll results in the bot reacting with letters instead of flags.
  The working code is added, but commented out as requested by server members, because it's funny


**Planned Features:**



**Credit:**

Base of the bot is designed by fishguy6564, you can read more about it [here](https://gitlab.com/fishguy6564/lanturn-bot-public-source-code)
Used algorithms and documentation from various Pokemon hackers
such as Admiral-Fish and zaksabeast

olliz0r for the sys-botbase sysmodule

Files in the data folder are from [Alcremie-B](https://github.com/RaphGG/den-bot)
