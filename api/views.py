from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.decorators import permission_classes
from habittracker.models import Habit
from .serializers import HabitSerializer

# Viewsets show views based on .models
# permission classes attribute sets who can access endpoint
class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer



class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


# class RecordListView(ListCreateAPIView):
#     serializer_class = RecordSerializer
#     permission_classes = []

# class RecordDetailView();

