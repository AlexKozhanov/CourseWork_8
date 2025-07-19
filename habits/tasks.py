import os
from datetime import datetime, timedelta
from celery import shared_task

from users.models import User
from habits.models import Habit
from habits.services import send_telegram_message
from config.settings import CHAT_ID

@shared_task
def send_message_to_user():
    """
    Отправка всех привычек.
    """
    habits = Habit.objects.filter(sign_of_a_pleasant_habit=False)
    for habit in habits:
        if habit.owner.tg_chat_id:
            message = f"У вас сегодня выполнение привычки: {habit.habit}, " \
                      f"которую нужно выполнить в {habit.time_execution} " \
                      f"в {habit.place_of_execution}"
            send_telegram_message(
                chat_id=habit.owner.tg_chat_id,
                message=message,)
            print("Сообщение отправлено send_message_to_user")
        else: print("Я ничего не нашел send_message_to_user")


@shared_task
def send_reminder():
    """
    Отправляет напоминания пользователям о привычках в назначенное время.
    time_execution - Время для выполнения привычки
    """
    now = datetime.now()  # текущее время ПК
    time_threshold = now - timedelta(seconds=40)  # время ПК минус 40 сек

    habits_to_remind = Habit.objects.filter(time_execution__lte=now.time(), time_execution__gte=time_threshold.time())
    user = User.objects.get(id=2)

    for habit in habits_to_remind:
        chat_id = user.tg_chat_id
        message = f"Я буду {habit.habit} в {habit.time_execution} в {habit.place_of_execution}"
        if chat_id:
            send_telegram_message(chat_id, message)
            print("Сообщение отправлено send_reminder")
        else: print("Я ничего не нашел send_reminder")


@shared_task
def send_work():
    chat_id = CHAT_ID
    # chat_id = 5059260529
    message = "Я работаю"
    send_telegram_message(chat_id, message)
    print("Сообщение отправлено send_work")

