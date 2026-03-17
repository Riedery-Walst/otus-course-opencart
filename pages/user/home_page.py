import random

from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage


logger = create_logger(__name__)

class HomePage(BasePage):
    TITLE = "Home"
    PATH = "/2-home"

    SEARCH_FILTERS = (By.ID, "search_filters")
    SEARCH_FILTERS_BRANDS = (By.ID, "search_filters_brands")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")
    BLOCK_CATEGORIES = (By.CSS_SELECTOR, ".block-categories")
    PRODUCTS = (By.CSS_SELECTOR, ".products .thumbnail-container")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price")

    def get_block_categories(self):
        logger.info("Get categories block")
        return self.find_element(self.BLOCK_CATEGORIES)

    def get_search_filters(self):
        logger.info("Get search filters block")
        return self.find_element(self.SEARCH_FILTERS)

    def get_add_to_cart_button(self):
        logger.info("Get 'Add to Cart' button")
        return self.find_element(self.ADD_TO_CART_BUTTON)

    def get_search_filters_brands(self):
        logger.info("Get search filters brands block")
        return self.find_element(self.SEARCH_FILTERS_BRANDS)

    def get_random_product_price(self):
        product = self.get_random_product()
        if product:
            price_element = product.find_element(*self.PRODUCT_PRICE)
            logger.info(f"Random product price found: {price_element.text}")
            return price_element
        logger.warning("No products found to get price")
        return None

    def get_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        if products:
            product = random.choice(products)
            logger.info(f"Random product selected")
            return product
        logger.warning("No products found on page")
        return None