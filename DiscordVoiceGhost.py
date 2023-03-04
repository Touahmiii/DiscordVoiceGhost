import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

GUILD_ID = Insert_Your_GUILD_ID_Here
CHANNEL_ID = Insert_Your_CHANNEL_ID_Here
TOKEN = os.getenv('TOKEN')

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=True, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")

client.run(TOKEN)
