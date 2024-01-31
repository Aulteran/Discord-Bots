import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.all()
intents.message_content = True
intents.guilds = True
intents.members = True

print(intents)

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot event: on bot ready
@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def example_command(ctx):
    # Access information from the command context
    author = ctx.author
    channel = ctx.channel
    guild = ctx.guild

    # Use the context to send a message
    await ctx.send(f"Command executed by {author} in channel {channel} of guild {guild}.")

# Command: remove users from a role
@bot.command()
async def remove_members(ctx, role: discord.Role):
    print("Command executed successfully.")
    print(f"Role mentioned: {role.name}")
    try:
        # Check if the user has permissions to manage roles
        if ctx.author.guild_permissions.manage_roles:
            print("permission granted")
            # Iterate through all members in the guild
            for member in ctx.guild.members:
                print("member found")
                # Check if the member has the specified role
                if role in member.roles:
                    print ("member role found")
                    # Remove the role from the member
                    await member.remove_roles(role)
                    await ctx.send(f"{member} has been removed from the role {role.name}.")
        else:
            await ctx.send("You don't have permission to manage roles.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    ctx.send(f"error")
    print(f"An error occurred: {error}")

# Run the bot
bot.run('REDACTED till next use as needed')
