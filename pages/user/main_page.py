import random

from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage


logger = create_logger(__name__)

class MainPage(BasePage):
    TITLE = "PrestaShop"
    PATH = ""

    CAROUSEL = (By.ID, "carousel")
    PRODUCTS = (By.CSS_SELECTOR, ".featured-products .product-miniature")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price")
    CURRENCY_SELECTOR = (By.XPATH, '//*[@aria-label="Currency dropdown"]')
    DOLLAR_LINK = (By.XPATH, '//a[@title="US Dollar"]')
    USER_NAME_TEXT = (By.CSS_SELECTOR, '.account')

    def get_currency_selector(self):
        logger.info("Get currency selector")
        return self.find_element(self.CURRENCY_SELECTOR)

    def get_carousel(self):
        logger.info("Get main carousel")
        return self.find_element(self.CAROUSEL)

    def open_random_product(self):
        product = self.get_random_product()
        if product:
            logger.info("Opening random product")
            product.click()
        else:
            logger.warning("No products found to open")

    def get_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        if products:
            product = random.choice(products)
            logger.info("Random product selected")
            return product
        logger.warning("No products available on main page")
        return None

    def switch_currency_to_dollar(self):
        logger.info("Switching currency to US Dollar")
        self.click(self.CURRENCY_SELECTOR)
        self.click(self.DOLLAR_LINK)
        logger.info("Currency switched to US Dollar")

    def get_random_product_price(self):
        product = self.get_random_product()
        if product:
            price_element = product.find_element(*self.PRODUCT_PRICE)
            logger.info(f"Random product price: {price_element.text}")
            return price_element
        logger.warning("No products found to get price")
        return None

    def get_user_name(self):
        user_name = self.find_element(self.USER_NAME_TEXT).text
        logger.info(f"Logged in user: {user_name}")
        return user_name