
import discord
from discord.ext import commands
import os
import requests
from pprint import pprint
import random
from discord.commands import slash_command, Option
##############################################


class Tenor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Schicke ein Random FF14 Gif")
    async def finalgif(self, ctx):
        key = os.getenv("TENOR_API")

        params = {
            "q": "FF14",
            "key": key,
            "limit": 100,
            "media_filter": "gif",
            "client_key": "Bob"
        }

        result = requests.get(
            f"https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        pprint(data)
        number = random.randint(0, 10)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title="FF14",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="via Tenor")
        await ctx.respond(embed=embed)
##############################################

    @slash_command(description="Schicke ein Random Panda Gif")
    async def panda(self, ctx):
        key = os.getenv("TENOR_API")

        params = {
            "q": "Panda",
            "key": key,
            "limit": 100,
            "media_filter": "gif",
            "client_key": "Bob"
        }

        result = requests.get(
            f"https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        pprint(data)
        number = random.randint(0, 10)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title="Panda",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="via Tenor")
        await ctx.respond(embed=embed)
##############################################

    @slash_command(description="Schicke ein Random Katzen Gif")
    async def katze(self, ctx):
        key = os.getenv("TENOR_API")

        params = {
            "q": "Katze",
            "key": key,
            "limit": 100,
            "media_filter": "gif",
            "client_key": "Bob"
        }

        result = requests.get(
            f"https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        pprint(data)
        number = random.randint(0, 10)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title="Katze",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="via Tenor")
        await ctx.respond(embed=embed)
##############################################

    @slash_command(description="Schicke ein Random CoD Gif")
    async def cod(self, ctx):
        key = os.getenv("TENOR_API")

        params = {
            "q": "codmw2",
            "key": key,
            "limit": 100,
            "media_filter": "gif",
            "client_key": "Bob"
        }

        result = requests.get(
            f"https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        pprint(data)
        number = random.randint(0, 10)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title="Call of Duty",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="via Tenor")
        await ctx.respond(embed=embed)
##############################################

    @slash_command(description="Schicke ein Random Enten Gif")
    async def ente(self, ctx):
        key = os.getenv("TENOR_API")

        params = {
            "q": "Ente",
            "key": key,
            "limit": 100,
            "media_filter": "gif",
            "client_key": "Bob"
        }

        result = requests.get(
            f"https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        pprint(data)
        number = random.randint(0, 10)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title="Ente NAGH NAGH NAGH",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="via Tenor/Enten sind cool")
        await ctx.respond(embed=embed)
##############################################
    @slash_command(description="Schicke ein Random Enten Gif")
    async def glückbärchen(self, ctx):
        key = os.getenv("TENOR_API")

        params = {
            "q": "Glückbärchen",
            "key": key,
            "limit": 100,
            "media_filter": "gif",
            "client_key": "Bob"
        }

        result = requests.get(
            f"https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        pprint(data)
        number = random.randint(0, 10)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title="Bärchen",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="via Tenor")
        await ctx.respond(embed=embed)        


def setup(bot):
    bot.add_cog(Tenor(bot))

# Path: bot-0.0.2\Discord-Bot0.02\cogs\Gif.py
# Hier werden die Gifs von Tenor geholt und gesendet
# Die Gifs werden über die Tenor API geholt
# Die funktionen sind alle gleich aufgebaut
# Es wird ein Parameter mitgegeben
# Der Parameter wird in die URL eingefügt
# Die URL wird dann an Tenor geschickt
# Tenor schickt dann ein JSON zurück
# Das JSON wird dann in ein Dictionary umgewandelt
# Dann wird ein Random Gif ausgewählt
# Das Gif wird dann in ein Embed gesetzt
# Das Embed wird dann gesendet
# Das ganze wird über eine Slash Command ausgeführt
# Die Slash Commands sind in der main.py registriert
