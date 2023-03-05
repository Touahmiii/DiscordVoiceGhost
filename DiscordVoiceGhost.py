# Import packages
import discord
import os
import asyncio
import textwrap
from dotenv import load_dotenv
from discord.ext import commands

# Load environment variables from the .env file
load_dotenv()

# Configure constants
GUILD_ID = os.getenv('GUILD_ID')  # The ID of the guild this bot needs to connect to
TOKEN = os.getenv('TOKEN')       # Retrieve the token stored as an environment variable
ADMIN_USER_ID = os.getenv('ADMIN_USER_ID')       # Replace with the user ID of the admin user

# Initialize the client
client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

# When the client is ready, print a message to the console
@client.event
async def on_ready():
    os.system('clear')  # Clear the console window
    print(f'Logged in as {client.user} ({client.user.id})')

# Listen for messages from the admin user in a direct message
@client.event
async def on_message(message):
    if message.author.id == int(ADMIN_USER_ID) and isinstance(message.channel, discord.DMChannel):
        if message.content.lower() == 'join':
            # Get the voice channel to join and connect to it
            guild = client.get_guild(int(GUILD_ID))
            channels = guild.voice_channels
            # Create a list of voice channel names and their IDs
            channel_list = [f'{index}: {channel.name} ({channel.id})' for index, channel in enumerate(channels)]
            # Send a message to prompt the user to choose a voice channel
            prompt = '\n'.join(channel_list) + '\n\nChoose a voice channel by typing its number:'
            for chunk in textwrap.wrap(prompt, width=2000, replace_whitespace=False):
                await message.channel.send(chunk)
            # Wait for the user to respond with a number
            def check(response):
                return response.author == message.author and response.channel == message.channel and response.content.isdigit()
            response = await client.wait_for('message', check=check)
            index = int(response.content)
            if index < 0 or index >= len(channels):
                await message.channel.send(f'Invalid selection. Please choose a number between 0 and {len(channels)-1}.')
            else:
                vc = await channels[index].connect()
                # Send a message confirming that the bot has joined the voice channel
                await message.channel.send(f"Joined voice channel {vc.channel.name}")
        elif message.content.lower() == 'leave':
            # Disconnect from the voice channel
            for vc in client.voice_clients:
                if vc.guild.id == int(GUILD_ID):
                    await vc.disconnect()
                    # Send a message confirming that the bot has left the voice channel
                    await message.channel.send(f"Left voice channel {vc.channel.name}")
                    break
        elif message.content.lower() == 'help':
            # Send a help message to the user
            help_message = """
            **List of available commands:**
            - join: make the bot join a voice channel
            - leave: make the bot leave the current voice channel
            - mute: mute the bot in the current voice channel
            - unmute: unmute the bot in the current voice channel
            - clear: delete all messages sent by the bot in the current text channel
            - help: display this help message
            
            To use a command, send a direct message to the bot with the command name.
            """
            await message.channel.send(help_message)
        elif message.content.lower() == 'mute':
            # Mute the bot in the voice channel
            for vc in client.voice_clients:
                if vc.guild.id == int(GUILD_ID):
                    await vc.guild.change_voice_state(channel=vc.channel, self_mute=True)
                    await message.channel.send(f"Muted in voice channel {vc.channel.name}")
                    break
        elif message.content.lower() == 'unmute':
            # Unmute the bot in the voice channel
            for vc in client.voice_clients:
                if vc.guild.id == int(GUILD_ID):
                    await vc.guild.change_voice_state(channel=vc.channel, self_mute=False)
                    await message.channel.send(f"Unmuted in voice channel {vc.channel.name}")
                    break
        elif message.content.lower() == 'clear':
            async with message.channel.typing():
                messages_to_delete = await message.channel.history(limit=None).flatten()
                deleted = 0
                for msg in messages_to_delete:
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                            deleted += 1
                        except discord.errors.Forbidden:
                            pass
                    elif isinstance(message.channel, discord.TextChannel):
                        break
                    await asyncio.sleep(0.5) # Wait for half a second before deleting the next message
                await message.channel.trigger_typing() # Stop the typing indicator

# Run the client
client.run(TOKEN)
