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
