import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.admin_login_page import AdminLoginPage
from pages.main_page import MainPage
from pages.user_registration_page import UserRegistrationPage
from tests.logger import create_logger

logger = create_logger(__name__)

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        action="store",
        help="Select a browser driver",
    )
    parser.addoption(
        "--url",
        default="http://localhost:8081",
        action="store",
        help="Base URL",
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")

    driver = None

    match browser_name:
        case "chrome":
            driver = webdriver.Chrome()
        case "edge":
            driver = webdriver.Edge()
        case "firefox":
            driver = webdriver.Firefox()
        case _:
            pytest.fail(f"Unknown browser: {browser_name}")

    logger.info(f"Start browser: {browser_name}")

    yield driver

    logger.info(f"Close browser: {browser_name}")
    driver.quit()

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def main_page(driver, base_url):
    page = MainPage(driver, base_url)
    page.open()

    return page

@pytest.fixture
def home_page(driver, base_url):
    page = HomePage(driver, base_url)
    page.open()

    return page

@pytest.fixture
def product_page(driver, base_url):
    main_page = MainPage(driver, base_url)
    main_page.open()

    product_page = main_page.open_random_product()

    return product_page

@pytest.fixture
def admin_login_page(driver, base_url):
    page = AdminLoginPage(driver, base_url)
    page.open()

    return page

@pytest.fixture
def user_registration_page(driver, base_url):
    page = UserRegistrationPage(driver, base_url)
    page.open()

    return page

@pytest.fixture
def dashboard_page(driver, base_url):
    login_page = AdminLoginPage(driver, base_url)
    login_page.open()

    dashboard_page = login_page.login()

    return dashboard_page