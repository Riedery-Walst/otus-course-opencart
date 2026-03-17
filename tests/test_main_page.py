def test_main_page_elements(opened_main_page):
    assert opened_main_page.is_page_opened()
    assert opened_main_page.get_currency_selector().is_displayed()
    assert opened_main_page.get_carousel().is_displayed()

    product = opened_main_page.get_random_product()
    assert product is not None and product.is_displayed()

    price = opened_main_page.get_random_product_price()
    assert price is not None and price.text.strip() != ""


def test_switch_product_currency_to_dollar(opened_main_page):
    opened_main_page.switch_currency_to_dollar()

    price = opened_main_page.get_random_product()

    assert "$" in price.text
