import allure
from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage

logger = create_logger(__name__)

class CreateProductPage(BasePage):
    PRODUCT_HEADER_NAME_1 = (By.ID, "product_header_name_1")
    SAVE_PRODUCT_BUTTON = (By.ID, "product_footer_save")
    CATALOG_PAGE = (By.ID, "subtab-AdminCatalog")
    CATALOG_LI = (By.ID, "subtab-AdminProducts")
    SUCCESSFUL_UPDATE_TEXT = (By.XPATH, '//*[text()="Successful update"]')

    @allure.step("Перейти на страницу продуктов")
    def goto_products_page(self):
        logger.info("Переход на страницу Каталог")
        self.click(self.CATALOG_PAGE)

        logger.info("Открытие списка продуктов")
        self.click(self.CATALOG_LI)

    @allure.step("Установить название продукта")
    def set_product_name(self, product_name):
        logger.info(f"Установка названия продукта: {product_name}")
        element = self.find_element(self.PRODUCT_HEADER_NAME_1)
        element.clear()
        element.send_keys(product_name)

    @allure.step("Сохранить продукт")
    def save_product(self):
        logger.info("Клик по кнопке 'Сохранить продукт'")
        self.click(self.SAVE_PRODUCT_BUTTON)

    @allure.step("Проверить сообщение об успешном обновлении")
    def get_successful_text(self):
        logger.info("Проверка сообщения об успешном обновлении")
        return self.find_element(self.SUCCESSFUL_UPDATE_TEXT)