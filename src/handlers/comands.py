from aiogram import types, Router
from aiogram.filters.command import Command
from src.keyboards import menu

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text="Доброго дня!", reply_markup=menu())
