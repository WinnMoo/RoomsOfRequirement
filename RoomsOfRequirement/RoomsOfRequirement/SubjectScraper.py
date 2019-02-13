#This class is used to scrape all the classes listed under one subject
#Example URL to scrape: 
#http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html

from urllib.request import urlopen
from bs4 import BeautifulSoup


data = [] #List used to hold all the data scraped from the html
pageToParse = urlopen(
    'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/CECS.html')

parsedPage = BeautifulSoup(pageToParse, "lxml")
for element in parsedPage.find_all('td'): #gets every element that has the 'td' tag
    data.append(element.text)  #add that element to the data list
    element.next_sibling

#lists used to hold the individual data sets for each class
days = []
times = []
classrooms = []


#data[] has all the info per class, every 11 lines is a new class
dayIndex = 5 #every interval of 5+(11*n) is the day table column
while dayIndex < len(data):
    days.append(data[dayIndex]) #add the day to the days list
    dayIndex = dayIndex + 11
    
timeIndex = 6
while timeIndex < len(data):
    times.append(data[timeIndex])
    timeIndex = timeIndex + 11

classIndex = 8
while classIndex < len(data):
    classrooms.append(data[classIndex])
    classIndex = classIndex + 11


#this block is used to remove unnecessary data such as classes with 'TBA' or 'Online-Only'
i = len(classrooms)-1
while i > 0:
    if len(classrooms[i]) > 8:
        del classrooms[i]
        del times[i]
        del days[i]
    elif classrooms[i] == "TBA":
        del classrooms[i]
        del times[i]
        del days[i]
    i = i - 1
    
print(days)
print(times)
print(classrooms)





