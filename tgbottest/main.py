import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from handlers import router

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5618063413:AAGhirNmHXiv-m_I95hGqLQSxAIlNq19ciw")
# Диспетчер
dp = Dispatcher()



# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())