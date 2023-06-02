from discord.ext import commands, tasks
from datetime import time, timezone


class Taskbanana(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.moin.start()


    @tasks.loop(time=time(19, 0, tzinfo=timezone.utc))
    async def gutenmorgen(self):
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send("Bello, me want banana.")



def setup(bot):
    bot.add_cog(Taskbanana(bot))
