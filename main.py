import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from bot.handlers import register_all_handlers
from bot.middlewares import LoggingMiddleware
from config import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def create_bot() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=config.bot_token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=MemoryStorage())
    dp.middleware.setup(LoggingMiddleware())
    register_all_handlers(dp)
    return bot, dp


if __name__ == "__main__":
    bot, dp = create_bot()
    logging.info("Bot is starting…")
    executor.start_polling(dp, skip_updates=True)
