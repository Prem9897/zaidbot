## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQAiOCyELShHUzX-TTFDWkaSYQ1UTjZaLQ8YVCIuyQNlScl2aqaeE-ofsZhMuUwIrE0BmTWt1IgcMqb4bvCVPomcg1de1kM3hILhPpGu-wRm-mqJqS5MQwj6ptarRYS_ATCI2qKt4lMZ3Nxv9I3OgI-M2PBX-KoqivNCYjRVoTNwV-kzKTvI_Z14CCjCEkx0ouPPcX0XQQqb5057eOzSOkjfYkK1W_G3mkypkf91OzrItqTE4DsmU8NyY6QnSMZF3lSZgVl9KX9XKVMyIciQZrkmjZnoUQ4ryoL6-yFma4lb1GFjiixW3SL-orlakCDELL_cxeJln9G5lKBXxcubxpUDAAAAATDvfKMA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5545963604:AAFaDB-N19p1c9mPBruvzScQPdiJqM-7x30")
BOT_NAME = getenv("BOT_NAME", "Elisa")

API_ID = int(getenv("API_ID", "4277083"))
API_HASH = getenv("API_HASH", "bb0ddae0921fc020ce61faae2d1261d5")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://newdb:newdb@cluster0.ruafqzg.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Denvil")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Denvil_xdd")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "miselisarobot")
OWNER_ID = getenv("OWNER_ID", "5497627952")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Elisa_play")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Elisha_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "denvil_bots")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5497627952").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
