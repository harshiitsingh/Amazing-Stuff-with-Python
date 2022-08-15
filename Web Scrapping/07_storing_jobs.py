# Storing the jobs paragraph in text files

from urllib import request
from bs4 import BeautifulSoup
import requests # to request information from a specific website.

# Job filtration by owned skills
print("Put some skills you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://internshala.com/jobs/work-from-home/?utm_source=is_menu_dropdown').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_="internship_meta")

for index, job in enumerate(jobs): # enumerate will help to iterate over the job index and its contents
    # index is a kind of counter for the job we are iterating on.
    salary=[]
    for s in job.find_all('div', class_='item_body'):
        salary.append(s.text)
   
    company_name = job.find('div', class_="heading_6 company_name").text
    role_name = job.find('div', class_="heading_4_5 profile").text
    more_info = job.find('div', class_="heading_4_5 profile").a['href']
    
    if unfamiliar_skill not in role_name:
        with open(f'posts/{index}.txt', 'w') as f:
            
            f.write(f"Company Name: {company_name.strip()} \n") # strip() will erase all the blank spaces
            f.write(f"Job Role Name: {role_name.strip()} \n")
            f.write(f"Salary: {salary[1].strip()} \n")
            f.write(f"More Info: {more_info} \n")

        print(f'File Saved: {index}')