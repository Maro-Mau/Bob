import discord
from discord.ext import commands
from discord.commands import slash_command, Option
##############################################
# Hier wird die Klasse Admin erstellt
# Diese Klasse ist nur für Admins
# Der Bot kann mit dieser Klasse Member kicken
# Der Befehl ist ein Slash Command


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Kicke einen Member")
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def kick(self, ctx, member: Option(discord.Member, "Wähle einen User")):
        try:
            await member.kick()
        except discord.Forbidden:
            await ctx.respond("Ich habe keine Rechte dafür!")
            return
        await ctx.respond(f"{member.mention} wurde gekickt")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        await ctx.respond(f"Es ist ein fehler aufgetreten ```{error}```")
        raise error


def setup(bot):
    bot.add_cog(Admin(bot))
