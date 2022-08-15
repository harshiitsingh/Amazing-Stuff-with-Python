# Setting up the Project to scrape every 10 minutes.

from urllib import request
from bs4 import BeautifulSoup
import requests # to request information from a specific website.
import time

# Job filtration by owned skills
print("Put some skills you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://internshala.com/jobs/work-from-home/?utm_source=is_menu_dropdown').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_="internship_meta")

    for job in jobs:
        salary=[]
        for s in job.find_all('div', class_='item_body'):
            salary.append(s.text)
            
        company_name = job.find('div', class_="heading_6 company_name").text
        role_name = job.find('div', class_="heading_4_5 profile").text
        more_info = job.find('div', class_="heading_4_5 profile").a['href']
        
        if unfamiliar_skill not in role_name:
            print(f"Company Name: {company_name.strip()}") # strip() will erase all the blank spaces
            print(f"Job Role Name: {role_name.strip()}")
            print(f"Salary: {salary[1].strip()}")
            print(f"More Info: {more_info}")
        
            print('') # empty line
            
if __name__ == '__main__':
    while True:
        find_jobs()
        
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)