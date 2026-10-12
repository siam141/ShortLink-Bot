import os
from typing import List

API_ID = os.environ.get("API_ID", "18013154")
API_HASH = os.environ.get("API_HASH", "93c6f3c43ede0082aceebfff185cf5ff")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8668760056:AAGzRndPpjzNVJ2GC-9yyxGe4CYNPCByv6o")
ADMIN = int(os.environ.get("ADMIN", "8530165612"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004411647916"))
DB_URI = os.environ.get("DB_URI", "mongodb+srv://siamvai:siamvai@cluster0.1bungtm.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "approve")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
PING_URL = os.environ.get("PING_URL", "") # Service URL for Keep-Alive
VERSION = os.environ.get("VERSION", "3.0")
