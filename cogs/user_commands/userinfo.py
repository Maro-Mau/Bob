import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option



class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Sag uns wer du bist.")
    async def info(
            self,
            ctx,
        alter: Option(int, "Das Alter", min_value=1, max_value=99),
        user: Option(discord.Member, "Gib einen User an", default=None),

    ):
        if user is None:
            user = ctx.author

        embed = discord.Embed(
            title=f"Infos über {user.name}",
            description=f"Hier siehst du alle Details über {user.mention}",
            color=0xFFD55E
        )
        time = discord.utils.format_dt(user.created_at, "d")
        embed.add_field(name="Account erstellt", value=time, inline=False)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Alter", value=alter)
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text="Irre Durch und Durch")
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
