from aiogram import types, Router
from aiogram.filters.command import Command
from src.keyboards import menu
from src.data_base import Database
from datetime import date
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    db = await Database.setup()
    if not await db.user_exists_sql(user_id=message.from_user.id):
        await db.add_users_sql(
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            date_join=date.today(),
        )

    await message.answer(text="Доброго дня!", reply_markup=menu())
