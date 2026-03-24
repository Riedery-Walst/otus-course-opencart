import allure
from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage

logger = create_logger(__name__)

class ProductsPage(BasePage):
    CREATE_PRODUCT_LINK = (By.ID, "page-header-desc-configuration-add")
    CREATE_PRODUCT_BUTTON = (By.ID, "create_product_create")
    DROPDOWN_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"dropdown-toggle-dots")])[1]')
    DELETE_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"grid-delete-row-link")])[1]')
    NEWEST_PRODUCT_NAME_TEXT = (By.XPATH, '(//*[contains(@class,"column-name")])[1]')
    CONFIRM_DELETE_BUTTON = (By.CLASS_NAME, 'btn-confirm-submit')

    @allure.step("Перейти на страницу создания продукта")
    def goto_create_product_page(self):
        logger.info("Переход на страницу создания продукта")
        self.wait_until_invisible((By.ID, "modal-create-product"))

        with allure.step("Нажать ссылку 'Добавить продукт'"):
            logger.info("Клик по ссылке 'Добавить продукт'")
            self.click(self.CREATE_PRODUCT_LINK)

        with allure.step("Дождаться появления модального окна"):
            logger.info("Ожидание появления модального окна создания продукта")
            self.wait_until_visible((By.ID, "modal-create-product"))

        with allure.step("Переключиться на iframe модального окна"):
            logger.info("Переключение на iframe модального окна создания продукта")
            self.switch_to_iframe((By.CSS_SELECTOR, "#modal-create-product iframe"))

        with allure.step("Нажать кнопку 'Создать продукт' внутри модального окна"):
            logger.info("Клик по кнопке 'Создать продукт' в модальном окне")
            self.click(self.CREATE_PRODUCT_BUTTON)

        with allure.step("Вернуться в основной контент страницы"):
            self.switch_to_default()
            logger.info("Возврат в основной контент страницы после создания продукта")

    @allure.step("Удалить последний созданный продукт")
    def delete_newest_product(self):
        logger.info("Удаление последнего созданного продукта")
        with allure.step("Открыть меню последнего продукта"):
            logger.info("Клик по меню последнего продукта")
            self.click(self.DROPDOWN_NEWEST_PRODUCT_BUTTON)
        with allure.step("Нажать кнопку удаления"):
            logger.info("Клик по кнопке удаления продукта")
            self.click(self.DELETE_NEWEST_PRODUCT_BUTTON)
        with allure.step("Подтвердить удаление"):
            logger.info("Подтверждение удаления продукта")
            self.click(self.CONFIRM_DELETE_BUTTON)
            logger.info("Удаление продукта подтверждено")

    @allure.step("Получить название последнего продукта")
    def get_newest_product_name(self):
        element = self.find_element(self.NEWEST_PRODUCT_NAME_TEXT)
        product_name = element.text
        logger.info(f"Название последнего продукта: {product_name}")
        return product_name