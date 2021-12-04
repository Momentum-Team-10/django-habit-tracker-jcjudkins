from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord, User
from .forms import (
    HabitForm,
    DailyRecordForm
)
# Create your views here.

# view for "homepage"


# list of users habits
def index(request):
    if not request.user.is_authenticated:
        return redirect("auth_login")
    else:
        habits = Habit.objects.all()
        return render(request, 'core/index.html', {'habits': habits})



# view for adding a new habit
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.author = request.user
            habit.save()
            return redirect('habit_detail', pk=habit.pk)
    else:
        form = HabitForm()

    return render(request, 'core/add_habit.html', {'form': form})


# view for edit habit 
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit.save()
            return redirect('index', pk=habit.pk)

    return render(request, 'core/edit_habit.html', {'form': form})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(
        request,
        'core/habit_detail.html',
        {'habit': habit}
)
    