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
        logger.info("Получение селектора валюты")
        return self.find_element(self.CURRENCY_SELECTOR)

    @allure.step("Получить главный карусельный блок")
    def get_carousel(self):
        logger.info("Получение главного карусельного блока")
        return self.find_element(self.CAROUSEL)

    @allure.step("Открыть случайный продукт")
    def open_random_product(self):
        product = self.get_random_product()
        if product:
            logger.info("Открытие случайного продукта")
            product.click()
        else:
            logger.warning("На главной странице нет продуктов для открытия")

    @allure.step("Выбрать случайный продукт")
    def get_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        if products:
            product = random.choice(products)
            logger.info("Выбран случайный продукт")
            return product
        logger.warning("На главной странице нет доступных продуктов")
        return None

    @allure.step("Переключить валюту на доллар")
    def switch_currency_to_dollar(self):
        logger.info("Переключение валюты на доллар США")
        self.click(self.CURRENCY_SELECTOR)
        self.click(self.DOLLAR_LINK)
        logger.info("Валюта успешно переключена на доллар США")

    @allure.step("Получить цену случайного продукта")
    def get_random_product_price(self):
        product = self.get_random_product()
        if product:
            price_element = product.find_element(*self.PRODUCT_PRICE)
            logger.info(f"Цена выбранного случайного продукта: {price_element.text}")
            return price_element
        logger.warning("На главной странице нет продуктов для получения цены")
        return None

    @allure.step("Получить имя авторизованного пользователя")
    def get_user_name(self):
        user_name = self.find_element(self.USER_NAME_TEXT).text
        logger.info(f"Авторизованный пользователь: {user_name}")
        return user_name