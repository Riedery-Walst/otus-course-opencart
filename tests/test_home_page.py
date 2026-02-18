def test_is_page_open(home_page):
    assert home_page.is_page_opened()


def test_is_search_filters_exist(home_page):
    assert home_page.get_search_filters().is_displayed()


def test_is_search_filters_brands_exist(home_page):
    assert home_page.get_search_filters_brands().is_displayed()


def test_is_block_categories_exist(home_page):
    assert home_page.get_block_categories().is_displayed()


def test_is_random_product_exist(home_page):
    assert home_page.get_random_product().is_displayed()


def test_is_random_product_price_exist(home_page):
    price = home_page.get_random_product_price()
    assert price.text.strip() != ""

def test_switch_product_currency_to_dollar(main_page):
    main_page.switch_currency_to_dollar()

    price = main_page.get_random_product()

    assert "$" in price.text
