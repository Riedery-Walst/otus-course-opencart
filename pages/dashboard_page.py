from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    TITLE = "Dashboard • PrestaShop"

    EMPLOYEE_BUTTON = (By.ID, "header_employee_box")
    LOGOUT_BUTTON = (By.ID, "header_logout")

    def get_employee_button(self):
        return self.find_element(self.EMPLOYEE_BUTTON)

    def get_logout_button(self):
        return self.find_element(self.LOGOUT_BUTTON)

    def logout(self):
        self.get_employee_button().click()
        self.get_logout_button().click()

        from pages.admin_login_page import AdminLoginPage
        return AdminLoginPage(self.driver, self.base_url)
