from rest_framework import serializers
from habits.models import Habit
from habits.validators import (
    FieldFillingValidator,
    RelatedHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.
    """

    class Meta:
        model = Habit
        # exclude = ("send_indicator",)
        fields = "__all__"
        validators = [
            FieldFillingValidator(
                "reward",
                "related_habit",
                "sign_of_a_pleasant_habit"),
            RelatedHabitValidator("related_habit"),
        ]
