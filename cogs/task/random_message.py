from discord.ext import commands, tasks
from datetime import time, timezone
import random

msg1 = "Bob ist müde, Bob geht Bubu machen Bob wünscht euch eine gute Nacht <3"
msg2 = "Mir ist Langweilig, ich will spielen"
msg3 = "Ich bin müde, ich will schlafen"
msg4 = "was ist das für 1 life"
msg5 = "was macht ihr so?"
msg6 = "ich bin ein bot, ich kann nicht schlafen"



class Random_msg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.randommsg.start()
    


    @tasks.loop(time=time(7, 45, tzinfo=timezone.utc))
    async def randommsg(self):
        messages = random.random(msg1, msg2, msg3, msg4, msg5, msg6)
        channel = await self.bot.fetch_channel(1066624282731479040)
        await channel.send([messages])


def setup(bot):
    bot.add_cog(Random_msg(bot))
