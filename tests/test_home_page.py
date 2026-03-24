import allure

@allure.feature("Главная страница")
@allure.story("Проверка элементов")
@allure.title("Тест отображения элементов главной страницы")
def test_home_page_elements(opened_home_page):
    assert opened_home_page.is_page_opened(), "Главная страница не открыта"
    assert opened_home_page.get_search_filters().is_displayed(), "Блок фильтров поиска не отображается"
    assert opened_home_page.get_search_filters_brands().is_displayed(), "Блок брендов в фильтрах не отображается"
    assert opened_home_page.get_block_categories().is_displayed(), "Блок категорий не отображается"

    product = opened_home_page.get_random_product()
    assert product is not None and product.is_displayed(), "Случайный продукт не найден или не отображается"

    price = opened_home_page.get_random_product_price()
    assert price is not None and price.text.strip() != "", "Цена продукта отсутствует"


@allure.feature("Главная страница")
@allure.story("Смена валюты")
@allure.title("Тест переключения валюты продукта на доллар")
def test_switch_product_currency_to_dollar(opened_main_page):
    opened_main_page.switch_currency_to_dollar()
    product = opened_main_page.get_random_product()
    price = product.find_element(*opened_main_page.PRODUCT_PRICE)
    assert "$" in price.text, "Валюта продукта не переключилась на доллар"