from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: webdriver.Remote):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
