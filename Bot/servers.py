import discord
import constants as c
from discord.ext import commands
class Servers:

    def __init__(self, bot):
        self.bot = bot
        self.invites = ["discord.gg/", "discordapp.com/invite/"]
    
    async def on_message(self,message):
        if message.author.id in c.admins:
            pass
        elif message.author.id in c.helpers:
            pass
        elif message.author.id==message.guild.owner:
            pass
        elif message.channel==442368353814970368:
            pass
        else:
            for inv in self.invites:
                if inv in message.content.lower():
                    await message.delete()
                    await message.channel.send("stop promoting your discord server you friendless loser")


def setup(bot):
    bot.add_cog(Servers(bot))


