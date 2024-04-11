import asyncio
import logging
import sentry_sdk
from aiogram import Bot, Dispatcher
from src.config import TOKEN
from src.handlers import comands, menu, submenu, view_feedback

sentry_sdk.init(
    dsn="https://1f24e84f56b3239868ebb5e3bd3411ef@o4504669478780928.ingest.us.sentry.io/4507069466673152",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

async def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(submenu.router)
    dp.include_router(comands.router)
    dp.include_router(view_feedback.router)
    dp.include_router(menu.router)


async def start_bot() -> None:
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()

    await register_handlers(dispatcher)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())
