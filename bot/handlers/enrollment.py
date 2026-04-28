from aiogram import types

from bot.keyboards.inline import rating_keyboard
from config import config

FINAL_TEXT = (
    "Спасибо за вашу оценку! ❤️\n\n"
    "До встречи на занятиях! 🎊\n\n"
    f"Переходите на наш Telegram-канал: {config.channel_link}\n"
    f"Запишитесь на первый бесплатный урок у нашего менеджера: {config.manager_link}"
)


async def cb_enroll(callback: types.CallbackQuery) -> None:
    await callback.message.edit_caption(
        caption="Спасибо за выбор! 🙌\n\nПожалуйста, оцените работу бота:",
        reply_markup=rating_keyboard(),
    )


async def cb_rate(callback: types.CallbackQuery) -> None:
    rating_value = callback.data.split("_")[1]
    user = callback.from_user

    await callback.bot.send_message(
        config.admin_id,
        f"🎸 Новый отзыв!\n\n"
        f"👤 Имя: {user.first_name} (@{user.username})\n"
        f"🆔 ID: {user.id}\n"
        f"⭐️ Оценка: {rating_value}/5",
    )

    await callback.message.edit_caption(caption=FINAL_TEXT)


def register_enrollment_handlers(dp) -> None:
    dp.register_callback_query_handler(cb_enroll, lambda c: c.data == "enroll")
    dp.register_callback_query_handler(
        cb_rate, lambda c: c.data.startswith("rate_")
    )
