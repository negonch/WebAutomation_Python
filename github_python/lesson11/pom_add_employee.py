import unittest

from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from menus.main_menu import MainMenu
from menus.welcome_menu import WelcomeMenu
from pages.add_employee_page import AddEmployeePage
from pages.employee_information_page import EmployeeInformationPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage
from pages.system_users_page import SystemUsersPage


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
        self.main_menu = MainMenu(self.browser)
        self.welcome_menu = WelcomeMenu(self.browser)
        self.sys_user = SystemUsersPage(self.browser)

    def test_add_employee_default_fields(self):
        first_name = Faker().first_name()
        last_name = Faker().last_name()
        emp_id = Faker().random.randrange(400000, 1000000)

        self.login_page.login()
        self.assertEqual(self.emp_info.PAGE_NAME, self.emp_info.get_header())
        self.emp_info.do_add_employee()
        self.assertEqual(self.add_emp.PAGE_NAME, self.add_emp.get_header())
        self.add_emp.enter_employee_info(emp_id, first_name, last_name)
        self.add_emp.do_save()
        self.assertEqual(self.personal_details.PAGE_NAME, self.personal_details.get_header())
        self.assertEqual(first_name, self.personal_details.get_first_name())
        self.assertEqual(last_name, self.personal_details.get_last_name())
        self.assertEqual(emp_id, int(self.personal_details.get_employee_id()))

    def test_add_user(self):
        first_name = Faker().first_name()
        last_name = Faker().last_name()
        emp_id = Faker().random.randrange(400000, 1000000)

        self.add_emp.go_to_page()
        self.login_page.login()
        self.assertEqual(self.add_emp.PAGE_NAME, self.add_emp.get_header())
        self.add_emp.enter_employee_info(emp_id, first_name, last_name)
        self.add_emp.do_create_login_details()
        self.add_emp.enter_user_info(f'{first_name}_{emp_id}', last_name.upper())
        self.add_emp.do_save()
        self.assertEqual(self.personal_details.PAGE_NAME, self.personal_details.get_header())

        # self.assertEqual(first_name, self.personal_details.get_first_name())
        # self.assertEqual(last_name, self.personal_details.get_last_name())
        # self.assertEqual(emp_id, int(self.personal_details.get_employee_id()))
        # OR
        self.assertDictEqual({
            'first_name': first_name,
            'last_name': last_name,
            'employee_id': str(emp_id)
        }, self.personal_details.get_all_personal_info())
        # self.add_emp.do_save()

        # self.browser.find_element(By.ID, 'menu_admin_viewAdminModule').click()
        self.main_menu.open_admin()

        self.sys_user.do_user_search(f'{first_name}_{emp_id}')
        result_list = self.browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr//a')
        self.assertTrue(len(result_list) == 1)

        username = result_list[0].text
        self.assertEqual(f'{first_name}_{emp_id}', username)

        self.welcome_menu.logout()

        self.login_page.login(username, last_name.upper())

        self.assertEqual(f'Welcome {first_name}', self.welcome_menu.get_welcome_message())



if __name__ == '__main__':
    unittest.main()
