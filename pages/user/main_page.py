import random
import allure
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

    @allure.step("Получить селектор валюты")
    def get_currency_selector(self):
        return self.find_element(self.CURRENCY_SELECTOR)

    @allure.step("Получить главный карусельный блок")
    def get_carousel(self):
        return self.find_element(self.CAROUSEL)

    @allure.step("Открыть случайный продукт")
    def open_random_product(self):
        product = self.get_random_product()
        product.click()

    @allure.step("Выбрать случайный продукт")
    def get_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        return random.choice(products)

    @allure.step("Переключить валюту на доллар")
    def switch_currency_to_dollar(self):
        self.click(self.CURRENCY_SELECTOR)
        self.click(self.DOLLAR_LINK)

    @allure.step("Получить цену случайного продукта")
    def get_random_product_price(self):
        product = self.get_random_product()
        return product.find_element(*self.PRODUCT_PRICE)

    @allure.step("Получить имя авторизованного пользователя")
    def get_user_name(self):
        user_name = self.find_element(self.USER_NAME_TEXT).text
        return user_name