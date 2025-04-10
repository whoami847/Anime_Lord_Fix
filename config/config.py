import os

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
ADMIN_USERS = [int(x) for x in os.getenv("ADMIN_USERS", "").split()]
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", None)
