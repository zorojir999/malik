import asyncio
from aiogram import types
from aiogram.filters import Command
import logging
from bot import Bot, dp
from handlers import (
    start_router,
    pic_router,
    manga_router,
    echo_router,

)


async def main():
    await Bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку"),
        types.BotCommand(command="courses", description="Показать мангу"),
    ])

    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(manga_router)

    dp.include_router(echo_router)
    await dp.start_polling(Bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())