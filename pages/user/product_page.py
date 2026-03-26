import allure
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

    @allure.step("Получить название продукта")
    def get_product_name(self):
        element = self.find_element(self.PRODUCT_NAME)
        return element

    @allure.step("Получить цену продукта")
    def get_product_price(self):
        element = self.find_element(self.PRODUCT_PRICE)
        return element

    @allure.step("Получить кнопку 'Добавить в корзину'")
    def get_add_to_cart_button(self):
        return self.find_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Получить кнопку 'Перейти к оформлению заказа'")
    def get_proceed_to_checkout_button(self):
        return self.find_element(self.PROCEED_TO_CHECKOUT_BUTTON)

    @allure.step("Получить описание продукта")
    def get_product_image(self):
        return self.find_element(self.PRODUCT_DESCRIPTION)

    @allure.step("Получить количество продукта")
    def get_product_quantity(self):
        element = self.find_element(self.PRODUCT_QUANTITY)
        return element