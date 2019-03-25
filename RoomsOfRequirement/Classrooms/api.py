"""
Created on Tue Mar 7 12:26:53 2019

@author: chris
"""
from rest_framework import viewsets, permissions
from .models import Classroom, Weekday
from .serializers import ClassroomSerializer, WeekdaySerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    """Deploys the APIs needed by our frontend"""

    queryset = Classroom.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassroomSerializer


class WeekdayViewSet(viewsets.ModelViewSet):
    """Deploys the APIs needed by our frontend"""

    queryset = Weekday.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WeekdaySerializer
