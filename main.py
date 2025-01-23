import asyncio
from aiogram import Bot, Dispatcher, types

from app.handlers import router

async def main():
    bot = Bot(token='7689394185:AAF6-bgn2UowWXJje_xrF3zhTsojzNSvEGA')
    dp = Dispatcher(bot)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('logOff')