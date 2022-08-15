'''
How To Store Scraped Data In A CSV File?
You can use a more structured approach to store the data by storing it in a csv file instead of in a text files.

Approach:

-Define the headers for the columns of your csv and store them in a list.
-Create a list and store the title, price, description, and rating of each product in the list.
-Segregate the values for each product individually by slicing and storing them in another list.
-Create and open a new csv file.
    -Note: You must import the csv module before you can use the csvwriter object to write to the csv file.
-Once the file is created, store the data in the csv file with the help of the csvwriter object.
'''

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

    company_name = job.find('div', class_="heading_6 company_name").text
    role_name = job.find('div', class_="heading_4_5 profile").text
    more_info = job.find('div', class_="heading_4_5 profile").a['href']
    
    
# import csv
# def Save_csv():
#     row_head =['Company Name', 'Job Role Name', 'Salary', 'More Info']
#     Data = []
#     for title, role, sal, info in zip(company_name, role_name, salary[1], more_info):
#         Data.append(title)
#         Data.append(role)
#         Data.append(sal)
#         Data.append(info)
#     rows = [Data[i:i + 4] for i in range(0, len(Data), 4)]
#     with open('data.csv', 'w', encoding='utf_8_sig', newline="") as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(row_head)
#         csvwriter.writerows(rows)

# https://blog.finxter.com/storing-scraped-data/