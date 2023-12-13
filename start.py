from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://jut.su/", text="аниме "),
                types.InlineKeyboardButton(url="https://https://remanga.org//", text="манга"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about"),
            ]
        ]
    )
    await message.answer(
        f"""Привет, {message.from_user.full_name}. Если нравиться аниме и манга 
        """, reply_markup=kb
    )


к


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("О нас")