import discord
from io import BytesIO

import requests
from discord.ext import commands


class Enumeration(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    # # Events
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Bot is online.')

    # Commands
    @commands.command()
    async def systeminfo(self, ctx):
        response = requests.post(url="http://localhost:8000", data=b'\x01')
        bytes_io = BytesIO(response.content)
        await ctx.send(file=discord.File(fp=bytes_io, filename="systeminfo.txt"))


async def setup(client):
    await client.add_cog(Enumeration(client))
