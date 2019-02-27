from selenium.webdriver.support import expected_conditions as EC
sfrom selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

url = 'https://www.linkedin.com/'
username = 'cswadhikar@gmail.com'
password = 'Swadhi@1'

# Disables notifications such as 'Chrome is controlled by automated s/w'
options = Options()
# options.add_argument('--disable-notifications')

# Create a driver instance
driver = webdriver.Chrome('c:\\chromedriver.exe', chrome_options=options)

# driver.implicitly_wait(30)
time.sleep(10)


def login():
    driver.get(url)

    if not wait_for_object(By.ID, 'login-email'):
        print '[login()] Failed to open linkedin.com'
        return 0

    # Enter credentials
    email_field = driver.find_element_by_id('login-email')
    pass_field = driver.find_element_by_id('login-password')
    login_btn = driver.find_element_by_id('login-submit')

    email_field.send_keys(username)
    pass_field.send_keys(password)
    login_btn.click()

    # Validate if login is successful
    if wait_for_object(By.LINK_TEXT, 'Swadhikar C'):
        print '[login()] Login successful!'
        return 1

    print 'Login failed!!'
    return 0


def wait_for_object(object_id, element, max_wait_time=30):
    print '[wait_for_object()] Waiting for element:', element

    wait = WebDriverWait(driver, max_wait_time)
    cond = EC.presence_of_element_located((object_id, element))    # Tuple argument

    try:
        wait.until(cond)
        print '[wait_for_object()] Found element:', element
    except TimeoutException:
        print '[wait_for_object()] Unable to locate element:', element, 'by using object id:', object_id
        return 0

    return 1


def profile_views():
    xpath_prof_views = "//span[@class='Sans-21px-black-85% identity-stat']"

    if not wait_for_object(By.XPATH, xpath_prof_views):
        print '[profile_views()] Failed to find profile views button!'
        return 0

    prof_views_btn = driver.find_element_by_xpath(xpath_prof_views)
    prof_views_btn.click()

    if wait_for_object(By.XPATH, "//header[@class='me-wyva-insight-card']"):
        print '[profile_views()] Loaded profile views successfully!'
        return 1

    print 'Failed to load profile views!'
    return 0

    
def close():
    driver.quit()

if __name__ == '__main__':
    try:
        login()
        profile_views()
    finally:
        close()

"""
[wait_for_object()] Waiting for element: login-email
[wait_for_object()] Found element: login-email
[wait_for_object()] Waiting for element: Swadhikar C
[wait_for_object()] Found element: Swadhikar C
[login()] Login successful!
[wait_for_object()] Waiting for element: //span[@class='Sans-21px-black-85% identity-stat']
[wait_for_object()] Found element: //span[@class='Sans-21px-black-85% identity-stat']
[wait_for_object()] Waiting for element: //header[@class='me-wyva-insight-card']
[wait_for_object()] Found element: //header[@class='me-wyva-insight-card']
[profile_views()] Loaded profile views successfully!
"""