import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class LulaLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get('https://app.staging-lula.is')
        self.wait = WebDriverWait(self.browser, 30)

    def test_login(self):
        # xpath = "//input[@name='identifier']"
        # css = "input[name='identifier']"
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='identifier']"))
        ).send_keys("student@yopmail.com")

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        ).send_keys("portnov1class")

        self.browser.find_element(By.XPATH, "//button[@type='submit' and text()='Sign In']").click()

        self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Billing"))).click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Payment')]")))

        # '.Table span>span:not([style="white-space: nowrap;"])'
        # '.Table td:nth-child(3) span>span'












if __name__ == '__main__':
    unittest.main()
