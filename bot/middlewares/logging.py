import logging
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    """Log every incoming update for observability."""

    async def on_pre_process_message(self, message: types.Message, data: dict) -> None:
        logger.info(
            "MSG  user=%s(%s) text=%r",
            message.from_user.id,
            message.from_user.username,
            message.text,
        )

    async def on_pre_process_callback_query(
        self, callback: types.CallbackQuery, data: dict
    ) -> None:
        logger.info(
            "CB   user=%s(%s) data=%r",
            callback.from_user.id,
            callback.from_user.username,
            callback.data,
        )
