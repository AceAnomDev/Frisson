from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.states.user import FeedbackForm
from config import config


async def cmd_feedback(message: types.Message) -> None:
    await FeedbackForm.waiting_for_text.set()
    await message.answer("Оставьте ваш отзыв 📝 о занятиях:")


async def handle_feedback_text(message: types.Message, state: FSMContext) -> None:
    user = message.from_user
    feedback = message.text

    await message.bot.send_message(
        config.feedback_admin_id,
        f"📝 Отзыв от {user.first_name} (@{user.username}, ID: {user.id}):\n\n{feedback}",
    )

    await message.answer("Спасибо за ваш отзыв! Мы ценим ваше мнение. 😊")
    await state.finish()


def register_feedback_handlers(dp) -> None:
    dp.register_message_handler(cmd_feedback, commands=["feedback"])
    dp.register_message_handler(
        handle_feedback_text, state=FeedbackForm.waiting_for_text
    )
