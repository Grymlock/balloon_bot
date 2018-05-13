import discord
from discord.ext import commands
import constants as c
class Utilities:

    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def add(self,ctx,num1,num2):
        'Adds numbers'
        if num1==str(9) and num2==str(10):
            await ctx.send("Twenty Wun")
        else:
            try:
                sum=int(num1)+int(num2)
                await ctx.send(f"The sum of `{num1}` and `{num2}` is "+ str(sum))
            except Exception as e:
                await ctx.send(f"`{e}`")
    
    @commands.command()
    async def subtract(self,ctx,num1,num2):
        'Subtracts numbers'
        try:
            difference=int(num1)-int(num2)
            await ctx.send(f"The difference between `{num1}` and `{num2}` is "+ str(difference))
        except Exception as e:
            await ctx.send(f"`{e}`")
    
    
    @commands.command()
    async def multiply(self,ctx,num1,num2):
        'Multiply numbers'
        try:
            product=int(num1)*int(num2)
            await ctx.send(f"The product of `{num1}` and `{num2}` is " + str(product))
        except Exception as e:
            await ctx.send(f"`{e}`")
            
    @commands.command()
    async def invite(self,ctx):
        "DM's the bot invite to a user"
        await ctx.send("DM'ed you the invite")
        await ctx.author.send("https://discordapp.com/api/oauth2/authorize?client_id=426560497781833748&permissions=470285559&scope=bot")

    @commands.command(invoke_without_command=True)
    async def server(self,ctx):
        "Show server info"
        serverembed = discord.Embed(color=discord.Color.green()) 
        serverembed.set_thumbnail(url=ctx.guild.icon_url) #puts server icon as thumbnail
        serverembed.add_field(name='Name', value=ctx.guild.name) #server name
        serverembed.add_field(name='Owner', value='<{}>'.format(str(ctx.guild.owner.id))) #server owner
        serverembed.add_field(name='Members', value=ctx.guild.member_count)
        serverembed.add_field(name='Creation (EST)', value='`{}`'.format(str(ctx.guild.created_at)))#server creation time
        serverembed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url_as(format='png'))
        serverembed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url_as(format='png'))
        await ctx.send(embed=serverembed)
    
    @commands.command()
    async def status(self,ctx):
        "Shows bot status"
        botembed=discord.Embed(color=discord.Color.green())
        botembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/442868510776098818/445290952559558657/unknown.png")
        botembed.add_field(name="Version",value="Version {}".format(str(c.version)))
        users=0
        for user in self.bot.users:
            if user.bot is True:
                continue
            else:
                users=users+1
        botembed.add_field(name="Users",value=users)
        guilds=0
        for guild in self.bot.guilds:
            guilds=guilds+1
        botembed.add_field(name="Servers",value=guilds)
        bchannels=0
        for guild in self.bot.guilds:
            for channels in guild.channels:
                bchannels=bchannels+1
        botembed.add_field(name="Channels",value=bchannels)
        await ctx.send(embed=botembed)


        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def massnick(self,ctx,*,nick=None):
        "Massnicks everybody in the server to the specified name.\n Requires Administrator Perms"
        membercount=0
        changednames=0
        failed=0
        for member in ctx.guild.members:
            membercount+=1
        if nick==None:
            await ctx.send("You need to specify a nickname")
        else:
            await ctx.send(f"Changing `{membercount}` users to `{nick}`. This may take a moment")
            for member in ctx.guild.members:
                try:
                    await member.edit(nick=nick)
                    changednames+=1
                except Exception as e:
                    failed+=1
                    print(e)
            await ctx.send(f"`{changednames}` users names changed. Failed to change `{failed}`")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearnick(self,ctx):
        "Resets all nicknames on the server.\n Requires Administrator Perms"
        membercount=0
        changednames=0
        failed=0
        for member in ctx.guild.members:
            membercount+=1
        await ctx.send(f"Reseting `{membercount}` users names. This may take a moment")
        for member in ctx.guild.members:
            try:
                await member.edit(nick="")
                changednames+=1
            except Exception as e:
                failed+=1
                print(e)
        await ctx.send(f"Reset `{changednames}`users names. Failed to reset `{failed}`")

    @commands.command()
    @commands.bot_has_permissions(manage_nicknames=True)
    async def changenick(self,ctx,member:discord.Member,*, nick):
        "Changes a users nickname"
        try:
            await member.edit(nick=str(nick))
            await ctx.send(f"`{member}'s'` nickname changed to `{nick}`")
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(Utilities(bot))
