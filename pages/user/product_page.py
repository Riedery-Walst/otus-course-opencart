from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#main h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "current-price-value")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".product-description p")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".cart-content a")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    PRODUCT_QUANTITY = (By.ID, "quantity_wanted")

    def get_product_name(self):
        return self.find_element(self.PRODUCT_NAME)

    def get_product_price(self):
        return self.find_element(self.PRODUCT_PRICE)

    def get_add_to_cart_button(self):
        return self.find_element(self.ADD_TO_CART_BUTTON)

    def get_proceed_to_checkout_button(self):
        return self.find_element(self.PROCEED_TO_CHECKOUT_BUTTON)

    def get_product_image(self):
        return self.find_element(self.PRODUCT_DESCRIPTION)

    def get_product_quantity(self):
        return self.find_element(self.PRODUCT_QUANTITY)
