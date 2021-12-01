from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

class Habit(models.Model):
    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    units = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def __str__(self):
        return f'<Habit name={self.name}>'  

class DailyRecord(models.Model):
    quantity = models.IntegerField()
    date = models.DateField()
    habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def __str__(self):
        return f'<DailyRecord habit={self.habit_id}>'  
