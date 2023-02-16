import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from helpers.login import login


class TableSort(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://hrm-online.portnov.com/"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 6)
        login(self.browser)

    def test_sort_by_first_middle_name(self):
        browser = self.browser
        browser.find_element(By.XPATH, '//*[@id="resultTable"]/thead/tr/th[3]/a').click()
        time.sleep(2) #TODO: replace with WDW

        bottom_name = ''
        while True:   #TODO: remember to add a condition
            list_of_names = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]/a')

            for i, name in enumerate(list_of_names):
                if i+1 < len(list_of_names):
                    self.assertLessEqual(name.text, list_of_names[i+1].text)
                    print(f'{name.text} is before {list_of_names[i+1].text}')
                else:
                    bottom_name = name
            try:
                pagination = browser.find_element(By.CLASS_NAME, 'desc').text
                pieces = pagination.split(' ')
                if pieces[-1] in pieces[0]:
                    break
                else:
                    browser.find_element(By.LINK_TEXT, 'Next').click()
            except NoSuchElementException:
                break



if __name__ == '__main__':
    unittest.main()
