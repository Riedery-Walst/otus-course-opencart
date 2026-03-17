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

    def get_employee_button(self):
        logger.info("Get employee button")
        return self.find_element(self.EMPLOYEE_BUTTON)

    def get_logout_button(self):
        logger.info("Get logout button")
        return self.find_element(self.LOGOUT_BUTTON)

    def logout(self):
        logger.info("Start logout process")

        self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_BUTTON))
        logger.info("Click employee menu")
        self.get_employee_button().click()

        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        logger.info("Click logout button")
        self.get_logout_button().click()

        logger.info("Logout completed")

    def goto_products_page(self):
        logger.info("Open Catalog section")
        self.click(self.CATALOG_PAGE)

        logger.info("Open Products page")
        self.click(self.CATALOG_LI)