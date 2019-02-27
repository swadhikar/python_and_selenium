# Python module to test social media like facebook and linked in
from time import sleep

from browser_framework.basetest import BaseTestCase
from lib.variables import FACEBOOK_URL, FACEBOOK_USER, LINKEDIN_USER, LINKEDIN_URL
from log_util.logger import log


class Facebook(BaseTestCase):
    def login_page(self):
        driver = self.driver
        driver.get(FACEBOOK_URL)
        log.info("Facebook loaded successfully")
        # Enter credentials
        field = driver.find_element_by_id('email')
        field.click()
        field.clear()
        field.send_keys(FACEBOOK_USER)
        field = driver.find_element_by_id('pass')
        field.click()
        field.clear()
        field.send_keys("<your password>")
        field = driver.find_element_by_id('loginbutton')
        field.click()
        driver.implicitly_wait(5)
        return 1

    def validate_login(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href,'ref=logo')]")
        log.info("Facebook logo found")
        sleep(5)
        return 1

    def close(self):
        driver = self.driver
        driver.quit()

    @property
    def result(self):
        fb = Facebook()
        try:
            fb.login_page()
            fb.validate_login()
            fb.take_screen_shot('login_page')
        finally:
            fb.close()

        return 1


class LinkedIn(BaseTestCase):
    def login_page(self):
        driver = self.driver
        driver.get(LINKEDIN_URL)
        log.info("[LinkedIn] Linkedin loaded successfully")
        # Enter credentials
        field = driver.find_element_by_id('login-email')
        field.click()
        field.clear()
        field.send_keys(LINKEDIN_USER)
        field = driver.find_element_by_id('login-password')
        field.click()
        field.clear()
        field.send_keys("<your password>")
        field = driver.find_element_by_id('login-submit')
        field.click()
        driver.implicitly_wait(5)
        return 1

    def validate_login(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href,'swadhikar-c')]") # validate if profile link exists
        log.info("[LinkedIn] Linked in login successful. Profile link displayed!")
        sleep(5)
        return 1

    def close(self):
        driver = self.driver
        driver.quit()

    @property
    def result(self):
        li = LinkedIn()
        try:
            li.login_page()
            li.validate_login()
            li.take_screen_shot('linked_in_login_page')
        finally:
            li.close()

        return 1


if __name__ == '__main__':
    pass
    # print Facebook().result # Test facebook login
    # print LinkedIn().result # Test facebook login
