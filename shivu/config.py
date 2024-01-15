class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6570434731"
    sudo_users = "6570434731",
    GROUP_ID = -1002069282863
    TOKEN = "6968464825:AAESoG4AK4LRccpTX2ksx1DEF3EZo0FExa8"
    mongo_url = ""
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "anime_savage_Group"
    UPDATE_CHAT = "Pro_Bot_Suppport"
    BOT_USERNAME = "Guess_Your_Characters_ProBot"
    CHARA_CHANNEL_ID = "-1002104813341"
    api_id = "27684245"
    api_hash = "22c33e48a7697c767c5e40bda82a8db9"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
