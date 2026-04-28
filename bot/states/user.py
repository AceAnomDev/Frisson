from aiogram.dispatcher.filters.state import State, StatesGroup


class TeacherBrowse(StatesGroup):
    """User is browsing teachers for a chosen instrument."""
    browsing = State()


class FeedbackForm(StatesGroup):
    """User is composing a text feedback message."""
    waiting_for_text = State()
