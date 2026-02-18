from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserRegistrationPage(BasePage):
    TITLE = "Registration"

    PATH = "/registration"

    FIRSTNAME_FIELD = (By.ID, "field-firstname")
    LASTNAME_FIELD = (By.ID, "field-lastname")
    EMAIL_FIELD = (By.ID, "field-email")
    PASSWORD_FIELD = (By.ID, "field-password")
    BIRTHDATE_FIELD = (By.ID, "field-birthday")

    def get_firstname_field(self):
        return self.find_element(self.FIRSTNAME_FIELD)

    def get_lastname_field(self):
        return self.find_element(self.LASTNAME_FIELD)

    def get_email_field(self):
        return self.find_element(self.EMAIL_FIELD)

    def get_password_field(self):
        return self.find_element(self.PASSWORD_FIELD)

    def get_birthdate_field(self):
        return self.find_element(self.BIRTHDATE_FIELD)
