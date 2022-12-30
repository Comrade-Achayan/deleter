import asyncio
import datetime
import os
from pyrogram import Client, filters

#AUTH_GROUP = os.environ["AUTH_GROUP"],

Bot = Client(
    "Deleter",
    bot_token = "5279408072:AAFma2GCbaFktWc0RJrxs_lvDDJQrqfFT2c",
    api_id = "2577247",
    api_hash = "aecd4418af2c891d4e659496397e74ae",
)

@Bot.on_message(filters.group & (filters.text | filters.reply | filters.photo))
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
