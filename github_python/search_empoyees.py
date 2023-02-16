import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from helpers.login import login


class SearchEmployees(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://hrm-online.portnov.com/"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)

    def test_search_by_id(self):
        expected_emp_id = '3250'

        browser = self.browser
        login(browser)
        ## username = 'admin'
        ## password = 'password'
        current = browser.current_url

        ## browser.find_element(By.ID, 'txtUsername').send_keys(username)
        ## browser.find_element(By.ID, 'txtPassword').send_keys(password)
        ## browser.find_element(By.ID, 'btnLogin').click()
        # Wait for new URL
        # Wait for Login Form or button to disappear
        # Wait for the user menu to appear
        wait = WebDriverWait(browser, 5)
        # wait.until(expected_conditions.url_changes(current))
        # wait.until_not(EC.url_contains('/auth/login'))
        # wait.until_not(EC.presence_of_element_located((By.ID, 'frmLogin')))
        wait.until(EC.presence_of_element_located((By.ID, 'welcome')))

        browser.find_element(By.ID, 'empsearch_id').send_keys(expected_emp_id)
        browser.find_element(By.NAME, '_search').click()
        wait.until(EC.text_to_be_present_in_element_attribute((By.ID, 'empsearch_id'), 'value', expected_emp_id))

        emp_id = browser.find_element(
            By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[2]/a').text

        self.assertEqual(expected_emp_id, emp_id)

    def test_search_by_employment_status(self):
        browser = self.browser
        username = 'admin'
        password = 'password'

        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()
        wait = WebDriverWait(browser, 5)
        wait.until(EC.presence_of_element_located((By.ID, 'welcome')))
        expected_emp_status = 'Part Time'

        Select(browser.find_element(By.ID, 'empsearch_employee_status')).select_by_visible_text(expected_emp_status)
        browser.find_element(By.NAME, '_search').click()

        # TODO: optimise this wait with text relative xpath
        wait.until(EC.element_attribute_to_include(
            (By.XPATH, '//*[@id="empsearch_employee_status"]/option[4]'), 'selected'))

        list_of_cells = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[6]')

        for count, cell in enumerate(list_of_cells, 1):
            self.assertEqual(
                expected_emp_status, cell.text,
                f'Value "{cell.text}" within row #{count} does not match expected value "{expected_emp_status}"')

        ###### OR
        # rows = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr')
        # for r in rows:
        #     self.assertEqual(expected_emp_status, r.find_element(By.XPATH, './/td[6]').text)


if __name__ == '__main__':
    unittest.main()
