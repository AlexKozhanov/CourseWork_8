# flake8: noqa
from django.core.management import BaseCommand

from habits.models import Habit
from users.models import User

# Указываем московское время
Time = [
    "13:01:00",
    "13:12:00",
    "13:13:00",
    "13:14:00",
    "13:15:00"]


class Command(BaseCommand):
    """
    Команда для наполнения БД привычками в перерыве.
    """
    def handle(self, *args, **options):
        user = User.objects.get(id=2)
        habit1 = Habit.objects.get_or_create(
            owner=user,
            habit="Смотреть YouTube Shorts",
            place_of_execution="комнате",
            time_execution=Time[3],
            periodicity=1,
            time_to_complete="00:00:30",
            sign_of_a_pleasant_habit=True,  # True - приятная привычка; False - полезная привычка
            # related_habit или reward
            # related_habit="",
            # reward="Шоколадка"
        )
        habit1 = Habit.objects.get(habit="Смотреть YouTube Shorts")
        habit2 = Habit.objects.get_or_create(
            owner=user,
            habit="Смотреть Pinterest",
            place_of_execution="спальне",
            time_execution=Time[4],
            periodicity=1,
            time_to_complete="00:01:20",
            sign_of_a_pleasant_habit=True,  # True - приятная привычка; False - полезная привычка
            # related_habit или reward
            # related_habit="",
            # reward="шоколадка"
        )
        habit2 = Habit.objects.get(habit="Смотреть Pinterest")
        habit3 = Habit.objects.get_or_create(
            owner=user,
            habit="Делать перерыв на 30-секунд",
            place_of_execution="комнате",
            time_execution=Time[0],
            periodicity=1,
            time_to_complete="00:00:30",
            sign_of_a_pleasant_habit=False,  # True - приятная привычка; False - полезная привычка
            # related_habit или reward
            # related_habit="",
            reward="Шоколадка"
        )
        habit4 = Habit.objects.get_or_create(
            owner=user,
            habit="Проходить урок DuoLingo",
            place_of_execution="спальне",
            time_execution=Time[1],
            periodicity=1,
            time_to_complete="00:01:20",
            sign_of_a_pleasant_habit=False,  # True - приятная привычка; False - полезная привычка
            # related_habit или reward
            related_habit=habit1,
            # reward="шоколадка"
        )
        habit5 = Habit.objects.get_or_create(
            owner=user,
            habit="Читать статью",
            place_of_execution="комнате",
            time_execution=Time[2],
            periodicity=1,
            time_to_complete="00:01:00",
            sign_of_a_pleasant_habit=False,  # True - приятная привычка; False - полезная привычка
            # related_habit или reward
            related_habit=habit2,
            # reward="шоколадка"
        )
