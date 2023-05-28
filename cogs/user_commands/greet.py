import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option


class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def greet(self, ctx):
        await ctx.respond(f"Hey {ctx.author.mention}")

    @commands.Cog.listener()
    async def on_member_join(
            self,
            member
    ):
        embed = discord.Embed(
            title="Willkommen!",
            description=f"Hallo und Herzlich Willkommen in der Irrenanstalt  {member.mention} bist du Privat oder Kassenpatient?",
            color=0xFFD55E
        )
        channel = await self.bot.fetch_channel(1109096992631697458)
        await channel.send(embed=embed)

    @slash_command(description="Grüsße einen User")
    async def hallo(self, ctx, user: Option(discord.Member, "Der User den du Grüßen möchtest")):
        await ctx.respond(f"Hallo und Willkommen {user.mention}")


def setup(bot):
    bot.add_cog(Greet(bot))
