import re
import os
from os import environ, getenv
from urllib.parse import urlsplit
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default=False):
    if isinstance(value, bool):
        return value
    value = str(value).strip().lower()
    if value in {"true", "yes", "1", "on", "enable", "enabled", "y"}:
        return True
    if value in {"false", "no", "0", "off", "disable", "disabled", "n"}:
        return False
    return default


SESSION = environ.get('SESSION', 'media_search')
API_ID = int(environ["API_ID"]) if environ.get("API_ID") else None
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'True'), True)

PICS = (environ.get('PICS', 'https://i.ibb.co/ch3n9wsf/x.jpg')).split() 
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/62efbcc4e7580b76530ba.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/e215d12bfd4fa2155e90e.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://telegra.ph/file/f983d857f3ce40795e4b8.jpg'))
FSUB_IMG = (environ.get('FSUB_IMG', 'https://i.ibb.co/cShkPjcZ/x.jpg')).split() 

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1982405151 6390284418').split()] 
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003116929269').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002995968359'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '  -1002995968359'))  
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002843957435'))  
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002995968359')) 
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002843957435') 
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002851154596') 
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

DATABASE_URI = environ.get("DATABASE_URI", "").strip()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'SilentXBotz_files')

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(environ.get('MULTIPLE_DB', "False"), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "").strip()
if not MULTIPLE_DB:
    DATABASE_URI2 = DATABASE_URI

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+dnlnGTiVZ3Q1MDk1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+fawa27AsAG5kM2E9')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Bobby_2606')
UPDATE_CHANNEL_LNK = environ.get('UPDATE_CHANNEL_LNK', 'https://t.me/+fawa27AsAG5kM2E9')

AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002843957435'))
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-1002843957435'))

IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'True'), True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002995968359'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002995968359'))
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/+ph5bMwjX_k45MDc1")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/+ph5bMwjX_k45MDc1")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/+ph5bMwjX_k45MDc1")

SHORTENER_API = environ.get("SHORTENER_API", "")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "softurl.in")

SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "shortxlinks.com")

SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "softurl.in")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "86450"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "86450"))

MOVIE_UPDATE_NOTIFICATION = is_enabled(environ.get("MOVIE_UPDATE_NOTIFICATION", "False"), False)
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "True"), True)
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = int(environ.get("PORT", "8089"))
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/moviesdiscussgroups') 
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
DELETE_TIME = int(environ.get("DELETE_TIME", "60"))  
LINK_MODE = is_enabled((environ.get('LINK_MODE', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', '-1002748763541'))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002869967157')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PM_SEARCH = is_enabled(environ.get('PM_SEARCH', 'True'), True)
EMOJI_MODE = is_enabled(environ.get('EMOJI_MODE', 'False'), False)
PAID_STREAM = is_enabled(environ.get('PAID_STREAM', 'True'), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["s01" , "s02" , "s03" , "s04", "s05" , "s06" , "s07" , "s08" , "s09" , "s10"]

STREAM_MODE = is_enabled(environ.get('STREAM_MODE', 'True'), True)

NO_PORT = is_enabled(environ.get('NO_PORT', 'False'), False)
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
HAS_SSL = is_enabled(getenv('HAS_SSL', 'False'), False)
_fqdn_env = str(getenv('FQDN', '')).strip()
if not _fqdn_env and ON_HEROKU and APP_NAME:
    _fqdn_env = f'{APP_NAME}.herokuapp.com'
elif not _fqdn_env:
    _fqdn_env = BIND_ADRESS

_has_url_scheme = '://' in _fqdn_env
_parsed_fqdn = urlsplit(_fqdn_env if _has_url_scheme else f'https://{_fqdn_env}')
FQDN = _parsed_fqdn.netloc or _parsed_fqdn.path.rstrip('/')
_url_scheme = _parsed_fqdn.scheme if _has_url_scheme else ('https' if getenv('FQDN') or ON_HEROKU or HAS_SSL else 'http')
if not getenv('FQDN') and not ON_HEROKU and not NO_PORT and ':' not in FQDN:
    FQDN = f'{FQDN}:{PORT}'
URL = f'{_url_scheme}://{FQDN.rstrip("/")}/'
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'SilentXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'SilentX'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

STAR_PREMIUM_PLANS = {
    1: "7day",
    30: "15day",    
    60: "1month", 
    120: "2month",   
}
Bot_cmds = {
    "start": "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
    "trendlist": "ɢᴇᴛ ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʟɪꜱᴛ",
    "myplan" : "ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ",
    "plan" :"ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴘʀɪᴄᴇ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "group_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "admin_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "details": "ꜱᴇᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ",
    "reset_group": "ʀᴇꜱᴇᴛ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ", 
    "stats": "ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ.",
    "delete": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
}
