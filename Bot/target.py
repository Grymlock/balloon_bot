import discord
import constants as c
import variables as v
import random as r
from discord.ext import commands

class Target:

    def __init__(self,bot):
        self.bot=bot
    
    @commands.group(hidden=True, invoke_without_command=True)
    async def targeter(self,ctx,argument=None):
        if ctx.author.id not in c.admins:
            pass
    
    @targeter.command(name="target")
    async def targeter_target(self,ctx,*,member:discord.Member):
        if ctx.author.id in c.admins:
            v.target=member.id
            await ctx.send("Target Changed")
        else:
            await ctx.send("No lol")
    
    async def on_message(self,message):
        if message.author.id==v.target:
            num=r.randint(1,1500)
            if num>=150:
                await message.author.send(str(message.content))
            if num==100:
                try:
                    await message.author.kick()
                except:
                    print("Do not have permissions to kick")
        else:
            pass
    @commands.command(hidden=True)
    async def massping(self,ctx,member:discord.Member,*,phrase):
        if ctx.author.id==c.ownerID:
            for i in range(1,100):
                await ctx.send(member.mention +str(phrase))
    
def setup(bot):
    bot.add_cog(Target(bot))                

