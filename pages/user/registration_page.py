import allure
from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage

logger = create_logger(__name__)

class RegistrationPage(BasePage):
    TITLE = "Регистрация"
    PATH = "/registration"

    FIRSTNAME_FIELD = (By.ID, "field-firstname")
    LASTNAME_FIELD = (By.ID, "field-lastname")
    EMAIL_FIELD = (By.ID, "field-email")
    PASSWORD_FIELD = (By.ID, "field-password")
    BIRTHDATE_FIELD = (By.ID, "field-birthday")
    TERMS_AND_CONDITIONS_CHECKBOX = (By.XPATH, '//*[@name="psgdpr"]/ancestor::label')
    CUSTOMER_PRIVACY_CHECKBOX = (By.XPATH, '//*[@name="customer_privacy"]/ancestor::label')
    FORM_SUBMIT_BUTTON = (By.CLASS_NAME, 'form-control-submit')

    @allure.step("Получить поле 'Имя'")
    def get_firstname_field(self):
        logger.info("Получение поля 'Имя'")
        return self.find_element(self.FIRSTNAME_FIELD)

    @allure.step("Получить поле 'Фамилия'")
    def get_lastname_field(self):
        logger.info("Получение поля 'Фамилия'")
        return self.find_element(self.LASTNAME_FIELD)

    @allure.step("Получить поле 'Email'")
    def get_email_field(self):
        logger.info("Получение поля 'Email'")
        return self.find_element(self.EMAIL_FIELD)

    @allure.step("Получить поле 'Пароль'")
    def get_password_field(self):
        logger.info("Получение поля 'Пароль'")
        return self.find_element(self.PASSWORD_FIELD)

    @allure.step("Получить поле 'Дата рождения'")
    def get_birthdate_field(self):
        logger.info("Получение поля 'Дата рождения'")
        return self.find_element(self.BIRTHDATE_FIELD)

    @allure.step("Отметить чекбокс 'Согласие с условиями'")
    def fill_terms_and_conditions_checkbox(self):
        logger.info("Клик по чекбоксу 'Согласие с условиями'")
        self.click(self.TERMS_AND_CONDITIONS_CHECKBOX)

    @allure.step("Отметить чекбокс 'Конфиденциальность клиента'")
    def fill_customer_privacy_checkbox(self):
        logger.info("Клик по чекбоксу 'Конфиденциальность клиента'")
        self.click(self.CUSTOMER_PRIVACY_CHECKBOX)

    @allure.step("Отправить форму регистрации")
    def register_new_user(self):
        logger.info("Отправка формы регистрации")
        self.click(self.FORM_SUBMIT_BUTTON)
        logger.info("Форма регистрации отправлена")