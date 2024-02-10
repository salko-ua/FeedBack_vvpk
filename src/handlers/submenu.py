from aiogram import types, Router, F
from src.keyboards import menu, trety_keyboard, dryga_keyboard, teacher

router = Router()


@router.message(F.text == "🏫 Коледж 🔔")
async def cmd_start(message: types.Message):
    await message.answer(text="Виберіть варіант:", reply_markup=trety_keyboard())


@router.message(F.text == "📚 Предмети 📚")
async def cmd_start(message: types.Message):
    await message.answer(text="Виберіть предмет:", reply_markup=dryga_keyboard())


@router.message(F.text == "👨‍🏫 Викладачі 👩‍🏫")
async def cmd_start(message: types.Message):
    await message.answer(text="Виберіть викладача", reply_markup=teacher())


@router.message(F.text == "⬅️ Назад ↩️")
async def cmd_start(message: types.Message):
    await message.answer(text="Головне меню:", reply_markup=menu())
