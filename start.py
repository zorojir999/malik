from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://remanga.org/", text="Манга  сайт"),
                types.InlineKeyboardButton(url="https://renovels.org/", text="сайт новел"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about"),
                types.InlineKeyboardButton(text="Каталог ", callback_data="catalog"),
            ]
        ]
    )
    await message.answer(
        f"""Привет, {message.from_user.full_name}.Здесь ты можешь почитать новеллы и мангу .
        """, reply_markup=kb
    )


# handler = обработчик


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "catalog")
async def catalog(callback: types.CallbackQuery):
    pass