class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6570434731"
    sudo_users = "6570434731", "6070038322"
    GROUP_ID = -1002069282863
    TOKEN = "6968464825:AAESoG4AK4LRccpTX2ksx1DEF3EZo0FExa8"
    mongo_url = "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/06355103255bdeaf79912.jpg", "https://telegra.ph/file/8d7966de81833aca719f5.jpg"]
    SUPPORT_CHAT = "anime_savage_Group"
    UPDATE_CHAT = "Pro_Bot_Support"
    BOT_USERNAME = "Guess_Your_Characters_ProBot"
    CHARA_CHANNEL_ID = "-1002104813341"
    api_id = "27684245"
    api_hash = "22c33e48a7697c767c5e40bda82a8db9"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
