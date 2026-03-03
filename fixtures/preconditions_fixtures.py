import pytest

from pages.admin_pages.products_page import ProductsPage


@pytest.fixture(params=["Test product"])
def product(create_product_page, request, driver, base_url, dashboard_page):
    product_name = request.param
    create_product_page.set_product_name(product_name)
    create_product_page.save_product()

    yield product_name

    dashboard_page.goto_products_page()
    page = ProductsPage(driver, base_url)
    page.delete_newest_product()