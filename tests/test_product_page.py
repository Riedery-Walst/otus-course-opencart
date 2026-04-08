import allure

@allure.feature("Страница продукта")
@allure.story("Проверка элементов")
@allure.title("Тест отображения элементов страницы продукта")
def test_product_page_elements(opened_product_page):
    product_name = opened_product_page.get_product_name()
    assert product_name is not None and product_name.text.strip() != "", "Название продукта отсутствует"

    product_price = opened_product_page.get_product_price()
    assert product_price is not None and product_price.text.strip() != "", "Цена продукта отсутствует"

    add_to_cart_button = opened_product_page.get_add_to_cart_button()
    assert add_to_cart_button.is_displayed(), "Кнопка 'Добавить в корзину' не отображается"

    quantity_field = opened_product_page.get_product_quantity()
    assert quantity_field.is_displayed(), "Поле количества продукта не отображается"

    product_image = opened_product_page.get_product_image()
    assert product_image.is_displayed(), "Изображение продукта не отображается"


@allure.feature("Страница продукта")
@allure.story("Добавление в корзину")
@allure.title("Тест добавления продукта в корзину")
def test_add_product_to_cart(opened_product_page):
    add_to_cart_button = opened_product_page.get_add_to_cart_button()
    add_to_cart_button.click()

    proceed_to_checkout = opened_product_page.get_proceed_to_checkout_button()
    assert proceed_to_checkout.is_displayed(), "Кнопка 'Перейти к оформлению заказа' не отображается после добавления продукта в корзину"