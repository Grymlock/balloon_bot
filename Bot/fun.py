import discord
import constants as c
from discord.ext import commands
import random as r
urls=['https://cdn.discordapp.com/attachments/433007901800398858/433047585121501194/maxresdefault.jpg','https://cdn.discordapp.com/attachments/442868510776098818/442879211296915466/9bt3n9w40bp01.jpg','https://cdn.discordapp.com/attachments/442323518860951589/443142715761360915/Dap.PNG',"https://cdn.discordapp.com/attachments/442323518860951589/443250907501821964/IMG_20180222_192827.jpg"]
badWords=["gamer","frick","fudge","heck","bubby"]
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
                rand=r.randint(0,3)
                em.set_image(url=str(urls[rand]))
                await ctx.send(embed=em)
                await ctx.send(str(member.mention))
        except:
            await ctx.send("Invalid user")

    async def on_message(self,message):
        if message.author.bot:#prevents the bot from reacting to itself
            pass
        else:
            for word in badWords:
                if message.content==(word):
                    await message.channel.send(f"Please do not use the word '{word}' or I will report you and block you")
            ran=r.randint(1,2000)
            if ran==1:
                await message.channel.send("^Are you listening to this retard lmao")
            if message.content==("gm") or message.content==("good morning"):
                await message.channel.send("Another day closer to death" + str(message.author.mention))
            if message.content==("gn") or message.content==("good night"):
                await message.channel.send("sleep tight boyo")
            if message.content==("good bye"):
                await message.channel.send("bye loser")
            if message.content==("what do we want"):
                await message.channel.send("Equality for women")
            if message.content==("when do we want it"):
                await message.channel.send("Now")

    
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
            await ctx.send("Reverse, reverse")
            for i in ctx.guild.members:
                try:
                    await i.edit(nick="")
                except Exception as e:
                    print(e)
                    pass
def setup(bot):
    bot.add_cog(Fun(bot))
    