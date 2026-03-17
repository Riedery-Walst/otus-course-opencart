import pytest


@pytest.mark.parametrize("product_name", ["Deleted Test Product"])
def test_delete_product_page(opened_create_product_page, product_name, products_page):
    opened_create_product_page.set_product_name(product_name)
    opened_create_product_page.save_product()

    opened_create_product_page.goto_products_page()

    products_page.delete_newest_product()

    assert products_page.get_newest_product_name() != product_name