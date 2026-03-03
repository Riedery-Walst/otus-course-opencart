def test_create_product(product, create_product_page):
    assert create_product_page.get_successful_text().is_displayed()