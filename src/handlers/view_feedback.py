from aiogram import types, Router, F
from src.keyboards import (
    feedback_review_choose,
    get_feedback_by_selection,
    menu,
)
from src.data_base import Database

router = Router()

"👨‍🏫 Викладачі 👩‍🏫"
"📚 Предмети 📚"
"🏫 Коледж 🔔"


@router.callback_query(F.data == "⬅️ Назад ↩️")
async def back(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer(text="Головне меню:", reply_markup=menu())


@router.message(F.text == "😱 Переглянути відгук 😱")
async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer(
        text="Виберіть які відгуки ви хочете переглянути:",
        reply_markup=feedback_review_choose(),
    )


@router.callback_query(F.data == "teacher")
@router.callback_query(F.data == "subject")
@router.callback_query(F.data == "college")
async def feedback_review(query: types.CallbackQuery):
    await query.message.answer(
        text=f"{1} Сторінка відгуків:",
        reply_markup=await get_feedback_by_selection(query.data, 1),
    )
    await query.answer()


@router.callback_query(F.data.startswith("⬅️ Назад"))
@router.callback_query(F.data.startswith("Вперед ➡️"))
async def feedback_review(query: types.CallbackQuery):
    page = int(query.message.text.split()[0])

    selection = query.data.split()[2]
    page = page + 1 if query.data.startswith("Вперед ➡️") else page - 1
    await query.message.edit_text(
        text=f"{page} Сторінка відгуків:",
        reply_markup=await get_feedback_by_selection(selection, page),
    )
    await query.answer()


@router.callback_query(F.data.startswith("SEE FEEDBACK"))
async def see_feedback(query: types.CallbackQuery):
    db = await Database.setup()
    feedback_id = query.data.split()[2]
    feedback = await db.get_feedback(feedback_id)
    await query.message.answer(
        text=f"Відгук від {feedback[1]}:\n\n{feedback[2]}"
    )
    await query.answer()
