# DiscordVoiceGhost

DiscordVoiceGhost is a Python script that allows you to automatically join a specified voice channel on Discord as a self-bot. This script is designed for Discord users who want to automatically join a specific voice channel whenever they log in.

## Prerequisites

Before you can use DiscordVoiceGhost, you will need to install the following software:

- Python 3.8 or higher
- discord.py-self

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/Touahmiii/DiscordVoiceGhost.git`
2. Navigate to the directory where the repository was cloned
3. Install the required Python packages using `pip install -r requirements.txt`

## Obtaining a Discord Token

1. Open Discord in your web browser or desktop app
2. Log in to your account
3. Press `Ctrl+Shift+I` to open the Developer Tools
4. Click the `Application` tab
5. Select `Local Storage` from the sidebar
6. Click on `https://discord.com` to expand the options
7. Find the `token` key and copy the value

**Note**: Make sure to keep your Discord token secret and never share it with anyone. If someone gets hold of your token, they can use your Discord account without your permission.

## Usage

1. Navigate to the directory where the repository was cloned
2. Create a `.env` file and add your Discord token as follows:
```
TOKEN=your_discord_token_here
```
3. Replace `GUILD_ID` and `CHANNEL_ID` in the `DiscordVoiceGhost.py` file with the IDs of the guild and voice channel you want to join
4. Run the script using `python DiscordVoiceGhost.py`

## Contributing

If you find any bugs or have suggestions for improvement, please feel free to contribute to this project by submitting a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
