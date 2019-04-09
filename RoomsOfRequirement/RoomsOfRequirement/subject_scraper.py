#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class is used to scrape all the classes listed under one subject
Example URL to scrape:
http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .classroom import Classroom


DATA = []  # List used to hold all the data scraped from the html
PAGE_TO_PARSE = urlopen(
    ('http://web.csulb.edu/depts/enrollment/registration/class_schedule/'
     'Spring_2019/By_Subject/CECS.html')
)

# python3 -m pip install lxml
PARSED_PAGE = BeautifulSoup(PAGE_TO_PARSE, "lxml")
# gets every element that has the 'td' tag
for element in PARSED_PAGE.find_all('td'):
    DATA.append(element.text)  # add that element to the data list

CLASSROOMS = []
i = 5  # The first entry is at 5, there is a new class every 11 entries
while i < len(DATA):
    FIELDS = (DATA[i], DATA[i+1], DATA[i+3])  # Day, time, class respectively
    # Classes labeled 'TBA' or 'Online-Only' are ignored
    if len(FIELDS[2]) > 8 or FIELDS[2] == 'TBA':
        pass
    else:
        CLASSROOMS.append(Classroom(FIELDS[0], FIELDS[1], FIELDS[2]))
        print(CLASSROOMS[-1])  # Can be removed later
    i += 11
