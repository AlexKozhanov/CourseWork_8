from datetime import timedelta
from django.core.validators import MaxValueValidator
from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    """
    Модель привычки.
    """
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        related_name="users_habits",
        **NULLABLE)
    habit = models.CharField(
        max_length=255,
        verbose_name="Привычка",
        help_text="Напиши что делаешь")
    place_of_execution = models.CharField(
        max_length=255,
        verbose_name="Место где нужно выполнять привычку",
        **NULLABLE,
        help_text="Напиши место")
    time_execution = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время",
        **NULLABLE,
        help_text="Время для выполнения привычки",)
    periodicity = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(7)],
        verbose_name="Периодичность",
        default=1,
        **NULLABLE,
        help_text="Укажите кол-во дней, за которые необходимо выполнить привычку (по умолчанию раз в день)",)
    time_to_complete = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Время на действие",
        **NULLABLE,
        help_text="время, которое предположительно потратит пользователь на выполнение привычки (по умолчанию 120сек)",)
    sign_of_a_pleasant_habit = models.BooleanField(
        verbose_name="Признак приятной привычки",
        default=False,
        **NULLABLE,
        help_text="True - приятная привычка; False - полезная привычка (по умолчанию False)")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Связанная приятная привычка",
        **NULLABLE,
        related_name="related_habits",
        help_text="привычка, которую выполняем после полезной привычки (не может быть полезной и иметь вознаграждение)")
    reward = models.CharField(
        verbose_name="Вознаграждение",
        **NULLABLE,
        help_text="чем пользователь должен себя вознаградить после выполнения (какой-то объект)")

    STATUS_PUBLISHED = [
        ("Опубликован", "Опубликован"),
        ("Не опубликован", "Не опубликован"),
    ]
    published = models.CharField(
        max_length=50,
        choices=STATUS_PUBLISHED,
        default="Не опубликован",
        **NULLABLE,
        verbose_name="Статус опубликования привычки (по умолчанию Не опубликован)",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)

    def __str__(self):
        return self.habit
