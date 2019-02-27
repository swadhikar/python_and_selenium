from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import variables
from log_util.logger import log
from lib.lib_os_util import get_current_timestamp
from selenium.webdriver.chrome.options import Options

main_window_handle = None


def get_driver(browser_name, chrome_disable_notifications=True):
    if str(browser_name).lower() == 'chrome':
        if chrome_disable_notifications:
            options = Options()
            options.add_argument('--disable-notifications')
            return webdriver.Chrome(executable_path=variables.WIN_CHROME_DRIVER, chrome_options=options)

        return webdriver.Chrome(executable_path=variables.WIN_CHROME_DRIVER)

    if str(browser_name).lower() == 'firefox':
        return webdriver.Firefox()

    if str(browser_name).lower() == 'safari':
        return webdriver.Safari()

    log.info("Driver not supported for browser: '{}'".format(browser_name))
    return None


def open_url(driver, url):
    driver.get(url)
    sleep(5)
    return 1


def bring_focus(driver):
    driver.execute_script("window.focus()")
    sleep(0.5)
    log.info("[WebDriver] Firefox window brought into focus")
    return 1


def create_new_tab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.switch_to_window(driver.window_handles[-1])

    log.info("[WebDriver] New tab created!")
    return 1


def toggle_to_main_window(driver):
    driver.switch_to.window(main_window_handle)

    log.info("[WebDriver] Toggle to main window successful!")
    return 1


def close_current_tab(driver):
    body = driver.find_element_by_tag_name('body')
    if not body:
        log.info("[WebDriver] Unable to find tag: 'body'")
    body.send_keys(Keys.COMMAND + 'w')
    log.info("[WebDriver] Current tab closed!")

    log.info("[WebDriver] Current tab closed successfully!")
    return 1


def close(driver):
    driver.quit()


def capture_screen(driver=None, path=None, filename='screen', timestamp=False):
    if not path:
        path = variables.SCREENSHOT_PATH

    filename = path + filename
    if timestamp:
        filename += get_current_timestamp()
    filename += ".png"

    driver.get_screenshot_as_file(filename)

    log.info("[WebDriver] Screenshot captured: '{}'".format(filename))
    return 1

def _is_element_located(driver, id_type, id):
    try:
        driver.find_element(id_type, id)
        return 1
    except selenium.common.exceptions.NoSuchElementException:
        return 0


def wait_for_object(driver, id=None):
    if _is_element_located(driver, By.LINK_TEXT, id):
        return 1
    elif _is_element_located(driver, By.XPATH, id):
        return 1
    elif _is_element_located(driver, By.TAG_NAME, id):
        return 1
    elif _is_element_located(driver, By.NAME, id):
        return 1
    elif _is_element_located(driver, By.ID, id):
        return 1
    elif _is_element_located(driver, By.PARTIAL_LINK_TEXT, id):
        return 1
    elif _is_element_located(driver, By.CSS_SELECTOR, id):
        return 1
    elif _is_element_located(driver, By.CLASS_NAME, id):
        return 1

    log.error("[WebDriver] Element not found: '{}'".format(id))
    return 0


if __name__ == '__main__':
    pass
