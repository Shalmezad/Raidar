# Standard build in libraries:
import asyncio
import configparser

# Pip installed libraries:
import discord


global_discord_client = discord.Client()


@global_discord_client.event
async def on_message(message):
    """
    Handles discord messages
    """
    if message.content.startswith("!raid"):
        await global_discord_client.send_message(message.channel, "Online")

# Set up discord
config = configparser.ConfigParser()
config.read('config/discord_secret.ini')
token = config['discord']['bot_token']
global_discord_client.run(token)
