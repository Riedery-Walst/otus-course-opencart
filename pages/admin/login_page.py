import allure
from selenium.webdriver.common.by import By

import config
from logger import create_logger
from pages.base_page import BasePage

logger = create_logger(__name__)

class LoginPage(BasePage):
    TITLE = "PrestaShop"
    PATH = "/administration/login"

    SUBMIT_BUTTON = (By.ID, "submit_login")
    EMAIL_FORM = (By.ID, "email")
    PASSWORD_FORM = (By.ID, "passwd")
    SHOP_IMAGE = (By.ID, "shop-img")
    STAY_LOGGED_IN_CHECKBOX = (By.CLASS_NAME, "form-check")

    @allure.step("Получить кнопку входа")
    def get_submit_button(self):
        return self.find_element(self.SUBMIT_BUTTON)

    @allure.step("Получить поле Email")
    def get_email_form(self):
        return self.find_element(self.EMAIL_FORM)

    @allure.step("Получить поле Password")
    def get_password_form(self):
        return self.find_element(self.PASSWORD_FORM)

    @allure.step("Получить изображение магазина")
    def get_shop_image(self):
        return self.find_element(self.SHOP_IMAGE)

    @allure.step("Получить чекбокс 'Оставаться в системе'")
    def get_stay_logged_in_checkbox(self):
        return self.find_element(self.STAY_LOGGED_IN_CHECKBOX)

    @allure.step("Войти в систему под пользователем")
    def login(self):
        logger.info(f"Вход в систему под пользователем {config.ADMIN_EMAIL}")

        with allure.step("Ввод Email"):
            email = self.get_email_form()
            email.send_keys(config.ADMIN_EMAIL)
            logger.info("Email введён")

        with allure.step("Ввод пароля"):
            password = self.get_password_form()
            password.send_keys(config.ADMIN_PASSWORD)
            logger.info("Пароль введён")

        with allure.step("Нажать кнопку входа"):
            logger.info("Клик по кнопке входа")
            self.click(self.SUBMIT_BUTTON)
            logger.info("Вход выполнен")