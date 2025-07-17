import requests

from config.settings import TELEGRAM_URL, TELEGRAM_BOT_ID


def send_telegram_message(message, chat_id):
    """
    Отправка сообщения в TG.
    """
    params = {
        "text": message,
        "chat_id": chat_id
    }
    requests.get(
        f"{TELEGRAM_URL}{TELEGRAM_BOT_ID}/sendMessage", params=params
    )
