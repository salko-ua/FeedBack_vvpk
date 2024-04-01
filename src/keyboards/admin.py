from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def accept_reject_feedback(feedback_id: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = ["Прийняти ✅", "Відхилити 🚫"]

    for button in keyboard:
        builder.add(
            InlineKeyboardButton(
                text=button, callback_data=button + feedback_id
            )
        )

    return builder.adjust(2).as_markup(resize_keyboard=True)
