from rest_framework import serializers
from habittracker.models import DailyRecord, Habit, User


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


# Including this class. Not sure if this will be used
class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'groups',
            )