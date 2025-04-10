from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from keep_alive import keep_alive  # ঠিক করা হয়েছে
from modules.all_features import register_handlers


# বট ক্লায়েন্ট তৈরি করা
app = Client(
    "AnimeLordBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# হ্যান্ডলার রেজিস্টার করা
register_handlers(app)


# হেলথচেক সার্ভার চালু করা
keep_alive()

# বট চালু রাখা
app.start()
print("Bot is now alive and running...")
idle()
app.stop()
print("Bot stopped.")
