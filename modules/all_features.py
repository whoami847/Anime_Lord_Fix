from pyrogram import filters
from pyrogram.types import Message
from pyrogram.client import Client


def register_handlers(app: Client):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        await message.reply_text("Aɴɪᴍᴇ Lᴏʀᴅ Bᴏᴛ ɪs Aʟɪᴠᴇ!")

    @app.on_message(filters.command("help"))
    async def help_handler(client, message: Message):
        await message.reply_text("Hᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ:\nUse /genlink or /batch to generate links.")

    @app.on_message(filters.command("batch"))
    async def batch_handler(client, message: Message):
        await message.reply_text("Send multiple files together to get a batch link.")

    @app.on_message(filters.command("genlink"))
    async def genlink_handler(client, message: Message):
        await message.reply_text("Send me a file, and I will generate a direct link.")

    @app.on_message(filters.command("forcesub"))
    async def forcesub_handler(client, message: Message):
        await message.reply_text("Force Subscription settings here. (Admin only)")

    @app.on_message(filters.command("users"))
    async def users_handler(client, message: Message):
        await message.reply_text("User list & management panel. (Admin only)")

    @app.on_message(filters.command("files"))
    async def files_handler(client, message: Message):
        await message.reply_text("File/message control panel. (Admin only)")

    @app.on_message(filters.command("status"))
    async def status_handler(client, message: Message):
        await message.reply_text("Bot status, user count, and uptime. (Admin only)")

    @app.on_message(filters.command("auto_del"))
    async def auto_del_handler(client, message: Message):
        await message.reply_text("Auto-delete message settings. (Admin only)")

    @app.on_message(filters.command("logs"))
    async def logs_handler(client, message: Message):
        await message.reply_text("Fetching logs... (Admin only)")

    @app.on_message(filters.command("channel"))
    async def channel_handler(client, message: Message):
        await message.reply_text("Manage connected channels. (Admin only)")

    @app.on_message(filters.command("broadcast"))
    async def broadcast_handler(client, message: Message):
        await message.reply_text("Broadcasting message to users... (Admin only)")

    @app.on_message(filters.command("stats"))
    async def stats_handler(client, message: Message):
        await message.reply_text("Bot statistics. (Admin only)")

    @app.on_message(filters.command("cmd"))
    async def cmd_handler(client, message: Message):
        await message.reply_text("Admin Bot Control Panel: /logs, /channel, /broadcast, /stats")

    @app.on_message(filters.command("restart"))
    async def restart_handler(client, message: Message):
        await message.reply_text("Bot is restarting... (Admin only)")

    @app.on_message(filters.command("button-c"))
    async def buttonc_handler(client, message: Message):
        await message.reply_text("Custom Button Creation Panel. (Admin only)")

    # Inbuilt feature: styled small caps font - no command needed
