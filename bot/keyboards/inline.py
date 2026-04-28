from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import config


def instrument_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("Акустическая 🎸", callback_data="Акустическая гитара"),
        InlineKeyboardButton("Электрогитара 🎸", callback_data="Электрогитара"),
        InlineKeyboardButton("Укулеле 🎸",       callback_data="Укулеле"),
    )
    return kb


def welcome_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Да ✅",  callback_data="join"),
        InlineKeyboardButton("Нет ❌", callback_data="no"),
    )
    return kb


def teacher_nav_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔙 Назад",       callback_data="back"),
        InlineKeyboardButton("➡️ Следующий",   callback_data="next"),
        InlineKeyboardButton("Выбрать ✅",      callback_data="agree"),
    )
    return kb


def after_choice_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🎯 Записаться",    url=config.manager_link),
        InlineKeyboardButton("🤔 Подумаю",       callback_data="think"),
        InlineKeyboardButton("⭐️ Оценить бота", callback_data="enroll"),
        InlineKeyboardButton("📢 Telegram-канал", url=config.channel_link),
        InlineKeyboardButton("🔙 Назад",         callback_data="back"),
    )
    return kb


def rating_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=5)
    kb.add(*[
        InlineKeyboardButton(f"⭐️{i}", callback_data=f"rate_{i}")
        for i in range(1, 6)
    ])
    return kb
