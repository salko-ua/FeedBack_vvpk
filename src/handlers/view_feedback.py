import time

from aiogram import types, Router, F
from src.keyboards import (
    feedback_review_choose,
    get_feedback_by_selection,
    back_by_selection,
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
    print(feedback)
    # not write plis who write feedback it is confidential information
    selection = (
            ('коледж' if feedback[2] == 'college' else '') +
            ('предмет' if feedback[2] == 'subject' else '') +
            ('викладача' if feedback[2] == 'teacher' else '')
    )
    selection_name = (
            (f"- \'{feedback[3]}\'" if feedback[2] == 'subject' else '') +
            (f"- \'{feedback[3]}\'" if feedback[2] == 'teacher' else '') +
            ('' if feedback[2] == 'college' else '')
    )
    text = (
        f"➡️ Відгук про {selection} {selection_name}\n"
        f"📝 Відгук: {feedback[4]}\n"
        #f"⭐️ Оцінка: {feedback[6]}\n"
        f"🕙 Створено користувачем - {time.strftime("%H:%M %D", time.localtime(feedback[5]))}"

    )
    await query.message.edit_text(text=text, reply_markup=await back_by_selection(feedback[2]))
    await query.answer()
