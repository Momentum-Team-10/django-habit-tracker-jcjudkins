from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles


# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

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

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.username

    def __str__(self):
        return f'<Habit name={self.name}>'  

class DailyRecord(models.Model):
    quantity = models.IntegerField(null=True)
    date = models.DateField(default=timezone.now, null=True)
    habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.username

    def __str__(self):
        return f'<DailyRecord habit={self.habit_id}>'  

