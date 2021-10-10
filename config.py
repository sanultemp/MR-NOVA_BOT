# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 8901416  # integer value, dont use ""
    API_HASH = "ff05861c1bf07edcb2644f7f308584df"
    TOKEN = "2092508379:AAEErte80CltHGUnmprsONZhONKfpQMWuwY"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1998893767  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "IamtheLuciferMorningstar"
    SUPPORT_CHAT = "StarKingBots"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001699950970
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001699950970
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://apfvtvvegpwgwu:353dd24c345f3173c443684b280e585001bfc75d79621d31e91b81fbccc31251@ec2-23-23-128-222.compute-1.amazonaws.com:5432/degnv17tvn1nqn"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "INRH4jNOx5OtaDWsiQYDmIh3WmhV2PNAo~AFt4K__vjXHeUEhgyHaYO6FZd2P~F8"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's - "1998893767" (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - "1998893767" (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "ZUDIT7VOAVFIPV46"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "9ZJDVJYOGNOW"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "hmmm"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "hmmm"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
