import requests
from celery import shared_task
from habits.models import Habit
from habits.services import send_telegram_message
from config.settings import TELEGRAM_BOT_ID


@shared_task
def send_message_to_user():
    """
    Отправка о выполнение привычки.
    """
    habits = Habit.objects.filter(sign_of_a_pleasant_habit=False)
    for habit in habits:
        habit.send_indicator -= 1
        if not habit.send_indicator:
            if habit.owner.tg_chat_id:
                message = f"У вас сегодня выполнение привычки: {habit.habit}, " \
                          f"которую нужно выполнить в {habit.time_execution} " \
                          f"в {habit.place_of_execution}"
                send_telegram_message(
                    message=message,
                    chat_id=habit.owner.tg_chat_id)
                habit.send_indicator = habit.periodicity
        habit.save(update_fields=["send_indicator"])


@shared_task
def send_message(pk) -> None:
    """Sends reminders to user's telegram."""
    habit = Habit.objects.get(pk=pk)
    text = (
        f"It's time to do {habit.action} at {habit.place}! "
        f"Don't forget to {habit.reward if habit.reward else habit.related_habit} afterwards."
    )
    params = {
        "text": text,
        "chat_id": habit.user.tg_chat_id,
    }
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_ID}/sendMessage", params=params)
