from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.
class User(AbstractUser):
   
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

class Habit(models.Model):
    name = models.CharField(max_length=50, null=True)
    goal = models.IntegerField(null=True)
    units = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    def __str__(self):
        return f'<Habit name={self.name}>'  

class DailyRecord(models.Model):
    quantity = models.IntegerField(null=True)
    date = models.DateField(default=timezone.now, null=True)
    habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    def __str__(self):
        return f'<DailyRecord habit={self.habit_id}>'  

