# This class is used to scrape all the classes listed under one subject
# Example URL to scrape:
# http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
from Classroom import Classroom


data = []  # List used to hold all the data scraped from the html
pageToParse = urlopen(
    'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/CECS.html')

parsedPage = BeautifulSoup(pageToParse, "lxml")  # python3 -m pip install lxml
# gets every element that has the 'td' tag
for element in parsedPage.find_all('td'):
    data.append(element.text)  # add that element to the data list
    element.next_sibling

classrooms = []
i = 5  # The first entry is at 5, there is a new class every 11 entries
while i < len(data):
    fields = (data[i], data[i+1], data[i+3])  # Day, time, class respectively
    # Classes labeled 'TBA' or 'Online-Only' are ignored
    if len(fields[2]) > 8 or fields[2] == 'TBA':
        pass
    else:
        classrooms.append(Classroom(fields[0], fields[1], fields[2]))
        print(classrooms[-1])  # Can be removed later
    i += 11
