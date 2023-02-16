import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://hrm.portnov.com/"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_something(self):
        browser = self.browser
        # browser = webdriver.Chrome(service=Service('/Users/ellie/Portnov2022/TestAutomation/drivers/chromedriver'))
        browser.get(self.url)
        # browser.get("http://hrm.portnov.com/")
        time.sleep(3)
        self.assertEqual('OrangeHRM', browser.title)  # add assertion here
        btn_value = browser.find_element(By.ID, 'btnLogin').get_attribute('value')
        self.assertEqual('LOGIN', btn_value)
        panel_header = browser.find_element(By.ID, 'logInPanelHeading').text
        self.assertEqual('LOGIN Panel', panel_header)
        self.assertIn('/auth/login', browser.current_url)

    def test_something_else(self):
        pass











if __name__ == '__main__':
    unittest.main()
