from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage

logger = create_logger(__name__)

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#main h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "current-price-value")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".product-description p")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".cart-content a")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    PRODUCT_QUANTITY = (By.ID, "quantity_wanted")

    def get_product_name(self):
        element = self.find_element(self.PRODUCT_NAME)
        logger.info(f"Product name: {element.text}")
        return element

    def get_product_price(self):
        element = self.find_element(self.PRODUCT_PRICE)
        logger.info(f"Product price: {element.text}")
        return element

    def get_add_to_cart_button(self):
        logger.info("Get 'Add to Cart' button")
        return self.find_element(self.ADD_TO_CART_BUTTON)

    def get_proceed_to_checkout_button(self):
        logger.info("Get 'Proceed to Checkout' button")
        return self.find_element(self.PROCEED_TO_CHECKOUT_BUTTON)

    def get_product_image(self):
        logger.info("Get product description block")
        return self.find_element(self.PRODUCT_DESCRIPTION)

    def get_product_quantity(self):
        element = self.find_element(self.PRODUCT_QUANTITY)
        logger.info(f"Product quantity field value: {element.get_attribute('value')}")
        return element