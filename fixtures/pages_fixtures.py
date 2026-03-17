import pytest

from pages.admin.create_product_page import CreateProductPage
from pages.admin.dashboard_page import DashboardPage
from pages.admin.login_page import LoginPage
from pages.admin.products_page import ProductsPage
from pages.base_page import BasePage
from pages.user.home_page import HomePage
from pages.user.main_page import MainPage
from pages.user.product_page import ProductPage
from pages.user.registration_page import RegistrationPage


@pytest.fixture(autouse=True, scope="session")
def set_base_url(request):
    BasePage.BASE_URL = request.config.getoption("--url")


@pytest.fixture
def opened_main_page(driver):
    return MainPage(driver).open()


@pytest.fixture
def opened_home_page(driver):
    return HomePage(driver).open()


@pytest.fixture
def opened_product_page(driver):
    main_page = MainPage(driver).open()
    main_page.open_random_product()
    return ProductPage(driver)


@pytest.fixture
def opened_user_registration_page(driver):
    return RegistrationPage(driver).open()


@pytest.fixture
def opened_admin_login_page(driver):
    return LoginPage(driver).open()


@pytest.fixture
def opened_dashboard_page(driver):
    page = LoginPage(driver).open()
    page.login()
    return DashboardPage(driver)


@pytest.fixture
def products_page(opened_dashboard_page, driver):
    opened_dashboard_page.goto_products_page()
    return ProductsPage(driver)


@pytest.fixture
def opened_create_product_page(products_page, driver):
    products_page.goto_create_product_page()
    return CreateProductPage(driver)