import discord
from discord.ext import commands
from discord.commands import slash_command, Option
##############################################
# Hier wird die Klasse Say erstellt
# Der Bot kann mit dieser Klasse Nachrichten in einem bestimmten Channel schreiben
# Die Nachricht wird von dem User geschrieben der den Befehl ausführt
# Der Bot kann nur in den Channel schreiben der in dem Befehl angegeben ist
# Der Befehl ist ein Slash Command
# Der Befehl hat 2 Parameter
# Der erste Parameter ist der Text der geschrieben werden soll
# Der zweite Parameter ist der Channel in dem der Bot schreiben soll
# Der Befehl ist nur für den Server "Bot Test Server" registriert


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Lass den Bot für dich sprechen!")
    async def botsay(self,
                     ctx,
                     text: Option(str, "Wie ist deine Nachricht?"),
                     channel: Option(discord.TextChannel),

                     ):
        await channel.send(text)
        await ctx.respond("Deine Nachricht wurde Gesendet!!!", ephemeral=True)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        pass


def setup(bot):
    bot.add_cog(Say(bot))
