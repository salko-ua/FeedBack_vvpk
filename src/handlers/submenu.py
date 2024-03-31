import time

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from random import choice

from src.keyboards import menu, dryga_keyboard, teacher
from src.data_base import Database
from src.keyboards import accept_reject_feedback

router = Router()


class FSMFeedBack(StatesGroup):
    chose_name_selection = State()
    write_feedback = State()


@router.message(F.text == "🏫 Коледж 🔔")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(text="Напишіть відгук:")
    await state.update_data(selection="collage")
    await state.update_data(selection_name=None)
    await state.set_state(FSMFeedBack.write_feedback)


@router.message(F.text == "📚 Предмети 📚")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(
        text="Виберіть предмет:", reply_markup=dryga_keyboard()
    )
    await state.update_data(selection_name=message.text)
    await state.update_data(selection="subject")
    await state.set_state(FSMFeedBack.chose_name_selection)


@router.message(F.text == "👨‍🏫 Викладачі 👩‍🏫")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(text="Виберіть викладача", reply_markup=teacher())
    await state.update_data(selection_name=message.text)
    await state.update_data(selection="teacher")
    await state.set_state(FSMFeedBack.chose_name_selection)


@router.callback_query(FSMFeedBack.chose_name_selection)
async def add_feedback1(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()

    if query.data == "Сховати ❌":
        await state.clear()
        await query.answer("Дію успішно відмінено ✅")
        return

    await state.update_data(selection_name=query.data)
    await query.message.answer(f"Напишіть відгук: ")
    await state.set_state(FSMFeedBack.write_feedback)


@router.message(F.text, FSMFeedBack.write_feedback)
async def add_feedback2(message: types.Message, state: FSMContext):
    db = await Database.setup()
    data = await state.get_data()
    await state.clear()

    date = int(time.time())

    feedback_id = ""
    for x in range(8):
        feedback_id += choice(list("1234567890ABCDEFGHIGKLMNOPQRSTUVYXWZ"))

    await db.add_feedback(
        feedback_id=feedback_id,
        user_id=message.from_user.id,
        selection=data["selection"],
        selection_object=data["selection_name"],
        feedback=message.text,
        data_sending=date,
        stars="⭐⭐⭐⭐⭐",
        status=0,
    )

    text_to_admin = (
        f"🗳 Відгук: {feedback_id}\n"
        f"➡️ Від: {message.from_user.id}\n"
        f"🎛 Тип: {data['selection']}\n"
        f"  ╰ {'І\'мя/Назва:' + data['selection_name'] + '\n' if data["selection_name"] is not None else ''}"
        f"📊 Відгук: {message.text}\n"
        f"🕙 Дата надсилання: {time.strftime("%D %H:%M", time.localtime(date))}\n"
        f"⭐️ Оцінка: ⭐⭐⭐⭐⭐\n"
        f"🧑🏿‍💻 Статус: Очікує на перевірку 🟡\n"
    )

    await message.answer(
        text=f"Ваш відгук надіслано на перевірку", reply_markup=menu()
    )
    await message.bot.send_message(
        chat_id=2138964363, text=text_to_admin, reply_markup=accept_reject_feedback(feedback_id=feedback_id)
    )
    await message.bot.send_message(
        chat_id=815020946, text=text_to_admin, reply_markup=accept_reject_feedback(feedback_id=feedback_id)
    )


@router.callback_query(F.data.startswith("Прийняти"))
@router.callback_query(F.data.startswith("Відхилити"))
async def accept_or_reject_feedback(query: types.CallbackQuery):
    feedback_id = query.data[-8:]
    chose = query.data[:-8]
    db = await Database.setup()

    feedback = await db.get_feedback(feedback_id=feedback_id)

    text_to_admin = (
        f"🗳 Відгук: {feedback_id}\n"
        f"➡️ Від: {feedback[1]}\n"
        f"🎛 Тип: {feedback[2]}\n"
        f"  ╰ {feedback[3] + '\n' if feedback[3] is not None else ''}"
        f"📊 Відгук: {feedback[4]}\n"
        f"🕙 Дата надсилання: {time.strftime("%D %H:%M", time.localtime(feedback[5]))}\n"
        f"⭐️ Оцінка: {feedback[6]}\n"
        f"🧑🏿‍💻 Статус: {'Прийнято ✅' if chose == 'Прийняти ✅' else 'Відхилено 🚫'}\n"
    )

    await query.message.edit_text(text=text_to_admin, reply_markup=None)

    if chose == "Прийняти ✅":
        await db.update_feedback_status(feedback_id=feedback_id, status=1)
    elif chose == "Відхилити 🚫":
        await db.update_feedback_status(feedback_id=feedback_id, status=2)


@router.message(F.text == "⬅️ Назад ↩️")
async def cmd_start(message: types.Message):
    await message.answer(text="Головне меню:", reply_markup=menu())
