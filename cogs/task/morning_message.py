from discord.ext import commands, tasks
from datetime import time, timezone


class Taskmorning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.taskmorning.start()

    @tasks.loop(time=time(7, 0, tzinfo=timezone.utc))
    async def moin(self):
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send("Guten Morgen, ich hoffe, ihr habt heute Spaß in eurem täglichen Wahnsinn.")




def setup(bot):
    bot.add_cog(Taskmorning(bot))
