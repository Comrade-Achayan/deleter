import asyncio
import datetime
import os
from pyrogram import Client, filters

AUTH_GROUP = os.environ["AUTH_GROUP"],

Bot = Client(
    "Deleter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

@Bot.on_message(filters.group & (filters.text | filters.reply | filters.photo), groups=0)
async def dlt(bot, update):
    await asyncio.sleep(10)
    await update.delete()

@Bot.on_message(filters.group & filters.bot)
async def det(bot, update):
    await asyncio.sleep(120)
    await update.delete()

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text="hi",         #START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
    )

Bot.run()
