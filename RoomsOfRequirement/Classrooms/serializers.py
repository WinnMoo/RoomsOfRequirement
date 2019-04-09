"""
Created on Tue Mar 7 12:26:53 2019

@author: chris
"""
from rest_framework import serializers
from .models import Classroom, Weekday


class ClassroomSerializer(serializers.ModelSerializer):
    """Handles serialization of Classroom model"""

    class Meta:
        model = Classroom
        fields = '__all__'


class WeekdaySerializer(serializers.ModelSerializer):
    """Handles serialization of Weekday model"""

    class Meta:
        model = Weekday
        fields = '__all__'
