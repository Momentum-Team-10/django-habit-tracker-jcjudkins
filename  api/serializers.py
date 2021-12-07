from rest_framework import serializers
from habittracker.models import Habit


# need to import fields from habit model
class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'name',
            'goal',
            'units',
        )