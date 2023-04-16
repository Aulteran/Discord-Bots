import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix = '.')

client.remove_command("help")

TOKEN = 'Njk0OTk3MjIwMDA4Nzg3OTY4.XogT3g.33LZaL9_O9uyjIKbKZzrEUPLO0s'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')
    print('Enforcer is now. Awaiting FEMA Orders\nOnly FEMA Director can Activate Systems V9-15\nPending Director Authorization\n\n')

@client.command()
async def help(ctx):
    print(f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Sending Help Message...')
    await ctx.send("**INFO**\nEnforcer is FEMA's new Moderator Bot. It will be replacing the Auttaja, Dyno, and Probot Bots. NOTE: Enforcer is developed and coded by FEMA. Any attempt to replicate it will result in a report to discord.\n**COMMANDS**\nPlease note: The prefix is`.`\n`help` - shows this help message\n`ping`or`latency` - will show you the round ping time from the bot and back\n`info <@someone's-username>` - will show all the user data of the specified user.\n`kick <@someone's-username> <optional-reason>` - will kick the person specified\n`ban <@someone's-username> <optional-reason>` - will ban the person specified\n`clear <amount>` - will delete a certain amount of messages. If no amount is specified, it will delete 10.")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(aliases=['latency'])
async def ping(ctx):
        await ctx.send(f'Pong! The Latency is {round(client.latency * 1000)}ms')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Sending Latency Details')

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Sending user info')
    if ctx.message.author.guild_permissions.administrator:
        if user is None:
            await ctx.send('Please input a user.')
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]ctx.message.author did not provide user')
        else:
            await ctx.send("The user's name is: {}".format(user.name) + "\nThe user's ID is: {}".format(user.id) + "\nThe user's current status is: {}".format(user.status) + "\nThe user's highest role is: `{}`".format(user.top_role) + "\nThe user joined at: {}".format(user.joined_at))
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Sent user data requested')
    else:
        await ctx.send('You lack permission to perform this action')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]message author did not have permission to perform action')


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.kick_members:
        await ctx.guild.kick(member, reason=reason)
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Kicked @{member.name}#{member.discriminator}')
        await ctx.send(f'Kicked @{member.name}#{member.discriminator} with the reason `{reason}`')
    else:
        await ctx.send('You lack permission to perform this action')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]ctx.message.author lacked permissions to perform action')


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.ban_members:
        await ctx.guild.ban(member, reason=reason)
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Banned @{member.name}#{member.discriminator}')
        await ctx.send(f'Banned @{member.name}#{member.discriminator}')
    else:
        await ctx.send('You lack permission to perform this action')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]ctx.message.author lacked permissions to perform action')
    
#unban command is in development
@client.command()
async def unban(ctx,*, member):
    banned_users = await ctx.guild.bans()
    member.name, member.discriminator = member.split('#')

    for ban.entry in banned_users:
        member.ban_entry.user

        if (member.name, member.discriminator) == (member.name, member.discriminator):
            await ctx.guild.unban(member)
            await ctx.send(f'Unbanned @{member.name}#{member.discriminator}')
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Unbanned member specified')

@client.command(pass_context=True)
async def clear(ctx, amount=10):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Messages deleted')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]Deleted messages')
    else:
        await ctx.send('You lack permission to perform this action')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]ctx.message.author lacked permissions to perform this action')


client.run(TOKEN) #insert token in 'TOKEN'