# Discord Screenshot Bot
A discord bot useful for taking screenshots of pages sent in by users. There's probably a better way to do this, but for my purposes this was the best option that I could come up with.

# Table of Contents

# Dependencies
The bot has a few dependencies:
* `firefox`
* `i3 window manager`
* `xdotool`
* `python 3`
* `os`
* `subprocess`
* `discord.py`
* `time`
* `dotenv`

# Setting up the bot scripts
1. Edit the `.env` file to contain the Discord Token information that you can find [here.](https://discordpy.readthedocs.io/en/latest/discord.html)
2. Edit the `DiscordBot.py` file (line 26) to change the file path for the screenshots to the location where FireFox is saving them (likely your downloads folder.)
3. If you wish to change the command prefix, edit the `DiscordBot.py` file (line 18) to change the prefix from `!`. 

# Deploying the bot
1. Once you've entered all the necessary information into the files, its as simple as running the command (make sure your working directory is in the folder with the two scripts)
	- `python3 DiscordBot.py`
2. You may want to use tmux to make your life a little easier

# Notes
