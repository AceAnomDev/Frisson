# 🎸 Frisson Guitar Bot

<p align="center">
  <img src="assets/images/avatar.jpg" width="180" alt="Frisson Bot Avatar" />
</p>

<p align="center">
  <a href="https://t.me/musical_guitar_bot">
    <img src="https://img.shields.io/badge/Telegram-Open%20Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Open in Telegram"/>
  </a>
</p>

Telegram bot for the **Frisson** online guitar school — helps prospective students choose a teacher and sign up for lessons.

---

## Project structure

```
frisson-guitar-bot/
├── assets/                    # Teacher photos
│
├── bot/
│   ├── data/
│   │   └── teachers.py        # Teacher and instrument data
│   ├── handlers/
│   │   ├── __init__.py        # Handler registration
│   │   ├── start.py           # /start, join, no
│   │   ├── teachers.py        # Teacher browsing (FSM)
│   │   ├── enrollment.py      # Bot rating (enroll, rate_N)
│   │   ├── feedback.py        # /feedback (FSM)
│   │   └── commands.py        # /help, /musical
│   ├── keyboards/
│   │   └── inline.py          # All inline keyboards
│   ├── middlewares/
│   │   └── logging.py         # Incoming update logging
│   └── states/
│       └── user.py            # FSM states (TeacherBrowse, FeedbackForm)
│
├── config.py                  # Environment variable loader
├── main.py                    # Entry point
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/your-org/frisson-guitar-bot.git
cd frisson-guitar-bot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
# edit .env and fill in all values
```

| Variable            | Description                                      |
|---------------------|--------------------------------------------------|
| `BOT_TOKEN`         | Bot token from @BotFather                        |
| `ADMIN_ID`          | Telegram ID of the admin (receives ratings)      |
| `FEEDBACK_ADMIN_ID` | Telegram ID of the feedback recipient            |
| `CHANNEL_ID`        | School's Telegram channel ID                     |
| `MANAGER_LINK`      | Link to the manager (`https://t.me/...`)         |
| `CHANNEL_LINK`      | Link to the channel (`https://t.me/...`)         |

### 4. Add teacher photos

Place image files in `assets/`.

### 5. Run the bot

```bash
python main.py
```

---

## Bot commands

| Command      | Description                                      |
|--------------|--------------------------------------------------|
| `/start`     | Main welcome message                             |
| `/musical`   | Go straight to instrument selection              |
| `/feedback`  | Leave a text review about lessons                |
| `/help`      | School info and contacts                         |

---

## Tech stack

- **Python 3.11+**
- **aiogram 2.x** — async Telegram Bot API framework
- **python-dotenv** — configuration management via `.env`
- **FSM (Finite State Machine)** — dialog state management
