#!/usr/bin/env python

# Script for testing the discord bot responding to user input so as to facilitate creating the Chegg bot

import os
import subprocess
import discord
import time
from dotenv import load_dotenv
from discord.ext import commands

# Import the bot token from the .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Set the command prefix for the bot
bot = commands.Bot(command_prefix='!')

# A simple test command, to ensure that regular message sending is working
@bot.command(name='test', help='Its a test function you idiot')
async def test(ctx):
    response = 'Well, I guess it somehow worked'
    await ctx.send(response)

# The meat and potatoes, when this command is called the screenshot script is executed and the resulting image is sent
@bot.command(name='screenshot', help='Takes a screenshot of a webpage')
async def screenshot(ctx):
    subprocess.call("./FullpageScreenshot.sh")
    time.sleep(2)
    image=discord.File('/path/to/screenshot.png')
    await ctx.send(file=image)
bot.run(token)
