from discord.ext import commands, tasks
from datetime import time, timezone


class Tasknight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.moin.start()


    @tasks.loop(time=time(22, 0, tzinfo=timezone.utc))
    async def night(self):
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send("Bob ist müde, Bob geht Bubu machen Bob wünscht euch eine gute Nacht <3")


def setup(bot):
    bot.add_cog(Tasknight(bot))
