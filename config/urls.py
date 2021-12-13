"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import debug_toolbar
from django.urls import include, path
from habittracker import views
from api import views as api_views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.index, name='index'),
    path('habittracker/add', views.add_habit, name='add_habit'),
    path('habittracker/<int:pk>/edit', views.add_habit, name='edit_habit'),
    path('habit_view/<int:pk>', views.habit_detail, name='habit_detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/habits', api_views.HabitListView.as_view(), name='habit_list'),
    path('api/habits/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit_detail')

]
