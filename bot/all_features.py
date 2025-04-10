from pyrogram.types import Message
from pyrogram import Client, filters
from config.config import ADMIN_USERS

def init_handlers(app: Client):
    
    @app.on_message(filters.command("start"))
    async def start(_, message: Message):
        await message.reply_text("Aɴɪᴍᴇ Lᴏʀᴅ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.")

    @app.on_message(filters.command("help"))
    async def help(_, message: Message):
        await message.reply_text("Uꜱᴇ /start ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇɴᴇꜱꜱ.\n/batch, /genlink, /forcesub, /users etc. available.")

    @app.on_message(filters.command("batch"))
    async def batch(_, message: Message):
        await message.reply_text("Sᴀᴠɪɴɢ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇꜱ...")

    @app.on_message(filters.command("genlink"))
    async def genlink(_, message: Message):
        await message.reply_text("Gᴇɴᴇʀᴀᴛɪɴɢ ꜱʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ...")

    @app.on_message(filters.command("forcesub"))
    async def forcesub(_, message: Message):
        await message.reply_text("Fᴏʀᴄᴇ Sᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴄʜᴇᴄᴋɪɴɢ...")

    @app.on_message(filters.command("users") & filters.user(ADMIN_USERS))
    async def users(_, message: Message):
        await message.reply_text("Mᴀɴᴀɢɪɴɢ ʙᴏᴛ ᴜꜱᴇʀꜱ...")

    @app.on_message(filters.command("files") & filters.user(ADMIN_USERS))
    async def files(_, message: Message):
        await message.reply_text("Fɪʟᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ꜱᴇᴛᴛɪɴɢꜱ...")

    @app.on_message(filters.command("status") & filters.user(ADMIN_USERS))
    async def status(_, message: Message):
        await message.reply_text("Bᴏᴛ ᴜᴘᴛɪᴍᴇ & ᴜꜱᴇʀ ᴄᴏᴜɴᴛ ᴄʜᴇᴄᴋ...")

    @app.on_message(filters.command("auto_del") & filters.user(ADMIN_USERS))
    async def auto_del(_, message: Message):
        await message.reply_text("Aᴜᴛᴏ ᴅᴇʟᴇᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ...")

    @app.on_message(filters.command("cmd") & filters.user(ADMIN_USERS))
    async def cmd(_, message: Message):
        await message.reply_text("Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅꜱ: /logs, /channel, /broadcast, /stats")

    @app.on_message(filters.command("restart") & filters.user(ADMIN_USERS))
    async def restart(_, message: Message):
        await message.reply_text("Rᴇꜱᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")

    @app.on_message(filters.command("button-c") & filters.user(ADMIN_USERS))
    async def button_create(_, message: Message):
        await message.reply_text("Cʀᴇᴀᴛɪɴɢ ᴄᴜꜱᴛᴏᴍ ʙᴜᴛᴛᴏɴ...")
