import allure
from faker import Faker
from pages.user.main_page import MainPage

@allure.feature("Регистрация пользователя")
@allure.story("Проверка элементов страницы регистрации")
@allure.title("Тест отображения элементов страницы регистрации")
def test_registration_page_elements(opened_user_registration_page):
    assert opened_user_registration_page.get_firstname_field().is_displayed()
    assert opened_user_registration_page.get_lastname_field().is_displayed()
    assert opened_user_registration_page.get_email_field().is_displayed()
    assert opened_user_registration_page.get_password_field().is_displayed()
    assert opened_user_registration_page.get_birthdate_field().is_displayed()


@allure.feature("Регистрация пользователя")
@allure.story("Создание нового пользователя")
@allure.title("Тест успешной регистрации нового пользователя")
def test_register_new_user(opened_user_registration_page, driver):
    fake = Faker()
    name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    birthdate = fake.date()

    opened_user_registration_page.get_firstname_field().send_keys(name)
    opened_user_registration_page.get_lastname_field().send_keys(last_name)
    opened_user_registration_page.get_email_field().send_keys(email)
    opened_user_registration_page.get_password_field().send_keys(password)
    opened_user_registration_page.get_birthdate_field().send_keys(birthdate)
    opened_user_registration_page.fill_terms_and_conditions_checkbox()
    opened_user_registration_page.fill_customer_privacy_checkbox()
    opened_user_registration_page.register_new_user()

    page = MainPage(driver)
    assert page.get_user_name() == f"{name} {last_name}"