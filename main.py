import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
BOT_TOKEN = "6942492036:AAHOJA-FqBJKHQpDVsI_LtCHGLctFPf1ejE"
bot = Bot(token=getenv(BOT_TOKEN))
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await  message.answer(f"{message.text}, {message.from_user.first_name},{message.from_user.username}")
async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
        asyncio.run(main())