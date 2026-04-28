from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto

from bot.data.teachers import TEACHERS, INSTRUMENT_TEACHERS
from bot.keyboards.inline import teacher_nav_keyboard, after_choice_keyboard
from bot.states.user import TeacherBrowse


# ── helpers ────────────────────────────────────────────────────────────────────

async def _send_teacher(bot: Bot, chat_id: int, state: FSMContext, new: bool) -> None:
    async with state.proxy() as data:
        teachers = INSTRUMENT_TEACHERS[data["instrument"]]
        name = teachers[data["index"]]
        data["teacher_name"] = name
        teacher = TEACHERS[name]
        keyboard = teacher_nav_keyboard()

        if new:
            msg = await bot.send_photo(
                chat_id,
                photo=open(teacher.photo, "rb"),
                caption=teacher.description,
                reply_markup=keyboard,
            )
            data["message_id"] = msg.message_id
        else:
            await bot.edit_message_media(
                media=InputMediaPhoto(
                    media=open(teacher.photo, "rb"),
                    caption=teacher.description,
                ),
                chat_id=chat_id,
                message_id=data["message_id"],
                reply_markup=keyboard,
            )


# ── handlers ───────────────────────────────────────────────────────────────────

async def cb_choose_instrument(callback: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["instrument"] = callback.data
        data["index"] = 0

    await TeacherBrowse.browsing.set()
    await _send_teacher(callback.bot, callback.from_user.id, state, new=True)


async def cb_navigate(callback: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        teachers = INSTRUMENT_TEACHERS[data["instrument"]]
        delta = 1 if callback.data == "next" else -1
        data["index"] = (data["index"] + delta) % len(teachers)

    await _send_teacher(callback.bot, callback.from_user.id, state, new=False)


async def cb_agree(callback: types.CallbackQuery) -> None:
    await callback.message.edit_caption(
        caption="👍 Отлично! Вы выбрали преподавателя\n\nЧто бы вы хотели сделать дальше? 👁️",
        reply_markup=after_choice_keyboard(),
    )


async def cb_think(callback: types.CallbackQuery) -> None:
    await callback.message.edit_caption(
        caption="🤔 Хорошо!\n\nБудем ждать вас в школе «Фриссон» 💛"
    )


def register_teacher_handlers(dp) -> None:
    dp.register_callback_query_handler(
        cb_choose_instrument,
        lambda c: c.data in INSTRUMENT_TEACHERS,
    )
    dp.register_callback_query_handler(
        cb_navigate,
        lambda c: c.data in ("next", "back"),
        state=TeacherBrowse.browsing,
    )
    dp.register_callback_query_handler(cb_agree,  lambda c: c.data == "agree")
    dp.register_callback_query_handler(cb_think,  lambda c: c.data == "think")
