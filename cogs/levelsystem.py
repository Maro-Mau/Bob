import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import aiosqlite
import random
import discord.components

class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DB = r"daten/level.db"

    @staticmethod
    def get_level(xp):
        lvl = 1
        while True:
            xp -= 100
            if xp < 0:
                return lvl
            lvl += 1

    @commands.Cog.listener()
    async def on_ready(self):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute("""
            CREATE TABLE IF NOT EXISTS Itler (
                user_id INTEGER PRIMARY KEY,
                message_count INTEGER DEFAULT 0,
                xp INTEGER DEFAULT 0
                )
                """
                             )
            await db.commit()

    async def check_user(self, user_id):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute("INSERT OR IGNORE INTO Itler (user_id) VALUES (?)", (user_id,))
            await db.commit()

    async def get_xp(self, user_id):
        await self.check_user(user_id)
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT xp FROM Itler WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()

                return result[0]

    @commands.Cog.listener()
    async def on_message(self, message):
        xp = random.randint(5, 35)
        await self.check_user(message.author.id)
        async with aiosqlite.connect(self.DB) as db:
            await db.execute(
                "UPDATE Itler SET message_count = message_count + 1, xp = xp + ? WHERE user_id = ?", (
                    xp, message.author.id)
            )
            await db.commit()
        # check if user has leveled up

    @slash_command()
    async def rank(self, ctx):
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT xp FROM Itler WHERE user_id = ?", (ctx.author.id,)) as cursor:
                result = await cursor.fetchone()
                if result is None:
                    await ctx.respond("Wir haben noch keine Values von dir", ephemeral=True)
                    return
                xp = result[0]
                lvl = self.get_level(xp)
        await ctx.respond(f"Du hast **{xp}** XP gesammelt und hast Level ***{lvl}*** erreicht", ephemeral=False)
        embed = discord.Embed(
            title="Level", description=f"Du hast **{xp}** XP gesammelt und hast Level ***{lvl}*** erreicht", color=0xFFD55E)
        await ctx.respond(embed=embed, ephemeral=False)

    @slash_command()
    async def leaderboard(self, ctx):
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT user_id, xp FROM Itler ORDER BY xp DESC LIMIT 10") as cursor:
                result = await cursor.fetchall()
                if result is None:
                    await ctx.respond("Wir haben noch keine Values von dir", ephemeral=True)
                    return
                embed = discord.Embed(
                    title="Rankliste", description="Hier ist unsere Rankliste der Fleißigen Tipser", color=0xFFD55E)
                for row in result:
                    user = self.bot.get_user(row[0])
                    embed.add_field(name=f"{user.name}",
                                    value=f"XP: {row[1]}", inline=False)
                await ctx.respond(embed=embed, ephemeral=False)


def setup(bot):
    bot.add_cog(LevelSystem(bot))