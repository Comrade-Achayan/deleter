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

@Bot.on_message(filters.group & (filters.text | filters.reply | filters.photo))
async def dlt(bot, update):
    await update.reply(text="")
    await asyncio.sleep(120)
    await update.delete()
   # await bot.delete_messages(
  #           chat_id=update.chat_id,
    #         message_ids=update.message_id
 #   )

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    
   # if not await db.is_user_exist(update.from_user.id):
	   # await db.add_user(update.from_user.id)
    
    await update.reply_text(
        text="hi",         #START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
	#reply_markup=START_BUTTONS
    )

Bot.run()
