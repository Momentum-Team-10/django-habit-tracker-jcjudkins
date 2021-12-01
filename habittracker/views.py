from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord, User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect("auth_login")
    habits = Habits.objects.all()

    template_name = "templates/core/index.html"

    return render(request, template_name, {"habits": habits})
    
