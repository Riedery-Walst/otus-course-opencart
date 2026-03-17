from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage


logger = create_logger(__name__)

class ProductsPage(BasePage):
    CREATE_PRODUCT_LINK = (By.ID, "page-header-desc-configuration-add")
    CREATE_PRODUCT_BUTTON = (By.ID, "create_product_create")
    DROPDOWN_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"dropdown-toggle-dots")])[1]')
    DELETE_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"grid-delete-row-link")])[1]')
    NEWEST_PRODUCT_NAME_TEXT = (By.XPATH, '(//*[contains(@class,"column-name")])[1]')
    CONFIRM_DELETE_BUTTON = (By.CLASS_NAME, 'btn-confirm-submit')

    def goto_create_product_page(self):
        logger.info("Go to Create Product page")
        self.wait_until_invisible((By.ID, "modal-create-product"))

        logger.info("Click 'Add Product' link")
        self.click(self.CREATE_PRODUCT_LINK)

        self.wait_until_visible((By.ID, "modal-create-product"))

        logger.info("Switch to Create Product modal iframe")
        self.switch_to_iframe((By.CSS_SELECTOR, "#modal-create-product iframe"))

        logger.info("Click 'Create Product' button inside modal")
        self.click(self.CREATE_PRODUCT_BUTTON)

        self.switch_to_default()
        logger.info("Switched back to default content after creating product")

    def delete_newest_product(self):
        logger.info("Delete newest product")
        self.click(self.DROPDOWN_NEWEST_PRODUCT_BUTTON)
        self.click(self.DELETE_NEWEST_PRODUCT_BUTTON)
        self.click(self.CONFIRM_DELETE_BUTTON)
        logger.info("Confirmed product deletion")

    def get_newest_product_name(self):
        element = self.find_element(self.NEWEST_PRODUCT_NAME_TEXT)
        product_name = element.text
        logger.info(f"Newest product name: {product_name}")
        return product_name