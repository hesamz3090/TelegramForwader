import asyncio
from pyrogram import Client
import config

client = Client(config.phone_number, config.api_id, config.api_hash, phone_number=config.phone_number)


async def main():
    async with client as app:
        async for message in app.get_chat_history(config.from_chat):
            try:
                await app.forward_messages(config.to_chat, config.from_chat, message.id)
            except Exception as e:
                print(str(e))


asyncio.run(main())
