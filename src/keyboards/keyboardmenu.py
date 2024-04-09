from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from typing import Literal
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from src.data_base import Database


def menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = [
        "📝 Додати відгук 📒",
        "😱 Переглянути відгук 😱",
        "📋 Про бота 📋",
        "📈 Статистика 📉",
    ]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


def feedback_choose() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = [
        "👨‍🏫 Викладачі 👩‍🏫",
        "📚 Предмети 📚",
        "⬅️ Назад ↩️",
        "🏫 Коледж 🔔",
    ]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


def feedback_review_choose() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="👨‍🏫 Викладачі 👩‍🏫", callback_data="teacher"
        )
    )
    builder.add(
        InlineKeyboardButton(text="📚 Предмети 📚", callback_data="subject")
    )
    builder.add(
        InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌")
    )
    builder.add(
        InlineKeyboardButton(text="🏫 Коледж 🔔", callback_data="college")
    )

    return builder.adjust(2).as_markup(resize_keyboard=True)


async def get_keyboard_by_type(
    types: Literal["subject", "teacher"],
    page: int,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    db = await Database.setup()
    all_names_by_type = await db.get_all_names_by_type(types, page)
    print(all_names_by_type)
    next_names_by_type = await db.get_all_names_by_type(types, page + 1)
    print(next_names_by_type)
    sizes = [1] * len(all_names_by_type) + [2] + [1]

    for button in all_names_by_type:
        builder.add(
            InlineKeyboardButton(text=button[0], callback_data=button[0])
        )

    if page != 1:
        builder.add(
            InlineKeyboardButton(
                text="⬅️ Назад", callback_data="⬅️ Назад 1 " + types
            )
        )
    if len(next_names_by_type) > 0:
        builder.add(
            InlineKeyboardButton(
                text="Вперед ➡️", callback_data="Вперед ➡️ 1 " + types
            )
        )

    builder.add(
        InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌")
    )

    return builder.adjust(*sizes).as_markup(resize_keyboard=True)


async def get_feedback_by_selection(
    selection: str, count: int
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    db = await Database.setup()
    all_feedback = await db.get_feedback_by_selection(selection, count)
    next_feedback = await db.get_feedback_by_selection(selection, count + 1)
    sizes = [1] * len(all_feedback) + [2] + [1]

    for button in all_feedback:
        button_text = f"{button[1].split('\n', 1)[0]}"
        builder.add(
            InlineKeyboardButton(
                text=button_text, callback_data="SEE FEEDBACK " + button[0]
            )
        )

    if count != 1:
        builder.add(
            InlineKeyboardButton(
                text="⬅️ Назад", callback_data="⬅️ Назад " + selection
            )
        )
    if len(next_feedback) > 0:
        builder.add(
            InlineKeyboardButton(
                text="Вперед ➡️", callback_data="Вперед ➡️ " + selection
            )
        )

    builder.add(
        InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌")
    )

    return builder.adjust(*sizes).as_markup(resize_keyboard=True)


async def back_by_selection(selection: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data=selection))
    builder.add(
        InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌")
    )

    return builder.adjust().as_markup(resize_keyboard=True)
