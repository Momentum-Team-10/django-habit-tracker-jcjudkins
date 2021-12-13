# accounts/forms.py
from django import forms
from .models import Habit, User, DailyRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            "name",
            "goal",
            "units",
            "created_at",
            "user_id",
        ]
        
class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = [
            "quantity",
            "date",
            "habit_id",
        ]


# may need a user form