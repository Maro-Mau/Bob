from discord.ext import commands, tasks
from datetime import time, timezone


class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.moin.start()

    @tasks.loop(time=time(7, 0, tzinfo=timezone.utc))
    async def moin(self):
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send("Guten Morgen, ich hoffe, ihr habt heute Spaß in eurem täglichen Wahnsinn.")

    @tasks.loop(time=time(19, 0, tzinfo=timezone.utc))
    async def gutenmorgen(self):
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send("Bello, me want banana.")

    @tasks.loop(time=time(22, 0, tzinfo=timezone.utc))
    async def moin(self):
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send("Bob ist müde, Bob geht Bubu machen Bob wünscht sich eine gute Nacht <3")


def setup(bot):
    bot.add_cog(Task(bot))
