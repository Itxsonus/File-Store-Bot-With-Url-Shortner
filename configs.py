import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "24139145"))
  API_HASH = os.environ.get("API_HASH", "726096d9244efd78707cd468ef89d431")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7082960629:AAHKOXinCBSE5vOwgSYOVozk57arcVhMudc")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Nexusnet_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002004195987"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "paisakamalo.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "d1c1c139cf4ac8893ed9433c9fc0436cbf0ee650")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "897584437"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://rockysingh123ops:nJuBxIL2Nqwn16xB@cluster0.0cjsezo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002137981012")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002074541840"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/KingVj01)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
