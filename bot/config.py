import os
from dotenv import load_dotenv


def get_token_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return os.environ.get("BOT_TOKEN")


BOT_TOKEN = get_token_env()

