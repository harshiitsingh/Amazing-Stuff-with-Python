# connect python with webbrowser-chrome
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui as pag

# https://youtu.be/ijT2sLVdnPM
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#  to start ChromeDriver with existing login, not to start in guest mode
# options.add_argument(r'--user-data-dir=C:\\Users\\harma\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--profile-directory=Harshit Singh')

# browser = webdriver.Chrome()
# driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# driver.get('https://www.google.com')

def main():
    # url of LinkedIn
    url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    # url of LinkedIn network page
    network_url = "https://www.linkedin.com/mynetwork/" 
    # path to browser web driver
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
    # driver.get(url)
    start_bot(driver, url, network_url)
    # login_to_linkedin(driver)

def login_to_linkedin(driver):
    username = driver.find_element(By.ID, "username")
    username.send_keys("your username")
    password = driver.find_element(By.ID, "password")
    password.send_keys("your password")
    # driver.find_element(By.CLASS_NAME, 'button.btn-md').click()
    try:
        driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large").click()
    except Exception as e:
        print(e)
    # driver.find_element("id", "sign-in-form__submit-btn").click() 

    # print(driver.find_element(By.ID, 'sign-in-form__submit-btn'))

def  goto_network_page(driver,network_url):
    driver.get(network_url)

def  accept_invitations_from_users(driver):
    # javaScript =  "window.scrollBy(0,0);"
    # driver.execute_script(javaScript)
    
    # Scroll to the top of the page
    driver.execute_script("window.scrollTo(0, 0)")
    
    element_exists =  True
    flag=1
    while element_exists and flag:
        try:
            # Find the invitation element
            driver.find_element(By.CSS_SELECTOR, '.invitation-card__action-container.pl3')
        except NoSuchElementException as e:  # handle the element not existing
            element_exists =  False
            print(e)
        finally:
            if element_exists:
                driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.invitation-card__action-btn").click()
                flag=0

def  start_bot(driver,url,network_url):
    driver.get(url)
    login_to_linkedin(driver)
    goto_network_page(driver,network_url)
    accept_invitations_from_users(driver)

# Driver's code
if __name__ == "__main__":
    main()