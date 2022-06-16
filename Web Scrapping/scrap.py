#importing webdriver from selenium
from selenium import webdriver
   
#selecting Firefox as the browser
#in order to select Chrome 
# webdriver.Chrome() will be used
driver = webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe')
   
#URL of the website 
url = "https://www.geeksforgeeks.org/"
   
#opening link in the browser
driver.get(url)

# scrapping the content
# scrapping the likes and comments