import json

import discord

prefix = '*'
footer_text = f'type {prefix}help to see my commands'
embed_color = 0x3cd3f6
error_embed_color = 0xff0000


def write(self):
    with open('data.json', 'w') as file:
        file.write(json.dumps(self.bot.data, indent=4, sort_keys=True))


async def embed(ctx, title: str, description: str):
    _embed = discord.Embed(title=title, description=description, color=embed_color)
    _embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    _embed.set_footer(text=footer_text)
    return await ctx.send(embed=_embed)


async def error_embed(ctx, title: str, description: str):
    _embed = discord.Embed(title=":x: " + title, description=description, color=error_embed_color)
    _embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    _embed.set_footer(text=footer_text)
    return await ctx.send(embed=_embed)


def server_init(self, ctx):
    if not str(ctx.guild.id) in self.bot.data:
        self.bot.data[str(ctx.guild.id)] = {}
        write(self)
        return False

    return True


def author_init(self, ctx):
    if not server_init(self, ctx):
        return False

    if ctx.author.id != self.bot.user.id and not str(ctx.author.id) in self.bot.data[str(ctx.guild.id)]:
        #print(f'User {ctx.author} in {ctx.guild.name} has no vouch data, creating fresh vouch data for them.')
        self.bot.data[str(ctx.guild.id)][str(ctx.author.id)] = {"Username": str(ctx.author), "Vouches": {}}
        write(self)
        return False

    return True


def owner(ctx):
    return ctx.author.id == 133420217152831488
