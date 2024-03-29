from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from src.keyboards import feedback_choise
from src.data_base import Database

router = Router()
"""
1.Користувач може переглядати відгуки
2.Користувач може додавати відгуки
3.Адмін повинен перевіряти і приймати або не приймати відгуки
5.Відповідь на команду /start
"""


@router.message(F.text == "📝 Додати відгук 📒")
async def add_feedback(message: types.Message):
    await message.answer(
        text="Куди ви хочете додати?", reply_markup=feedback_choise()
    )


@router.message(F.text == "😱 Переглянути відгук 😱")
async def cmd_start(message: types.Message):
    await message.answer(
        text="Куди ви хочете додати?", reply_markup=feedback_choise()
    )


@router.message(F.text == "📋 Про бота 📋")
async def cmd_start(message: types.Message):
    await message.answer(text="Інформація про бота:")


@router.callback_query(F.data == "Сховати ❌")
async def hide(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    await state.clear()


@router.message(F.text == "📈 Статистика 📉")
async def cmd_start(message: types.Message):
    db = await Database.setup()

    caption = (
        "<b>Статистика</b> 📊:\n",
        f"  • Користувачів 👥: {await db.count_users()}\n",
        f"  • Відгуків 📝: {0}\n",
        f"     ╰ Викладачів 👨‍🏫: {0}\n",
        f"     ╰ Предметів 📕: {0}\n",
        f"     ╰ Коледжу 🏫: {0}\n",
        f"  • Прийнятих відгуків ✅: {0}\n",
        f"  • Відхилених відгуків 🚫: {0}\n",
    )

    await message.answer(text="".join(caption), parse_mode="HTML")
