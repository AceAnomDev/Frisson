# 🎸 Frisson Guitar Bot

<p align="center">
  <img src="assets/avatar.jpg" width="180" alt="Frisson Bot Avatar" />
</p>

<p align="center">
  <a href="https://t.me/musical_guitar_bot">
    <img src="https://img.shields.io/badge/Telegram-Открыть%20бота-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Open in Telegram"/>
  </a>
</p>

Telegram-бот онлайн-школы гитары **«Фриссон»** — помогает потенциальным ученикам выбрать преподавателя и записаться на занятия.

---

## Структура проекта

```
frisson-guitar-bot/
├── assets/                    # Фотографии преподавателей
│
├── bot/
│   ├── data/
│   │   └── teachers.py        # Данные о преподавателях и инструментах
│   ├── handlers/
│   │   ├── __init__.py        # Регистрация всех хендлеров
│   │   ├── start.py           # /start, join, no
│   │   ├── teachers.py        # Листание преподавателей (FSM)
│   │   ├── enrollment.py      # Оценка бота (enroll, rate_N)
│   │   ├── feedback.py        # /feedback (FSM)
│   │   └── commands.py        # /help, /musical
│   ├── keyboards/
│   │   └── inline.py          # Все inline-клавиатуры
│   ├── middlewares/
│   │   └── logging.py         # Логирование входящих апдейтов
│   └── states/
│       └── user.py            # FSM-состояния (TeacherBrowse, FeedbackForm)
│
├── config.py                  # Загрузка переменных окружения
├── main.py                    # Точка входа
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-org/frisson-guitar-bot.git
cd frisson-guitar-bot
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настроить переменные окружения

```bash
cp .env.example .env
# отредактируйте .env, заполнив все значения
```

| Переменная          | Описание                                    |
|---------------------|---------------------------------------------|
| `BOT_TOKEN`         | Токен бота от @BotFather                    |
| `ADMIN_ID`          | Telegram ID администратора (для оценок)     |
| `FEEDBACK_ADMIN_ID` | Telegram ID получателя текстовых отзывов    |
| `CHANNEL_ID`        | ID Telegram-канала школы                    |
| `MANAGER_LINK`      | Ссылка на менеджера (`https://t.me/...`)    |
| `CHANNEL_LINK`      | Ссылка на канал (`https://t.me/...`)        |

### 4. Добавить фото преподавателей

Поместите файлы в `assets/`.

### 5. Запустить бота

```bash
python main.py
```

---

## Команды бота

| Команда      | Описание                                          |
|--------------|---------------------------------------------------|
| `/start`     | Главное приветствие                               |
| `/musical`   | Выбор инструмента напрямую                        |
| `/feedback`  | Оставить текстовый отзыв о занятиях               |
| `/help`      | Информация о школе и контакты                     |

---

## Технологии

- **Python 3.11+**
- **aiogram 2.x** — асинхронный Telegram Bot API фреймворк
- **python-dotenv** — управление конфигурацией через `.env`
- **FSM (Finite State Machine)** — управление состоянием диалога
