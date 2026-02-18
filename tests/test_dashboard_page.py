def test_logout(dashboard_page):
    login_page = dashboard_page.logout()

    assert login_page.is_page_opened()
