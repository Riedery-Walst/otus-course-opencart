import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage

logger = create_logger(__name__)

class DashboardPage(BasePage):
    TITLE = "Dashboard • PrestaShop"

    EMPLOYEE_BUTTON = (By.ID, "header_employee_box")
    LOGOUT_BUTTON = (By.ID, "header_logout")
    CATALOG_PAGE = (By.ID, "subtab-AdminCatalog")
    CATALOG_LI = (By.ID, "subtab-AdminProducts")

    @allure.step("Получить кнопку сотрудника")
    def get_employee_button(self):
        return self.find_element(self.EMPLOYEE_BUTTON)

    @allure.step("Получить кнопку выхода")
    def get_logout_button(self):
        return self.find_element(self.LOGOUT_BUTTON)

    @allure.step("Выйти из панели администратора")
    def logout(self):
        self.find_element(self.EMPLOYEE_BUTTON)
        self.get_employee_button().click()

        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        self.get_logout_button().click()

    @allure.step("Перейти на страницу продуктов")
    def goto_products_page(self):
        self.click(self.CATALOG_PAGE)
        self.click(self.CATALOG_LI)