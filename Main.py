import asyncio
from aiogram import Bot, Dispatcher

from app.Handler import router
from app.DataBase import Models





async def main():
    #await async_main()
    bot = Bot(token = '7274024551:AAGeMcBd9E5Lg2WoV_PX09s7koIucJoFxwU')
    dp  = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    Models.db

if __name__ =='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot is off")