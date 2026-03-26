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
        self.wait_until_invisible((By.ID, "modal-create-product"))

        with allure.step("Нажать ссылку 'Добавить продукт'"):
            self.click(self.CREATE_PRODUCT_LINK)

        with allure.step("Дождаться появления модального окна"):
            self.wait_until_visible((By.ID, "modal-create-product"))

        with allure.step("Переключиться на iframe модального окна"):
            self.switch_to_iframe((By.CSS_SELECTOR, "#modal-create-product iframe"))

        with allure.step("Нажать кнопку 'Создать продукт' внутри модального окна"):
            self.click(self.CREATE_PRODUCT_BUTTON)

        with allure.step("Вернуться в основной контент страницы"):
            self.switch_to_default()

    @allure.step("Удалить последний созданный продукт")
    def delete_newest_product(self):
        with allure.step("Открыть меню последнего продукта"):
            self.click(self.DROPDOWN_NEWEST_PRODUCT_BUTTON)
        with allure.step("Нажать кнопку удаления"):
            self.click(self.DELETE_NEWEST_PRODUCT_BUTTON)
        with allure.step("Подтвердить удаление"):
            self.click(self.CONFIRM_DELETE_BUTTON)

    @allure.step("Получить название последнего продукта")
    def get_newest_product_name(self):
        element = self.find_element(self.NEWEST_PRODUCT_NAME_TEXT)
        product_name = element.text
        return product_name