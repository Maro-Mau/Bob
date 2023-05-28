import discord
from discord.ext import commands
from discord.commands import slash_command, message_command, user_command


class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @user_command(name="Willkommen")
    async def willkommen(self, ctx, member):
     await ctx.respond(f"{ctx.author.mention} heist {member.mention} Herzlich Willkommen und hofft auf eine schöne gemeinsame zeit ")
    @user_command(name="Lachen")
    async def lachen(self, ctx, member):
     await ctx.respond(f"{ctx.author.mention} Lacht Herzlich mit {member.mention} ")

    @user_command(name="Stupse jemand auf die Nase")
    async def stups(self, ctx, member):
     await ctx.respond(f"{ctx.author.mention} hat {member.mention} auf die nase gestupst")

    @user_command(name="Zustimmen")
    async def zustimmen(self, ctx, member):
     await ctx.respond(f"{ctx.author.mention} stimmt {member.mention} voll zu")

    @user_command(name="Nicht Zustimmen")
    async def nicht_zustimmen(self, ctx, member):
     await ctx.respond(f"{ctx.author.mention} stimmt {member.mention} nicht zu")



def setup(bot):
    bot.add_cog(Context(bot))