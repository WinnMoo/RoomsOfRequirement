#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:56:23 2019

@author: winn
"""
from datetime import datetime


class Classroom:
    DOW = {'M': 'Monday', 'Tu': 'Tuesday',
           'W': 'Wednesday', 'Th': 'Thursday', 'F': 'Friday'}

    def __init__(self, day, time, classroomNumber):
        self.formatClassRoomNumber(classroomNumber)
        self.formatDays(day)
        self.formatTimes(time)

    def __str__(self):
        return 'Days: {0:23} Time: {1:15} Building: {2} Room #: {3}'.format(
            str(self.days),
            self.start + '-' + self.end,
            self.building,
            self.room)

    def formatClassRoomNumber(self, classroomNumber):
        tokens = classroomNumber.split('-')
        self.building = tokens[0]
        self.room = tokens[1]

    # If you guys want, you can change this to hold just the initials instead 
    # of the full names of the dates
    def formatDays(self, day):
        self.days = []
        for c in day:
            if c == 'M' or c == 'W' or c == 'F':
                self.days.append(self.DOW[c])
                # self.days.append(c)
            elif c == 'h' or c == 'u':
                self.days.append(self.DOW['T' + c])
                # self.days.append('T' + c)

    def formatTimes(self, time):
        times = time.split('-')
        self.start = times[0]
        self.end = times[1]

        # TODO convert from 12hr format to 24hr format
        if ':' not in self.start:
            self.start += ':00'
        if ':' not in self.end:
            # Removes the AM/PM from end of string, then adds it after ':00'
            am_pm = self.end[-2:]
            self.end = self.end[:-2] + ':00 ' + am_pm

        if self.end[-2:] == 'AM':
            self.start += 'AM'
        else:
            self.start += 'PM'
        
        # a = datetime.strptime(self.start, "%H:%M")
