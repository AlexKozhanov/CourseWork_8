from django.core.management import BaseCommand

from habits.models import Habit
from users.models import User

Time = [
    "17:00:00",
    "17:01:00",
    "17:02:00",
    "17:03:00",
    "17:04:00",
    "17:05:00"]

class Command(BaseCommand):
    """
    Команда для наполнения БД привычками в перерыве.
    """
    def handle(self, *args, **options):
        user = User.objects.get(id=2)
        habit1 = Habit.objects.get_or_create(
            owner=user,
            habit="перерыв на 5-минут",
            place_of_execution="комнате",
            time_execution=Time[0],
            periodicity=1,
            time_to_complete="00:01:00",
            reward= "шоколадка",
            published= "Опубликован",
        )
        habit2 = Habit.objects.get_or_create(
            owner=user,
            habit="Крутить головой",
            place_of_execution="комнате",
            time_execution=Time[1],
            periodicity=1,
            time_to_complete="00:01:00",
            reward="шоколадка",
            published="Опубликован",
        )
        habit3 = Habit.objects.get_or_create(
            owner=user,
            habit="Крутить руками",
            place_of_execution="комнате",
            time_execution=Time[2],
            periodicity=1,
            time_to_complete="00:01:00",
            reward="шоколадка",
            published="Опубликован",
        )
        habit4 = Habit.objects.get_or_create(
            owner=user,
            habit="Крутить ногами",
            place_of_execution="комнате",
            time_execution=Time[3],
            periodicity=1,
            time_to_complete="00:01:00",
            reward="шоколадка",
            published="Опубликован",
        )
        habit5 = Habit.objects.get_or_create(
            owner=user,
            habit="Крутить телом",
            place_of_execution="комнате",
            time_execution=Time[4],
            periodicity=1,
            time_to_complete="00:01:00",
            reward="шоколадка",
            published="Опубликован",
        )
        habit6 = Habit.objects.get_or_create(
            owner=user,
            habit="Продолжать работу",
            place_of_execution="где-то",
            time_execution=Time[5],
            periodicity=1,
            time_to_complete="00:01:00",
            reward="шоколадка",
            published="Опубликован",
        )