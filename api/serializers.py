from rest_framework import serializers
from habittracker.models import DailyRecord, Habit


# need to import fields from habit model
class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Habit
        fields = (
            'pk',
            'name',
            'goal',
            'units',
        )

class RecordSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = DailyRecord
        fields = (
            'pk',
            'quantity',
            'date',
        )