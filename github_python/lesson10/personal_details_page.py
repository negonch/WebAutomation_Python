from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class PersonalDetailsPage(BasePage):
    @property
    def PAGE_NAME(self):
        return 'Personal Details'

    def get_header(self):
        return self.wait.until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '.personalDetails .head h1'))).text

    def get_first_name(self):
        return self.browser.find_element(By.ID, 'personal_txtEmpFirstName').get_attribute('value')

    def get_last_name(self):
        return self.browser.find_element(By.ID, 'personal_txtEmpLastName').get_attribute('value')

    def get_employee_id(self):
        return self.browser.find_element(By.ID, 'personal_txtEmployeeId').get_attribute('value')
