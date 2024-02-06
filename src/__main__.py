
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

bot = Bot(token="")
dp = Dispatcher()


def start_all_kb() -> ReplyKeyboardMarkup:
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


@dp.message(F.text == "🏫 Коледж 🔔")
async def cmd_start(message: types.Message):
    await message.answer(text="Виберіть варіант:", reply_markup=trety_keyboard())


@dp.message(F.text == "📚 Предмети 📚")
async def cmd_start(message: types.Message):
    await message.answer(text="Виберіть предмет:", reply_markup=dryga_keyboard())


@dp.message(F.text == "📝 Додати відгук 📒")
async def cmd_start(message: types.Message):
    await message.answer(text="Куди ви хочете додати?", reply_markup=feedback_choise())


@dp.message(F.text == "😱 Переглянути відгук 😱")
async def cmd_start(message: types.Message):
    await message.answer(text="Куди ви хочете додати?", reply_markup=feedback_choise())


@dp.message(F.text == "👨‍🏫 Викладачі 👩‍🏫")
async def cmd_start(message: types.Message):
    await message.answer(text="Виберіть викладача", reply_markup=teacher())


@dp.message(F.text == "📋 Про бота 📋")
async def cmd_start(message: types.Message):
    await message.answer(text="Інформаці про бота:")


@dp.message(F.text == "📈 Статистика 📉")
async def cmd_start(message: types.Message):
    await message.answer(text="Статистика:")


@dp.message(F.text == "⬅️ Назад ↩️")
async def cmd_start(message: types.Message):
    await message.answer(text="Головне меню:", reply_markup=start_all_kb())


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text="Доброго дня!", reply_markup=start_all_kb())


async def main():
    print("Bot Online")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
