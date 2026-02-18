def test_is_page_open(admin_login_page):
    assert admin_login_page.is_page_opened()


def test_is_submit_button_exist(admin_login_page):
    assert admin_login_page.get_submit_button().is_displayed()


def test_is_email_form_exist(admin_login_page):
    assert admin_login_page.get_submit_button().is_displayed()


def test_is_password_form_exist(admin_login_page):
    assert admin_login_page.get_password_form().is_displayed()


def test_is_shop_image_exist(admin_login_page):
    assert admin_login_page.get_shop_image().is_displayed()


def test_is_stay_logged_in_checkbox_exist(admin_login_page):
    assert admin_login_page.get_stay_logged_in_checkbox().is_displayed()


def test_login(dashboard_page):
    assert dashboard_page.is_page_opened()
