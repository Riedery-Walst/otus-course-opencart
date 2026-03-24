import allure

@allure.feature("Главная страница")
@allure.story("Проверка элементов")
@allure.title("Тест отображения элементов главной страницы")
def test_main_page_elements(opened_main_page):
    assert opened_main_page.is_page_opened(), "Главная страница не открыта"
    assert opened_main_page.get_currency_selector().is_displayed(), "Селектор валюты не отображается"
    assert opened_main_page.get_carousel().is_displayed(), "Карусель не отображается"

    product = opened_main_page.get_random_product()
    assert product is not None and product.is_displayed(), "Случайный продукт не найден или не отображается"

    price = opened_main_page.get_random_product_price()
    assert price is not None and price.text.strip() != "", "Цена продукта отсутствует"


@allure.feature("Главная страница")
@allure.story("Смена валюты")
@allure.title("Тест переключения валюты продукта на доллар")
def test_switch_product_currency_to_dollar(opened_main_page):
    opened_main_page.switch_currency_to_dollar()
    product = opened_main_page.get_random_product()
    price = product.find_element(*opened_main_page.PRODUCT_PRICE)
    assert "$" in price.text, "Валюта продукта не переключилась на доллар"