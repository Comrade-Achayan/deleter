import asyncio
import os
from pyrogram import Client, filters

AUTH_GROUP = os.environ["AUTH_GROUP"],

Bot = Client(
    "Deleter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

@Bot.on_message(filters.chat(AUTH_GROUP) & (filters.text | filters.photo))
async def dlt(bot, update):
    mgd = update.chat.title
    await asyncio.sleep(120)
    await update.delete()


Bot.run
