import allure
from pages.admin.login_page import LoginPage

@allure.feature("Панель администратора")
@allure.story("Выход из системы")
@allure.title("Тест выхода из панели администратора")
def test_logout(opened_dashboard_page, driver):
    opened_dashboard_page.logout()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "Страница логина не открыта после выхода"