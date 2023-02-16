import unittest

from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_employee_page import AddEmployeePage
from pages.employee_information_page import EmployeeInformationPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


class AddEmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://hrm-online.portnov.com/"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 6)
        self.login_page = LoginPage(self.browser)
        self.emp_info = EmployeeInformationPage(self.browser)
        self.add_emp = AddEmployeePage(self.browser)
        self.personal_details = PersonalDetailsPage(self.browser)

    def test_add_employee_default_fields(self):
        first_name = Faker().first_name()
        last_name = Faker().last_name()
        emp_id = Faker().random.randrange(400000, 1000000)

        self.login_page.login()
        self.emp_info.do_add_employee()
        self.add_emp.enter_employee_info(emp_id, first_name, last_name)
        self.add_emp.do_save()
        self.assertEqual(self.personal_details.PAGE_NAME, self.personal_details.get_header())
        self.assertEqual(first_name, self.personal_details.get_first_name())
        self.assertEqual(last_name, self.personal_details.get_last_name())
        self.assertEqual(emp_id, int(self.personal_details.get_employee_id()))


if __name__ == '__main__':
    unittest.main()
