import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix = '.')

client.remove_command("help")

TOKEN = 'Njk0MzM0MTQzNjI2MDg0NDM0.Xoj-eA.f_ms35a0o1OHLThTpoRSglVhDwU'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Awaiting FEMA Orders'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')
    print('Overwhelm is now online. Awaiting FEMA Orders\nOnly FEMA Director can Activate Systems V9-15\nPending Director Authorization\n')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



client.run(TOKEN)