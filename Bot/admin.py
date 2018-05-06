import discord
import os
import sys
from discord.ext import commands
import constants as c
class Admin:

    def __init__(self,bot):
        self.bot=bot

    @commands.group(hidden=True, invoke_without_command=True)
    async def admin(self,ctx,argument=None):
        if ctx.author.id not in c.admins:
            pass
        
    @admin.command(name="shutdown")
    async def admin_shutdown(self, ctx):
        'Shuts the bot down'
        if ctx.author.id in c.admins:
            await ctx.send('Bot shutting down')
            await sys.exit()
    
    @admin.command(name="presence")
    async def admin_presence(self, ctx, *, presence=None):
        '''Sets the bot's "Playing" status.'''
        if ctx.author.id in c.admins:
            if presence is None or "default"==presence:
                presence = discord.Game(f"try .help | version{c.version}")
                await self.bot.change_presence(status=discord.Status.online, activity=presence)
                await ctx.send('Presence reset to default.')    
            else:
                presence = discord.Game(presence)
                await self.bot.change_presence(status=discord.Status.online, activity=presence)
                await ctx.send(f'Presence set to `{presence}`.')
        else:
            pass
    
    @admin.command(name="nick")
    async def admin_nick(self, ctx, *, reqnick=None):
        "Sets the bot's nickname for the server."
        if ctx.author.id in c.admins:
            bb=ctx.guild.get_member(426560497781833748)
            if reqnick is None:
                await bb.edit(nick="Ballon_Bot")
                await ctx.send('Nickname reset to `Balloon_Bot`.')
            else:
                try:
                    await bb.edit(nick=reqnick)
                    await ctx.send(f'Nickname set to `{reqnick}`.')
                except:
                    await ctx.send('Nickname is too long!')
        else:
            pass
    @commands.group(hidden=True,invoke_without_command=True)
    async def helper(self,ctx,argument=None):
        if ctx.author.id not in c.helpers:
            pass
    
    @helper.command(name="nick")
    async def helper_nick(self, ctx, *, reqnick=None):
        "Sets the bot's nickname for the server."
        if ctx.author.id in c.helpers:
            bb=ctx.guild.get_member(426560497781833748)
            if reqnick is None:
                await bb.edit(nick="Ballon_Bot")
                await ctx.send('Nickname reset to `Balloon_Bot`.')
            else:
                try:
                    await bb.edit(nick=reqnick)
                    await ctx.send(f'Nickname set to `{reqnick}`.')
                except:
                    await ctx.send('Nickname is too long!')
        else:
            pass
    
    @helper.command(name="presence")
    async def helper_presence(self, ctx, *, presence=None):
        '''Sets the bot's "Playing" status.'''
        if ctx.author.id in c.helpers:
            if presence is None or "default"==presence:
                presence = discord.Game(f"try .help | version{c.version}")
                await self.bot.change_presence(status=discord.Status.online, activity=presence)
                await ctx.send('Presence reset to default.')    
            else:
                presence = discord.Game(presence)
                await self.bot.change_presence(status=discord.Status.online, activity=presence)
                await ctx.send(f'Presence set to `{presence}`.')
        else:
            pass
def setup(bot):
    bot.add_cog(Admin(bot))