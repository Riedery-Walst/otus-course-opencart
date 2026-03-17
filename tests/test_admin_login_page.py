def test_login_page_elements(opened_admin_login_page):
    assert opened_admin_login_page.is_page_opened()
    assert opened_admin_login_page.get_email_form().is_displayed()
    assert opened_admin_login_page.get_password_form().is_displayed()
    assert opened_admin_login_page.get_submit_button().is_displayed()
    assert opened_admin_login_page.get_shop_image().is_displayed()
    assert opened_admin_login_page.get_stay_logged_in_checkbox().is_displayed()