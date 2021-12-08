from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from habittracker.models import Habit
from .serializers import HabitSerializer


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer



class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
