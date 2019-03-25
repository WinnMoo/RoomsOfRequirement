"""
Created on Tue Mar 7 12:26:53 2019

@author: chris
"""
from rest_framework import routers
from .api import ClassroomViewSet, WeekdayViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register('api/Classrooms', ClassroomViewSet, 'Classrooms')
ROUTER.register('api/Weekdays', WeekdayViewSet, 'Weekdays')

urlpatterns = ROUTER.urls
