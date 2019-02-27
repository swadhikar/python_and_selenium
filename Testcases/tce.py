from browser_framework.basetest import BaseTestCase
from log_util.logger import log
import browser_framework.driver_util as driver_util
import time


class TCE(BaseTestCase):
    browser = driver_util.get_driver('firefox')

    @staticmethod
    def open_portal(browser):
        driver_util.open_url(browser, 'http://www.tce.edu/')
        return driver_util.wait_for_object_by_id(browser, 'logo', 20)

    @staticmethod
    def check_tabs(browser):
        list_tab_names = ['Home', 'About TCE', 'Academics', 'Admission', 'Departments', 'Research', 'Contact Us']

        for tab in list_tab_names:
            if not driver_util.wait_for_object(browser, id=tab):
                raise Exception("Unable to detect tab: '{}'".format(tab))
            else:
                log.info("[TCE.check_tabs()] Found tab: '{}'".format(tab))

            time.sleep(1)

        log.info("[TCE.check_tabs()] Detected all the tabs successfully!")

        return 1

    @staticmethod
    def check_logo(browser):
        img_xpath = "//img[contains(@src, 'tce_logo.png')]"

        if not driver_util.wait_for_object(browser, img_xpath):
            raise Exception("Unable to find tce logo in portal")

        return 1

    @staticmethod
    def tear_down():
        driver_util.close(TCE.browser)


class TC00001(TCE):
    """
        Tests if the TCE portal is loaded successfully
    """

    def __init__(self):
        super(TC00001, self).__init__()
        self.execute_step(self.open_portal, "Opens TCE website", self.browser)
        self.execute_step(driver_util.capture_screen, "Capture screen after login", driver=self.browser,
                          filename='login_success')

    @property
    def result(self):
        return 1


class TC00002(TCE):
    """
        Tests if the TCE portal all tabs in the page are loaded successfully
    """

    def __init__(self):
        super(TC00002, self).__init__()
        self.execute_step(self.open_portal, "Opens TCE website", self.browser)
        self.execute_step(self.check_tabs, "Checks if all the tabs are displayed correctly", self.browser)
        self.execute_step(driver_util.capture_screen, "Capture screen for all tabs", driver=self.browser,
                          filename='tabs_success')

    @property
    def result(self):
        return 1


class TC00003(TCE):
    """
        Tests if the TCE portal contains vinaiye uyir logo
    """

    def __init__(self):
        super(TC00003, self).__init__()
        self.execute_step(self.open_portal, "Opens TCE website", self.browser)
        self.execute_step(self.check_logo, "Checks if tce logo exists in the portal", self.browser)
        self.execute_step(driver_util.capture_screen, "Capture screen for logo success", driver=self.browser,
                          filename='logo_success')

    @property
    def result(self):
        return 1


if __name__ == "__main__":
    pass
    # print TC00001().result
    # TC00001.tear_down()
    # print TC00002().result
    # TC00002.tear_down()
    # print TC00003().result
    # TC00003.tear_down()

