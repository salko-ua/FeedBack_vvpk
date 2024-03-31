from aiogram import types, Router, F
from src.keyboards import feedback_choise

router = Router()


@router.message(F.text == "😱 Переглянути відгук 😱")
async def cmd_start(message: types.Message):
    await message.answer(
        text="Куди ви хочете додати?", reply_markup=feedback_choise()
    )
