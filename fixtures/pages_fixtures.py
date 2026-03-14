import pytest

from pages.admin.create_product_page import CreateProductPage
from pages.admin.dashboard_page import DashboardPage
from pages.admin.login_page import LoginPage
from pages.admin.products_page import ProductsPage
from pages.user.home_page import HomePage
from pages.user.main_page import MainPage
from pages.user.product_page import ProductPage
from pages.user.registration_page import RegistrationPage


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

    product_page = ProductPage(driver, base_url)
    main_page.open_random_product()

    return product_page


@pytest.fixture
def user_registration_page(driver, base_url):
    page = RegistrationPage(driver, base_url)
    page.open()

    return page


@pytest.fixture
def admin_login_page(driver, base_url):
    page = LoginPage(driver, base_url)
    page.open()

    return page


@pytest.fixture
def dashboard_page(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login()

    dashboard_page = DashboardPage(driver, base_url)

    return dashboard_page


@pytest.fixture
def products_page(dashboard_page, driver, base_url):
    dashboard_page.goto_products_page()

    page = ProductsPage(driver, base_url)

    return page


@pytest.fixture
def create_product_page(products_page, driver, base_url):
    products_page.goto_create_product_page()

    page = CreateProductPage(driver, base_url)

    return page
