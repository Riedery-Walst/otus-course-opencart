import faker
import pytest
from faker import Faker

from conftest import driver
from pages.user.main_page import MainPage


def test_is_page_open(user_registration_page):
    assert user_registration_page.is_page_opened()


def test_is_firstname_field_exist(user_registration_page):
    assert user_registration_page.get_firstname_field().is_displayed()


def test_is_lastname_field_exist(user_registration_page):
    assert user_registration_page.get_lastname_field().is_displayed()


def test_is_email_field_exist(user_registration_page):
    assert user_registration_page.get_email_field().is_displayed()


def test_is_password_field_exist(user_registration_page):
    assert user_registration_page.get_password_field().is_displayed()


def test_is_birthdate_field_exist(user_registration_page):
    assert user_registration_page.get_birthdate_field().is_displayed()


def register_new_user(user_registration_page, driver, base_url):
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

    page = MainPage(driver, base_url)

    assert page.get_user_name() == name + " " + last_name