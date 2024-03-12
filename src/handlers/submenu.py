from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.keyboards import menu, trety_keyboard, dryga_keyboard, teacher
from src.data_base import Database

router = Router()


class FSMFeedBack(StatesGroup):
    chose_name_selection = State()
    write_feedback = State()


@router.message(F.text == "🏫 Коледж 🔔")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(text="Виберіть варіант:", reply_markup=trety_keyboard())
    await state.update_data(selection="collage")
    await state.update_data(selection_name=None)
    await state.set_state(FSMFeedBack.write_feedback)


@router.message(F.text == "📚 Предмети 📚")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(text="Виберіть предмет:", reply_markup=dryga_keyboard())
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
    teacher_name = query.data[8:]
    print(teacher_name)
    await state.update_data(selection_name=query.data)
    await query.message.answer(f"Напишіть відгук: ")
    await state.set_state(FSMFeedBack.write_feedback)


@router.message(F.text, FSMFeedBack.write_feedback)
async def add_feedback2(message: types.Message, state: FSMContext):
    db = await Database.setup()
    data = await state.get_data()

    await db.add_feedback(
        user_id=message.from_user.id,
        selection=data["selection"],
        selection_object=data["selection_name"],
        feedback=message.text,
        data_sending=10000,
        stars="⭐⭐⭐⭐⭐",
    )


@router.message(F.text == "⬅️ Назад ↩️")
async def cmd_start(message: types.Message):
    await message.answer(text="Головне меню:", reply_markup=menu())
