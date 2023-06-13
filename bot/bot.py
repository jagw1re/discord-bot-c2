import asyncio
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')


async def load_extensions():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        discord.utils.setup_logging()
        await load_extensions()
        await client.start(os.getenv('TOKEN'))


asyncio.run(main())
