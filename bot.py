from pyrogram import idle, __version__
from pyrogram.raw.all import layer
import logging
import logging.config
import time
import asyncio
from datetime import date, datetime
import pytz
from aiohttp import web
from info import *

missing_settings = [
    name for name, value in (
        ("API_ID", API_ID),
        ("API_HASH", API_HASH),
        ("BOT_TOKEN", BOT_TOKEN),
        ("DATABASE_URI", DATABASE_URI),
    ) if not value
]
if MULTIPLE_DB and not DATABASE_URI2:
    missing_settings.append("DATABASE_URI2")
if missing_settings:
    raise RuntimeError(
        "Missing required environment variables: " + ", ".join(missing_settings)
    )

from database.ia_filterdb import Media, Media2
from database.users_chats_db import db
from utils import temp
from Script import script
from plugins import web_server, check_expired_premium 
from Lucia.Bot import SilentX
from Lucia.Bot.clients import initialize_clients
import pyrogram.utils

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
botStartTime = time.time()

async def SilentXBotz_start():
    print('Initalizing Your Bot!')
    await SilentX.start()
    bot_info = await SilentX.get_me()
    SilentX.username = bot_info.username
    await initialize_clients()
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    if MULTIPLE_DB:
        await Media2.ensure_indexes()
        print("Multiple Database Mode On. Now Files Will Be Save In Second DB If First DB Is Full")
    else:
        print("Single DB Mode On ! Files Will Be Save In First Database")
    me = await SilentX.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    temp.B_LINK = me.mention
    SilentX.username = '@' + me.username
    SilentX.loop.create_task(check_expired_premium(SilentX))
    logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(script.LOGO)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await SilentX.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(temp.B_LINK, today, time))
    for admin in ADMINS:
        try:
            await SilentX.send_message(chat_id=admin, text=f"<b>๏[-ิ_•ิ]๏ {me.mention} Restarted ✅</code></b>")
        except Exception:
            logging.exception("Failed to send a restart notification")
    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, BIND_ADRESS, PORT).start()
    try:
        await idle()
    finally:
        await app.cleanup()
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(SilentXBotz_start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')
