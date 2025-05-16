from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timezone, timedelta
import asyncio

API_ID = 
API_HASH = ''
PHONE_NUMBER = ''

client = TelegramClient('session_name', API_ID, API_HASH)

async def update_username():
    while True:
        now = datetime.now(timezone.utc) + timedelta(hours=8)
        new_username = now.strftime("%Y-%m-%d %H:%M") + " 🕡️ 明月"
        try:
            await client(UpdateProfileRequest(first_name=new_username))
            print(f"成功更新用户名: {new_username}")
        except Exception as e:
            print(f"更新失败: {e}")
        await asyncio.sleep(60)

async def main():
    await client.start(PHONE_NUMBER)
    await update_username()

with client:
    client.loop.run_until_complete(main())
