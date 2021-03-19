# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
This is a Permanent File Store Bot 
Send me any TELEGRAM file and I'll store it and generate a permanent shareable link!! ❤️
**BY : @CyrusProjects**
**FOR: @Flix_movies_lk
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Owner:** @cyrusexplode

I am not the person that coding the source code of this bot. So credits goes to him, that the creator of this bot's source code.

[Donate Now](https://www.paypal.me/slpres) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\n.

Send a valid media to get its public shareable link.
"""
