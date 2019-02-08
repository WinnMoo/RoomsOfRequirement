#This class is used to scrape all the classes listed under one subject
#Example URL to scrape: 
#http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/ACCT.html

import urllib2
from bs4 import BeautifulSoup

pageToParse = urllib2.urlopen(
    'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/CECS.html')

classroom = []
times = []