'''
To scrape a website, one must have to use inspect tool mostly.
And must know about it, about code, tags and attributes etc.'''

# must install the request library

from urllib import request
from bs4 import BeautifulSoup
import requests # to request information from a specific website.

html_text = requests.get('https://internshala.com/jobs/work-from-home/?utm_source=is_menu_dropdown').text
# print("Request code status: ", html_text)

soup = BeautifulSoup(html_text, 'lxml')
# jobs = soup.find_all('div', class_="internship_meta")
job = soup.find('div', class_="internship_meta")
# print(job)

company_name = job.find('div', class_="heading_6 company_name").text.replace(' ', '')
# print(company_name)

role_name = job.find('div', class_="heading_4_5 profile").text
# print(role_name.text)

# print(f'''
#       Company Name: {company_name}
#       Job Role Name: {role_name}
#       ''')

# salary = job.find_all('div', class_='item_body')
# print(salary)

# for s in job.find_all('div', class_='item_body'):
#     print(s.text)

salary=[]
for s in job.find_all('div', class_='item_body'):
    salary.append(s.text)
    
# print(salary)
print((salary[1]))
# print(type(salary[1]))
    