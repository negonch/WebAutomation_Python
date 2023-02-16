from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddEmployeePage(BasePage):
    def enter_employee_info(self, emp_id, first_name="Bob", last_name="Smith"):
        self.browser.find_element(By.ID, 'firstName').send_keys(first_name)
        self.browser.find_element(By.ID, 'lastName').send_keys(last_name)

        self.browser.find_element(By.ID, 'employeeId').clear()
        self.browser.find_element(By.ID, 'employeeId').send_keys(emp_id)

    def do_save(self):
        self.browser.find_element(By.ID, 'btnSave').click()
