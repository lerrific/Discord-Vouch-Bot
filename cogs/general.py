import os

import importlib

import discord
from discord.ext import commands

import utils


class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(utils.owner)
    async def reload(self, ctx):
        utils.server_init(self, ctx)
        utils.author_init(self, ctx)

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.reload_extension(f'cogs.{filename[:-3]}')
        importlib.reload(utils)
        await utils.embed(ctx, 'Reloaded all cogs successfully.', None)

    @commands.command(aliases=['commands'])
    async def help(self, ctx):
        utils.server_init(self, ctx)
        utils.author_init(self, ctx)

        embed = discord.Embed(title="Commands / Help", description=f"**Start your commands with `{utils.prefix}`**", color=utils.embed_color)
        embed.add_field(name=f"{utils.prefix}vouch", value=f"Vouch for a user. Usage: `{utils.prefix}vouch @user Message here`", inline=False)
        embed.add_field(name=f"{utils.prefix}vouches", value=f"Display all vouches a user has. Usage: `{utils.prefix}vouches @user`", inline=False)
        embed.add_field(name=f"{utils.prefix}leaderboard", value=f"Display the leaderboard for users with the most vouches.", inline=False)
        embed.add_field(name=f"{utils.prefix}delvouch", value=f"**(ADMIN)** Delete a users vouch from another user. Usage: `{utils.prefix}delvouch @user1 @user2`", inline=False)
        embed.add_field(name=f"{utils.prefix}delallvouches", value=f"**(ADMIN)** Delete ALL of a users vouches. Usage: `{utils.prefix}delallvouches @user`", inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        utils.server_init(self, ctx)
        utils.author_init(self, ctx)

        # Update username
        if ctx.author.id != self.bot.user.id and str(ctx.author) != self.bot.data[str(ctx.guild.id)][str(ctx.author.id)]["Username"]:
            self.bot.data[str(ctx.guild.id)][str(ctx.author.id)]["Username"] = str(ctx.author)
            utils.write(self)


def setup(bot):
    bot.add_cog(General(bot))
