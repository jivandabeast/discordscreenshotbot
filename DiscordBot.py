#!/usr/bin/env python

# Script for testing the discord bot responding to user input so as to facilitate creating the Chegg bot

import os
import subprocess
import discord
import time
from dotenv import load_dotenv
from discord.ext import commands
from subprocess import call

# Import the bot token from the .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Set the command prefix for the bot
bot = commands.Bot(command_prefix='!')

# Command for screenshoting the requested page 
@bot.command(name='screenshot', help='Takes a screenshot of a webpage')
@commands.has_role('Screenshot')
async def screenshot(ctx, arg):
    call(["./FullpageScreenshot.sh", arg])
    time.sleep(2)
    image=discord.File('/path/to/screenshot.png')
    await ctx.send(file=image)
bot.run(token)
