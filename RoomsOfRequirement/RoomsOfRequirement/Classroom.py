"""
Created on Tue Feb 12 16:56:23 2019

@author: winn
"""


class Classroom:
    """Classroom that contains time slot(s), days of week, and room number"""

    DOW = {'M': 'Monday', 'Tu': 'Tuesday',
           'W': 'Wednesday', 'Th': 'Thursday', 'F': 'Friday'}

    def __init__(self, day, time, classroomNumber):
        self.format_classroom_number(classroomNumber)
        self.format_days(day)
        self.format_times(time)

    def __str__(self):
        return 'Days: {0:23} Time: {1:15} Building: {2} Room #: {3}'.format(
            str(self.days),
            self.start + '-' + self.end,
            self.building,
            self.room)

    def format_classroom_number(self, classroom_number):
        """Initializes building and room number from title"""

        tokens = classroom_number.split('-')
        self.building = tokens[0]
        self.room = tokens[1]

    # If you guys want, you can change this to hold just the initials instead
    # of the full names of the dates
    def format_days(self, day):
        """Initializes days of the week from small string"""

        self.days = []
        for char in day:
            if char in ('M', 'W', 'F'):
                self.days.append(self.DOW[char])
                # self.days.append(char)
            elif char in ('h', 'u'):
                self.days.append(self.DOW['T' + char])
                # self.days.append('T' + char)

    def format_times(self, time):
        """Initializes start and end time from minified string"""

        times = time.split('-')
        self.start = times[0]
        self.end = times[1]

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
