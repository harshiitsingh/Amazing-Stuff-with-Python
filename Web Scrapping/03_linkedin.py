from bs4 import BeautifulSoup as bs
import requests

res = requests.get('https://www.linkedin.com/posts/spaceonova_ai-space-technology-activity-6916284060117979136-KLw2?utm_source=linkedin_share&utm_medium=member_desktop_web')
# print("The status code is ", res.status_code)
# print("\n")
# soup_data = bs(res.text, 'html.parser')
# print(soup_data.title)
# print("\n")
# print(soup_data.find_all('h4'))

match3 = bs.find('div', class_="share-update-card__update-text")
print(match3)