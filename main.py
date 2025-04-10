import os
import logging
from pyrogram import Client, idle
from modules import all_features
from modules.keep_alive import keep_alive

logging.basicConfig(level=logging.INFO)

app = Client(
    "anime_lord_bot",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN")
)

all_features.register_handlers(app)

if __name__ == "__main__":
    keep_alive()
    app.start()
    logging.info("Bot Started")
    idle()
    app.stop()
