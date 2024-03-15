import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "25639252"))
API_HASH = getenv("API_HASH", "42db0fd56c51ff2b94cf064838eba7c1")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6956372908:AAGVq1qX8mbjNGolU0Fa2MsLGLcEu2U-8Y4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")

###MUST_JOIN = getenv("MUST_JOIN", "gabutan07")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002146931876"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5061180769))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "musik")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "378ddd21-4ab1-46a8-b3ef-ef9c96f1d247")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/jaadisini/venom",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/stayheresay")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/cillsupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGHOVQAUfHEKgcxxY2DYWyJ89aGAYqmXIqde5AxqzAQksg9txK5IKU7fw9fdb5IJISZ8Y518cmS1UNlQ4KSgVfSzDaOkxEerPwbqQwt-wLnjcV0BEWNFFUpRM5xcPOap31n5gdTtEMvf26_G3y8cCwDzjHz5uAlq7TuMDsdYWF4iOqqGXD3HY8p1eOm0v_Y41Nq249NugJEzKkO3sFHfBC_9s-M4td_lT-wBgGkqYYMCoTbQFn7emPdPOLGRE8N0t3lfdxcLJfRqjLGmfb97fqNh1tzxqqxAUMeQfZkt43_nHAz7kTe9nZYyfJWqtyiklF7xHkojRm1eoreIfQA5J9S5pvjvgAAAAA3v5y-AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph//file/768e52d46733806e6beee.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph//file/768e52d46733806e6beee.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
STATS_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
