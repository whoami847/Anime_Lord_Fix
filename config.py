import os

API_ID = int(os.getenv("API_ID", "21463947"))
API_HASH = os.getenv("API_HASH", "39d6a5245f670ee68c507e274b3c7b3d")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7327021662:AAGYxW11fymRBqnDGUUTCLfP9FG0zrv1jKs")

# Admin user list
ADMIN_USERS = [int(x) for x in os.getenv("ADMIN_USERS", "7282066033").split()]

# Optional Force Subscribe channel username
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", None)
