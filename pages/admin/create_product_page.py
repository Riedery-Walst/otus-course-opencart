from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage


logger = create_logger(__name__)

class CreateProductPage(BasePage):
    PRODUCT_HEADER_NAME_1 = (By.ID, "product_header_name_1")
    SAVE_PRODUCT_BUTTON = (By.ID, "product_footer_save")
    CATALOG_PAGE = (By.ID, "subtab-AdminCatalog")
    CATALOG_LI = (By.ID, "subtab-AdminProducts")
    SUCCESSFUL_UPDATE_TEXT = (By.XPATH, '//*[text()="Successful update"]')

    def goto_products_page(self):
        logger.info("Go to Catalog page")
        self.click(self.CATALOG_PAGE)

        logger.info("Open Products list")
        self.click(self.CATALOG_LI)

    def set_product_name(self, product_name):
        logger.info(f"Set product name: {product_name}")
        element = self.find_element(self.PRODUCT_HEADER_NAME_1)
        element.send_keys(product_name)

    def save_product(self):
        logger.info("Click Save product button")
        self.click(self.SAVE_PRODUCT_BUTTON)

    def get_successful_text(self):
        logger.info("Check successful update message")
        return self.find_element(self.SUCCESSFUL_UPDATE_TEXT)