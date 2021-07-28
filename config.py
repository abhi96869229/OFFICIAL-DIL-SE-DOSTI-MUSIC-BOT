#MIT License

#Copyright (c) 2021 XD-Deepak
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://youtu.be/gnyW6uaUgk4")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1819814100 1847068212 856802597')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '2749695'))
    CHAT = int(os.environ.get("CHAT", "-1001415962984"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001543935568")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None



    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "ACKJQI-ZBQAKY-DLUJBU-ORWEPW-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 60))
    API_HASH = os.environ.get("API_HASH", "55ce46fea3a9b1b1f086a0748e9f9dd7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1914528594:AAHoNLcMhpTz2nbPgjI6Jisu3tGsgdim7xI") 
    SESSION = os.environ.get("SESSION_STRING", "AQCkGwlbh1DY8CYz5Vv6mHufheZKBKsAdiO6k811HePwEClw3GL2oxuu6DjAHXD5JUBFXGj9Zq7oUsL-8ugicT142wXrPl5C4nmOhy8Vc0TZgo6YOQspD4iBg_NJ2W1vm0kmEUj1MjfaaHIcUPBDFsACj38CD_xgkEylfL9T0NSer16EtzDZLjBrLQtj_0qlbPw6hVucqGpFWXHV2rbyvoJOBD8Cd4w8xz6Ii3ea4teR0oAOKC2S9vCdwxLJJnthOrQnuIoT-R-qSOuU1VTyL9qP6vh7gD7WOdJsoI6dqVfy2EX8EtBq89w6u1_SbMAEzyOPTZwMZo7IEsDViIjmrL7-a9OHQgA")
    playlist=[]
    msg = {}


#DIL_SE_DOSTI
