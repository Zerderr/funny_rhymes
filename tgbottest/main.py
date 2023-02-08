import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from handlers import router
logging.basicConfig(level=logging.INFO)
bot = Bot(token="notokenhere:D")
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
