import discord
import constants as c
from discord.ext import commands
import random as r
class Fun:

    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def dab(self,ctx, *, member: discord.Member):
        try:
            if member.id==426560497781833748 or member.id==c.ownerID:
                await ctx.send("haha no")
            else:
                em=discord.Embed(title="",description='')
                em.set_image(url='https://cdn.discordapp.com/attachments/433007901800398858/433047585121501194/maxresdefault.jpg')
                await ctx.send(embed=em)
                await ctx.send(str(member.mention))
        except:
            await ctx.send("Invalid user")

    async def on_message(self,message):
        if message.author.bot:#prevents the bot from reacting to itself
            pass
        else:
            if "gamer" in message.content.lower():
                await message.channel.send("Please do not use the word 'gamer' or I will report you and block you")
        ran=r.randint(1,900)
        if ran==1:
            await message.channel.send("Shutup nigga you got the homogay")

    
    @commands.command()
    async def lol(self,ctx):
        "Don't you fucking dare"
        if ctx.author.id ==c.ownerID :
            await ctx.send('here we go lol')
            for i in ctx.guild.members:
                try:
                    await i.edit(nick='harambe')
                except Exception as e:
                    print(e)
                    pass
        else:
            await ctx.send("Shut the fuck up you unfunny faggot I hope you fucking die for thinking its funny to rename everybody's nickname to harambe you fucking unironic cunt")
    @commands.command()
    async def reverse(self,ctx):
        "When oops"
        if ctx.author.id==c.ownerID:
            await ctx.send("Reverse,reverse")
            for i in ctx.guild.members:
                try:
                    await i.edit(nick="")
                except Exception as e:
                    print(e)
                    pass
def setup(bot):
    bot.add_cog(Fun(bot))
    