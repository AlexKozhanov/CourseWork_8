from datetime import datetime, timedelta
from celery import shared_task

from users.models import User
from habits.models import Habit
from habits.services import send_telegram_message


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
def send_reminder():
    """
    Отправляет напоминания пользователям о привычках в назначенное время.
    time_execution - Время для выполнения привычки
    """

    now = datetime.now()
    time_threshold = now - timedelta(seconds=40)

    habits_to_remind = Habit.objects.filter(
        time_execution__lte=now.time(),
        time_execution__gte=time_threshold.time()
    )

    # users = User.objects.all()
    # for user in users: pass

    for habit in habits_to_remind:
        chat_id = User.tg_chat_id
        if chat_id:
            message = f"Я буду {habit.habit} в {habit.time_execution} в {habit.place_of_execution}"
            send_telegram_message(chat_id, message)
            print("Сообщение отправлено")

    chat_id = 5059260529
    message = f"Я работаю"
    send_telegram_message(message, chat_id)
