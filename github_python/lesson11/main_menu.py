from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainMenu:
    def __init__(self, browser: webdriver.Remote):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def open_admin(self):
        self.browser.find_element(By.ID, 'menu_admin_viewAdminModule').click()