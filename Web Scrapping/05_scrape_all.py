from urllib import request
from bs4 import BeautifulSoup
import requests # to request information from a specific website.

html_text = requests.get('https://internshala.com/jobs/work-from-home/?utm_source=is_menu_dropdown').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_="internship_meta")

for job in jobs:
    salary=[]
    for s in job.find_all('div', class_='item_body'):
        salary.append(s.text)
        
    # if salary[1] >= "4":
    company_name = job.find('div', class_="heading_6 company_name").text.replace(' ', '')
    role_name = job.find('div', class_="heading_4_5 profile").text

    print(f'''
        Company Name: {company_name}
        Job Role Name: {role_name}
        Salary: {salary[1]}
        ''')
    
    print('') # empty line  