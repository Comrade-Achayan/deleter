import asyncio
import os
from pyrogram import Client, filters

Bot = Client(
    "Deleter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)
