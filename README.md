# DiscordVoiceGhost

DiscordVoiceGhost is a Python-based Discord bot that can join and leave voice channels, mute and unmute itself, and clear its own messages in text channels. It is designed to be run as a self-bot, meaning that it uses your Discord account to perform actions.

## Setup

1. Clone the repository: `git clone https://github.com/Touahmiii/DiscordVoiceGhost.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a file named `.env` in the root directory of the project and add the following lines:
```
TOKEN=your_bot_token_here
GUILD_ID=your_guild_id_here
ADMIN_USER_ID=your_admin_user_id_here
```

Replace `your_bot_token_here` with your Discord bot token, `your_guild_id_here` with the ID of the guild you want the bot to connect to, and `your_admin_user_id_here` with your own Discord user ID.

4. Run the bot: `python bot.py`

## Usage

To use the bot, send it a direct message with one of the following commands:

- `join`: make the bot join a voice channel
- `leave`: make the bot leave the current voice channel
- `mute`: mute the bot in the current voice channel
- `unmute`: unmute the bot in the current voice channel
- `clear`: delete all messages sent by the bot in the current text channel
- `help`: display a help message

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
