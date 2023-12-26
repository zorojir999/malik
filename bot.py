from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

BOT_TOKEN = '6770894028:AAFOSGU-gfUfDsyfdAyDocCWpIiJTaIbAbA'
load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()