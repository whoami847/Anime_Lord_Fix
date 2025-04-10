from pyrogram import Client, idle
from config.config import API_ID, API_HASH, BOT_TOKEN
from bot.all_features import init_handlers
import asyncio
from webserver import run as start_webserver

app = Client("anime_lord_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

init_handlers(app)  # হ্যান্ডলার আগে যুক্ত করো

async def main():
    await app.start()
    print("✅ Bot Started")
    await start_webserver()
    await idle()
    await app.stop()
    print("🛑 Bot Stopped")

if __name__ == "__main__":
    asyncio.run(main())
