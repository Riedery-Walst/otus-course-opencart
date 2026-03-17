def test_product_page_elements(opened_product_page):
    assert opened_product_page.get_product_name()
    assert opened_product_page.get_product_price()
    assert opened_product_page.get_add_to_cart_button()
    assert opened_product_page.get_product_quantity()
    assert opened_product_page.get_product_image()

def test_add_product_to_cart(opened_product_page):
    add_to_cart = opened_product_page.get_add_to_cart_button()

    add_to_cart.click()

    assert opened_product_page.get_proceed_to_checkout_button().is_displayed()