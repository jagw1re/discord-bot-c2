import discord
import pyautogui
from io import BytesIO

import requests
from discord.ext import commands


class Screenshot(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    # # Events
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Bot is online.')

    # Commands
    @commands.command()
    async def ss(self, ctx):
        response = requests.post(url="http://localhost:8000", data=b'\x00')
        bytes_io = BytesIO(response.content)
        await ctx.send(file=discord.File(fp=bytes_io, filename="screenshot.png"))


async def setup(client):
    await client.add_cog(Screenshot(client))
