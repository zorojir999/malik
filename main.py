import asyncio

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "6942492036:AAHOJA-FqBJKHQpDVsI_LtCHGLctFPf1ejE"
bot =Bot(token=BOT_TOKEN)
dp = Dispatcher()
@dp.message()
async  def echo_message(message:types.Message):
    await message.answer(text=message.text)
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())