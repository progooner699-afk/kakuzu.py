import os
import discord

from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Kakuzu is online as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as error:
        print(f"Command sync failed: {error}")


@bot.tree.command(
    name="ping",
    description="Check Kakuzu's response time"
)
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! Kakuzu's latency is {latency}ms."
    )


if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing from your .env file")

bot.run(TOKEN)