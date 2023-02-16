from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EmployeeInformationPage(BasePage):
    def do_add_employee(self):
        self.browser.find_element(By.ID, 'btnAdd').click()

    def do_delete_employee(self):
        #TODO: complete later
        pass
