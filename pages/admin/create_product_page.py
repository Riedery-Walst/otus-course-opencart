from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CreateProductPage(BasePage):
    PRODUCT_HEADER_NAME_1 = (By.ID, "product_header_name_1")
    SAVE_PRODUCT_BUTTON = (By.ID, "product_footer_save")
    CATALOG_PAGE = (By.ID, "subtab-AdminCatalog")
    CATALOG_LI = (By.ID, "subtab-AdminProducts")
    SUCCESSFUL_UPDATE_TEXT = (By.XPATH, '//*[text()="Successful update"]')

    def goto_products_page(self):
        self.click(self.CATALOG_PAGE)
        self.click(self.CATALOG_LI)

    def set_product_name(self, product_name):
        element = self.find_element(self.PRODUCT_HEADER_NAME_1)
        element.send_keys(product_name)

    def save_product(self):
        self.click(self.SAVE_PRODUCT_BUTTON)

    def get_successful_text(self):
        return self.find_element(self.SUCCESSFUL_UPDATE_TEXT)