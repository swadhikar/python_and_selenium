import constants
import time


class SeleniumUiElement:
    def __init__(self, by, eid, driver):
        self.by = by
        self.eid = eid
        self.driver = driver

    def __str__(self):
        return '{}({}, {}, {})'.format(self.__class__.__name__, self.by, self.eid, self.driver)


class DropDown(SeleniumUiElement):
    pass


class Input(SeleniumUiElement):
    pass


class CheckBox(SeleniumUiElement):
    pass


class RadioButton(SeleniumUiElement):
    pass


class MyClass:
    def __init__(self):
        self.driver = ''

    def get_ui_element_from_id(self, element_id):
        from selenium.webdriver.common.by import By  # TODO
        from random import choice    # TODO To remove

        # element_tag = self.driver.find_element(By.ID, element_id).get_attribute('type')    # Confirm in page
        element_tag = choice(['input', 'select', 'checkbox', 'radio'])    # TODO To remove

        if element_tag == 'input':
            return Input(By.ID, element_id, self.driver)

        if element_tag == 'select':
            return DropDown(By.ID, element_id, self.driver)

        if element_tag == 'checkbox':
            return CheckBox(By.ID, element_id, self.driver)

        if element_tag == 'radio':
            return RadioButton(By.ID, element_id, self.driver)

        return SeleniumUiElement(By.ID, element_id, self.driver)

    def create_user(self, dictionary):
        from collections import OrderedDict     # TODO move it to top of the file

        for k, v in dictionary.items():
            if isinstance(v, OrderedDict):
                self.create_user(dictionary[k])    # TODO self
            else:
                self.perform_action(k, v)

    def perform_action(self, element_id, action):
        element = self.get_ui_element_from_id(element_id)

        if isinstance(element, DropDown):
            # element.select_option_by_text(action)
            print 'Selecting {} in {} drop down'.format(action, element_id)    # TODO add proper comments
        elif isinstance(element, CheckBox):
            # element.click(action['check'])     # TODO check before clicking
            print 'Checking {} in {} checkbox'.format(action, element_id)
        elif isinstance(element, RadioButton):
            # element.click(action['click'])     # TODO check before clicking
            print 'Clicking {} in {} radio button'.format(action, element_id)
        elif isinstance(element, Input):
            # element.send_text(action) # TODO check before clicking
            print 'Sending {} to {} textbox'.format(action, element_id)
        else:
            pass    # Handle
        time.sleep(1)


if __name__ == '__main__':
    my = MyClass()
    my.create_user(constants.guest_portal)

    # C:\Python27\python.exe my_module.py
    # Selecting  TestPortalName in portalName drop down
    # Checking Test Portal for testing guest access in portalDesc checkbox
    # Clicking  {'check': False} in checkbox1 radio button
    # Selecting {'check': True} in checkbox2 drop down
    # Sending {'option': 'Select this drop down option'} to select1 textbox
    # Clicking {'click': True} in radiobutton1 radio button
    # Sending {'check': True} to checkbox2 textbox
