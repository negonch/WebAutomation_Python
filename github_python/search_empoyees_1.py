import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SearchEmployees(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://hrm-online.portnov.com/"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)

    def test_search_by_id(self):
        expected_emp_id = '3250'

        browser = self.browser
        username = 'admin'
        password = 'password'
        current = browser.current_url

        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()
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




if __name__ == '__main__':
    unittest.main()
