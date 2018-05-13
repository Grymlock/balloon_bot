import discord
import constants as c
from discord.ext import commands

bot=commands.Bot(description="Best bot on Discord",command_prefix="-")
@bot.event
async def on_ready():

    for cog in c.cogs:

        try:
            bot.load_extension(f'{cog}')
            print(f"Cog {cog} successfully loaded.")
            
        except Exception as e:
            print(f"CRITICAL: Cog {cog} failed to load.")
            print(e)


    print(f'Logged in as\n{bot.user .name}\n{bot.user.id}\nBalloonBot v{c.version} Online')

    botusers = 0    
    for user in bot.users:  
        if user.bot is True:
            continue
        else:
            botusers = botusers + 1

    botguilds = 0
    for guild in bot.guilds:
        botguilds = botguilds + 1

    botchannels = 0
    for guild in bot.guilds:
        for channel in guild.channels:
            botchannels = botchannels + 1

    presence = discord.Game(f"-help | v{c.version}")
    await bot.change_presence(status=discord.Status.online, activity=presence)

    print(f'Users: {botusers}\nGuilds: {botguilds}\nChannels: {botchannels}')
bot.run(str(c.token))
