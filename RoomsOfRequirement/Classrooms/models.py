"""
Created on Tue Mar 7 12:26:53 2019

@author: chris
"""
from django.db import models


class Classroom(models.Model):
    """Models the pre-exisiting tables in the database"""

    class_id = models.IntegerField(primary_key=True)
    classroom = models.TextField()
    weekday = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'CLASSROOM'
