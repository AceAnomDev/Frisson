from aiogram import types
from bot.keyboards.inline import welcome_keyboard, instrument_keyboard


WELCOME_TEXT = (
    "👋 Приветствуем вас в онлайн-школе гитары «Фриссон»! 😃\n\n"
    "Мы точно знаем, как тебе помочь, если ты:\n\n"
    "💫 Не знаешь с чего начать играть и как прийти к желанному уровню\n"
    "💫 Не звучат аккорды\n"
    "💫 Никак не дается проклятое баррэ\n"
    "💫 Хочешь играть свои любимые песни и самостоятельно разбирать их\n"
    "💫 Не получается петь под гитару\n\n"
    "Благодаря нашей методике обучения уже 300+ учеников играют свои любимые песни 🎶\n\n"
    "🎸 Независимо от вашего уровня — с нуля, новичок или продвинутый гитарист — "
    "мы поможем вам раскрыть свой музыкальный потенциал 📈💡\n\n"
    "🤘 В нашей школе вас ждёт:\n\n"
    "✅ Индивидуальные и групповые занятия\n"
    "✅ Персонализированные уроки под ваши цели и темп обучения\n"
    "✅ Профессиональные преподаватели\n"
    "✅ Удобный формат — занимайтесь в любое время и в любом месте\n"
    "✅ Поддержка дружного сообщества гитаристов\n\n"
    "Посмотрите отзывы наших учеников — https://t.me/otzivifrisson\n\n"
    "Вы хотите начать обучение? 🙌"
)


async def cmd_start(message: types.Message) -> None:
    await message.answer(WELCOME_TEXT, reply_markup=welcome_keyboard())


async def cb_join(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(
        "Выберите инструмент 🎸:", reply_markup=instrument_keyboard()
    )


async def cb_no(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text("Будем рады видеть вас позже 😊")


def register_start_handlers(dp) -> None:
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_callback_query_handler(cb_join, lambda c: c.data == "join")
    dp.register_callback_query_handler(cb_no,  lambda c: c.data == "no")
