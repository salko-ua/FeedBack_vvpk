from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
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


def teacher() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Руслан Цаль-Цалько",
        "Андрій Назаров",
        "Богдан Ващук",
        "Назад <-",
        "Далі ->",
        "Сховати ❌",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


def dryga_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Педагогіка",
        "Архітектура",
        "Історія",
        "Математика",
        "Фізика",
        "Назад <-",
        "Далі->",
        "Сховати ❌",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


async def get_feedback_by_selection(
    selection: str, count: int
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    db = await Database.setup()
    all_feedback = await db.get_feedback_by_selection(selection, count)
    print(all_feedback)
    next_feedback = await db.get_feedback_by_selection(selection, count + 1)
    print(next_feedback)
    sizes = [1] * len(all_feedback) + [2] + [1]
    print(sizes)

    for button in all_feedback:
        button_text = f"{button[1][:10]}..."
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
