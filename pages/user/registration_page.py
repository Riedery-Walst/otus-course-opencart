from selenium.webdriver.common.by import By

from logger import create_logger
from pages.base_page import BasePage


logger = create_logger(__name__)

class RegistrationPage(BasePage):
    TITLE = "Registration"
    PATH = "/registration"

    FIRSTNAME_FIELD = (By.ID, "field-firstname")
    LASTNAME_FIELD = (By.ID, "field-lastname")
    EMAIL_FIELD = (By.ID, "field-email")
    PASSWORD_FIELD = (By.ID, "field-password")
    BIRTHDATE_FIELD = (By.ID, "field-birthday")
    TERMS_AMD_CONDITIONS_CHECKBOX = (By.XPATH, '//*[@name="psgdpr"]')
    CUSTOMER_PRIVACY_CHECKBOX = (By.XPATH, '//*[@name="customer_privacy"]')
    FORM_SUBMIT_BUTTON = (By.CLASS_NAME, 'form-control-submit')

    def get_firstname_field(self):
        logger.info("Get first name field")
        return self.find_element(self.FIRSTNAME_FIELD)

    def get_lastname_field(self):
        logger.info("Get last name field")
        return self.find_element(self.LASTNAME_FIELD)

    def get_email_field(self):
        logger.info("Get email field")
        return self.find_element(self.EMAIL_FIELD)

    def get_password_field(self):
        logger.info("Get password field")
        return self.find_element(self.PASSWORD_FIELD)

    def get_birthdate_field(self):
        logger.info("Get birthdate field")
        return self.find_element(self.BIRTHDATE_FIELD)

    def fill_terms_amd_conditions_checkbox(self):
        logger.info("Click 'Terms and Conditions' checkbox")
        self.click(self.TERMS_AMD_CONDITIONS_CHECKBOX)

    def fill_customer_privacy_checkbox(self):
        logger.info("Click 'Customer Privacy' checkbox")
        self.click(self.CUSTOMER_PRIVACY_CHECKBOX)

    def register_new_user(self):
        logger.info("Submit registration form")
        self.click(self.FORM_SUBMIT_BUTTON)
        logger.info("Registration form submitted")

    def register_new_user(self):
        self.click(self.FORM_SUBMIT_BUTTON)
