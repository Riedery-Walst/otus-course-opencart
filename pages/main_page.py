import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class MainPage(BasePage):
    TITLE = "PrestaShop"

    PATH = ""

    CAROUSEL = (By.ID, "carousel")
    PRODUCTS = (By.CSS_SELECTOR, ".featured-products .product-miniature")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price")
    CURRENCY_SELECTOR = (By.XPATH, '//*[@aria-label="Currency dropdown"]')
    DOLLAR_LINK = (By.XPATH, '//a[@title="US Dollar"]')

    def get_currency_selector(self):
        return self.find_element(self.CURRENCY_SELECTOR)

    def get_carousel(self):
        return self.find_element(self.CAROUSEL)

    def open_random_product(self):
        product = self.get_random_product()
        product.click()

        return ProductPage(self.driver, self.base_url)

    def get_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        return random.choice(products) if products else None

    def switch_currency_to_dollar(self):
        self.click(self.CURRENCY_SELECTOR)
        self.click(self.DOLLAR_LINK)

    def get_random_product_price(self):
        product = self.get_random_product()

        return product.find_element(*self.PRODUCT_PRICE)
