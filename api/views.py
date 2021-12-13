from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.decorators import action, permission_classes, api_view, action


from habittracker.models import Habit
from .serializers import HabitSerializer, RecordSerializer, UserSerializer
from habittracker.models import Habit, DailyRecord, User
from .permissions import IsOwnerOrReadOnly


# Viewsets show views based on .models
# permission classes attribute sets who can access endpoint

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'records': reverse('record-list', request=request, format=format),
        'habits': reverse('habits_list', request=request, format=format)
    })


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]



class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecordListView(viewsets.ListAPIView):
    queryset = DailyRecord.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecordDetailView(viewsets.RetrieveAPIView):
    queryset = DailyRecord.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]

