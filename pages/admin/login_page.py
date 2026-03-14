from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.base_page import BasePage


class LoginPage(BasePage):
    TITLE = "PrestaShop"

    PATH = "/administration/login"

    SUBMIT_BUTTON = (By.ID, "submit_login")
    EMAIL_FORM = (By.ID, "email")
    PASSWORD_FORM = (By.ID, "passwd")
    SHOP_IMAGE = (By.ID, "shop-img")
    STAY_LOGGED_IN_CHECKBOX = (By.CLASS_NAME, "form-check")

    def get_submit_button(self):
        return self.find_element(self.SUBMIT_BUTTON)

    def get_email_form(self):
        return self.find_element(self.EMAIL_FORM)

    def get_password_form(self):
        return self.find_element(self.PASSWORD_FORM)

    def get_shop_image(self):
        return self.find_element(self.SHOP_IMAGE)

    def get_stay_logged_in_checkbox(self):
        return self.find_element(self.STAY_LOGGED_IN_CHECKBOX)

    def login(self):
        email = self.get_email_form()
        email.send_keys(config.ADMIN_EMAIL)

        password = self.get_password_form()
        password.send_keys(config.ADMIN_PASSWORD)

        self.click(self.SUBMIT_BUTTON)