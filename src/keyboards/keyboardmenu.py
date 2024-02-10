from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


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


def feedback_choise() -> ReplyKeyboardMarkup:
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


def teacher() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Руслан Цаль-Цалько",
        "Андрій Назаров",
        "Богдан Ващук",
        "Відмінити❌",
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
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


def trety_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Пропозиції",
        "Скарги",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)
