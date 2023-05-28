import os
import discord
from dotenv import load_dotenv
import ezcord
import logging

version = "0.0.4"
# Das ist die Version des Bots
load_dotenv()
log_channel = os.getenv("LOG_CHANNEL")
debug_channel = os.getenv("DEBUG_CHANNEL")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

activity = discord.Activity(
    type=discord.ActivityType.custom, name="In Code we Trust")

ezcord.set_log(
    log_level=logging.DEBUG,
    discord_log_level=logging.INFO,
    webhook_url=log_channel

)


bot = ezcord.Bot(
    intents=intents,
    debug_guilds=[723945239223599188],
    activity=activity,
    error_webhook_url=debug_channel
)


if __name__ == "__main__":
    bot.load_cogs(subdirectories=True)


bot.run(os.getenv("TOKEN"))
