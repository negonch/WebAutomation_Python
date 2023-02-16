from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class SystemUsersPage(BasePage):
    @property
    def PAGE_NAME(self):
        return "System Users"

    @property
    def PAGE_URL(self):
        return '/admin/viewSystemUsers'

    def do_user_search(self, value):
        self.browser.find_element(
            By.ID, 'searchSystemUser_userName').send_keys(value)
        self.browser.find_element(By.ID, 'searchBtn').click()
        self.wait.until(expected_conditions.text_to_be_present_in_element_value(
            (By.ID, 'searchSystemUser_userName'), value))
