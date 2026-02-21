def test_is_page_open(main_page):
    assert main_page.is_page_opened()


def test_is_currency_exist(main_page):
    assert main_page.get_currency_selector().is_displayed()


def test_is_carousel_exist(main_page):
    assert main_page.get_carousel().is_displayed()


def test_is_random_product_exist(main_page):
    assert main_page.get_random_product().is_displayed()


def test_is_random_product_prise_exist(main_page):
    price = main_page.get_random_product_price()
    assert price.text.strip() != ""


def test_switch_product_currency_to_dollar(main_page):
    main_page.switch_currency_to_dollar()

    price = main_page.get_random_product()

    assert "$" in price.text
