from pages.admin.login_page import LoginPage


def test_logout(opened_dashboard_page, driver, base_url):
    opened_dashboard_page.logout()
    login_page = LoginPage(driver, base_url)

    assert login_page.is_page_opened()
