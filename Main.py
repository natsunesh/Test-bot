import asyncio
from aiogram import Bot, Dispatcher

from app.Handler import router
from app.DataBase.Models import async_main





async def main():
    await async_main()
    bot = Bot(token = "")
    dp  = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    

if __name__ =='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot is off")
