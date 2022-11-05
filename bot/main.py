from tokenize import Token
from discord.ext import commands
import os
import json
import discord
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='&', intents=intents)

async def load_extensions():
	for filename in os.listdir("bot/cogs"):
		if filename.endswith(".py"):
			await client.load_extension(f"cogs.{filename[:-3]}")
			
async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)

asyncio.run(main())