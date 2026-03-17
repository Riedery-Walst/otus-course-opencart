from faker import Faker

from conftest import driver
from pages.user.main_page import MainPage


def test_registration_page_elements(opened_user_registration_page):
    assert opened_user_registration_page.is_page_opened()
    assert opened_user_registration_page.get_firstname_field().is_displayed()
    assert opened_user_registration_page.get_lastname_field().is_displayed()
    assert opened_user_registration_page.get_email_field().is_displayed()
    assert opened_user_registration_page.get_password_field().is_displayed()
    assert opened_user_registration_page.get_birthdate_field().is_displayed()


def register_new_user(user_registration_page, driver):
    fake = Faker()

    name = fake.name()
    last_name = fake.last_name()

    user_registration_page.get_firstname_field.send_keys(name)
    user_registration_page.get_lastname_field.send_keys(last_name)
    user_registration_page.get_email_field.send_keys(fake.email())
    user_registration_page.get_password_field.send_keys(fake.password())
    user_registration_page.get_birthdate_field.send_keys(fake.date())
    user_registration_page.fill_terms_amd_conditions_checkbox()
    user_registration_page.fill_customer_privacy_checkbox()

    page = MainPage(driver)

    assert page.get_user_name() == name + " " + last_name