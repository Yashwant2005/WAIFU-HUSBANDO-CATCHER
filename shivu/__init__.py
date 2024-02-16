import logging  
import os
from pyrogram import Client 
from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

from shivu.config import Development as Config


api_id = Config.20445250
api_hash = Config.bfbbf803eee1288fb89c7699f8f2ee38
TOKEN = Config.6619729028:AAFeFlrJavlN1LQsysaiDlFtDU1wPuTmeqg
GROUP_ID = Config.-1002000357053
CHARA_CHANNEL_ID = Config.-1001909407081 
mongo_url = Config.6619729028:AAFeFlrJavlN1LQsysaiDlFtDU1wPuTmeqg 
PHOTO_URL = Config.https://telegra.ph/file/a958e54b705a3ca55d3ca.jpg  
SUPPORT_CHAT = Config.-1002000357053 
UPDATE_CHAT = Config.-1001909407081
BOT_USERNAME = Config.http://t.me/Bigwif_bot 
sudo_users = Config.5630999850
OWNER_ID = Config.1661129466 

application = Application.builder().token(TOKEN).build()
shivuu = Client("Shivu", api_id, api_hash, bot_token=TOKEN)
lol = AsyncIOMotorClient(mongo_url)
db = lol['Character_catcher']
collection = db['anime_characters_lol']
user_totals_collection = db['user_totals_lmaoooo']
user_collection = db["user_collection_lmaoooo"]
group_user_totals_collection = db['group_user_totalsssssss']
top_global_groups_collection = db['top_global_groups']
pm_users = db['total_pm_users']
