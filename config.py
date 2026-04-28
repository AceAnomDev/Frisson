import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    bot_token: str
    admin_id: str
    feedback_admin_id: str
    channel_id: str
    manager_link: str
    channel_link: str

    @classmethod
    def from_env(cls) -> "Config":
        required = {
            "BOT_TOKEN": os.getenv("BOT_TOKEN"),
            "ADMIN_ID": os.getenv("ADMIN_ID"),
            "FEEDBACK_ADMIN_ID": os.getenv("FEEDBACK_ADMIN_ID"),
            "CHANNEL_ID": os.getenv("CHANNEL_ID"),
            "MANAGER_LINK": os.getenv("MANAGER_LINK"),
            "CHANNEL_LINK": os.getenv("CHANNEL_LINK"),
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise EnvironmentError(f"Missing required env vars: {', '.join(missing)}")

        return cls(
            bot_token=required["BOT_TOKEN"],
            admin_id=required["ADMIN_ID"],
            feedback_admin_id=required["FEEDBACK_ADMIN_ID"],
            channel_id=required["CHANNEL_ID"],
            manager_link=required["MANAGER_LINK"],
            channel_link=required["CHANNEL_LINK"],
        )


config = Config.from_env()
