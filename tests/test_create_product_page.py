import pytest


@pytest.mark.parametrize("product_name", ["Created Test Product"])
def test_create_product(create_product_page, product_name, products_page):
    create_product_page.set_product_name(product_name)
    create_product_page.save_product()

    create_product_page.goto_products_page()

    assert products_page.get_newest_product_name() == product_name