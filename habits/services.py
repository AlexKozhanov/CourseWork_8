import json
from config.settings import TELEGRAM_BOT_ID
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from habits.models import Habit


# def send_telegram_message(message, chat_id):
#     """
#     Отправка сообщения в TG.
#     """
#     params = {
#         "text": message,
#         "chat_id": chat_id
#     }
#     requests.get(
#         f"https://api.telegram.org/bot{TELEGRAM_BOT_ID}/sendMessage",
#         params=params
#     )


def create_task(schedule: CrontabSchedule, habit: Habit) -> None:
    """Creates period task to send reminders."""
    PeriodicTask.objects.create(
        crontab=schedule,
        name=f"Sending reminder {habit.pk}",
        task="habits.tasks.send_message",
        args=json.dumps([habit.pk]),
    )
