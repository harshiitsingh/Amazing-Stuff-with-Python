# Learnt from: https://www.youtube.com/watch?v=ng2o98k983k
'''
Scraping website means parsing the content from my website and pulling out the exact info
that we want.
Eg. Pulling headlines from a news site, grab some scores a sports website, monitor
the prices of the items in an online store or something like that.'''

'''
There are different types of parsers
Difference Between Parsers: https://goo.gl/zdy9br'''

# here we will use lxml parser # pip install lxml
# pip install html5lib # it will install html5lib parser 

from bs4 import BeautifulSoup
import requests

with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup) # print the whole html code
print(soup.prettify()) # print the whole html code in a proper formatted and indented way

# TO GRAB INFO FROM THE HTML FILE
match  = soup.title # to get the title of the wbsite
print(match)

match1  = soup.title.text
print(match1)

match2 = soup.div
print(match2)

match3 = soup.find('div', class_ = 'footer')
print(match3)