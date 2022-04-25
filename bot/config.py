#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", default=5168062, cast=int)
    API_HASH = config("API_HASH", default="04c049aa96d1cc87920b45b7fb43c0d0")
    BOT_TOKEN = config("BOT_TOKEN", default="5058183358:AAEE65GnRhfFi-DLb_3BX7V0m-QB4FRtIr8")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
