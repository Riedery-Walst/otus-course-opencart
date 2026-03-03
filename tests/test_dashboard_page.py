from pages.admin_pages.login_page import LoginPage


def test_logout(dashboard_page, driver, base_url):
    dashboard_page.logout()
    login_page = LoginPage(driver, base_url)

    assert login_page.is_page_opened()
