import os

API_ID = int(os.environ.get("API_ID", "23458837"))
API_HASH = os.environ.get("API_HASH", "8fd8e59e53a2bec74d18134925050e5b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7081565062:AAFFOZehkLH4JdtNTvi88UTZHEPKoEsOYBQ")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "2139317596")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "6058139652"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'EonixCore')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
