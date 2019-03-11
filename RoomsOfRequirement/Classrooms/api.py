"""
Created on Tue Mar 7 12:26:53 2019

@author: chris
"""
from rest_framework import viewsets, permissions
from .models import Classroom
from .serializers import ClassroomSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    """Deploys the APIs needed by our frontend"""

    queryset = Classroom.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassroomSerializer
