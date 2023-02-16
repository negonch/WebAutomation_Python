from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class WelcomeMenu:
    def __init__(self, browser: webdriver.Remote):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def logout(self):
        self.browser.find_element(By.ID, 'welcome').click()
        # self.browser.find_element(By.CSS_SELECTOR, '#welcome-menu li:last-child a').click()
        # OR
        self.browser.find_element(By.LINK_TEXT, 'Logout').click()

    def get_welcome_message(self):
        return self.browser.find_element(By.ID, 'welcome').text