from aiogram import types

from bot.keyboards.inline import instrument_keyboard
from config import config

HELP_TEXT = (
    "📚 Добро пожаловать в онлайн-школу гитары «Фриссон»!\n\n"
    "🚀 Мы предлагаем:\n"
    "— Индивидуальные занятия 🎈\n"
    "— Уроки по акустической гитаре, электрогитаре и укулеле 🎸\n"
    "— Персональный подход и поддержку преподавателей ❤️\n\n"
    "Нажмите «Выбрать ✅», чтобы выбрать преподавателя и записаться.\n\n"
    "💰 Стоимость уточняйте у менеджера: {manager}\n\n"
    "❓ Вопросы — в нашем канале: {channel}\n"
)


async def cmd_help(message: types.Message) -> None:
    await message.answer(
        HELP_TEXT.format(manager=config.manager_link, channel=config.channel_link)
    )


async def cmd_musical(message: types.Message) -> None:
    await message.answer("Выберите инструмент 🎸:", reply_markup=instrument_keyboard())


def register_command_handlers(dp) -> None:
    dp.register_message_handler(cmd_help,    commands=["help"])
    dp.register_message_handler(cmd_musical, commands=["musical"])
