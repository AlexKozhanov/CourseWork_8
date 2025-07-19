import requests
from config.settings import TELEGRAM_URL, TELEGRAM_BOT_ID


def send_telegram_message(chat_id, message):
    """
    Отправь сообщение в TG.
    :param chat_id: id .
    :param message: текст сообщения.
    """
    params = {
        "text": message,
        "chat_id": chat_id
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_BOT_ID}/sendMessage", params=params)
