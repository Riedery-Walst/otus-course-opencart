def test_is_page_open(product_page):
    assert product_page.get_product_name()


def test_is_product_name_present(product_page):
    assert product_page.get_product_name()


def test_is_product_price_present(product_page):
    assert product_page.get_product_price()


def test_is_add_to_cart_button_present(product_page):
    assert product_page.get_add_to_cart_button()


def test_is_product_quantity_present(product_page):
    assert product_page.get_product_quantity()


def test_is_product_image_present(product_page):
    assert product_page.get_product_image()


def test_add_product_to_cart(product_page):
    add_to_cart = product_page.get_add_to_cart_button()

    add_to_cart.click()

    assert product_page.get_proceed_to_checkout_button().is_displayed()