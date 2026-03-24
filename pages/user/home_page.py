import random
import allure
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

    @allure.step("Получить блок категорий")
    def get_block_categories(self):
        logger.info("Получение блока категорий")
        return self.find_element(self.BLOCK_CATEGORIES)

    @allure.step("Получить блок фильтров поиска")
    def get_search_filters(self):
        logger.info("Получение блока фильтров поиска")
        return self.find_element(self.SEARCH_FILTERS)

    @allure.step("Получить кнопку 'Добавить в корзину'")
    def get_add_to_cart_button(self):
        logger.info("Получение кнопки 'Добавить в корзину'")
        return self.find_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Получить блок брендов в фильтрах поиска")
    def get_search_filters_brands(self):
        logger.info("Получение блока брендов в фильтрах поиска")
        return self.find_element(self.SEARCH_FILTERS_BRANDS)

    @allure.step("Получить цену случайного продукта")
    def get_random_product_price(self):
        product = self.get_random_product()
        if product:
            price_element = product.find_element(*self.PRODUCT_PRICE)
            logger.info(f"Цена выбранного случайного продукта: {price_element.text}")
            return price_element
        logger.warning("На странице нет продуктов для получения цены")
        return None

    @allure.step("Выбрать случайный продукт")
    def get_random_product(self):
        products = self.find_elements(self.PRODUCTS)
        if products:
            product = random.choice(products)
            logger.info("Выбран случайный продукт")
            return product
        logger.warning("На странице нет продуктов")
        return None