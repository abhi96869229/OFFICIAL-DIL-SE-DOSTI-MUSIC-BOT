#MIT License

#Copyright (c) 2021 XD-Deepak


from config import Config
from pyrogram import Client
from config import Config
REPLY_MESSAGE=Config.REPLY_MESSAGE
if REPLY_MESSAGE is not None:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH,
        plugins=dict(root="userplugins")
        )
else:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH
        )
USER.start()


#DIL_SE_DOSTI
