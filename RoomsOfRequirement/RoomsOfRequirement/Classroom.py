#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:56:23 2019

@author: winn
"""

class Classroom():
    def __init__(self, classroomNumber, day, time):
        self.classroomNumber = classroomNumber
        self.day = day
        
        
    def formatTime(time):
        times = time.split('-')
        startTime = times[0]
        endTime = times[1]
        
        #TODO convert from 12hr format to 24hr format
        # datetime.strptime(startTime, "%H:%M")
        if endTime[-2:] == "AM":
            startTime = startTime + 'AM'
        else:
            startTime = endTime + 'PM'
        
        
        if ':' not in startTime: 
            startTime = startTime + ':00'
        
        if ':' not in endTime:
            endTime = endTime + ':00'
            
            
        
        self.StartTime
        self.EndTime