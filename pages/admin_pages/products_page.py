from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    CREATE_PRODUCT_LINK = (By.ID, "page-header-desc-configuration-add")
    STANDARD_PRODUCT_BUTTON = (By.XPATH, "//*[@data-value='standard']")
    CREATE_PRODUCT_BUTTON = (By.ID, "create_product_create")
    DROPDOWN_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"dropdown-toggle-dots")])[1]')
    DELETE_NEWEST_PRODUCT_BUTTON = (By.XPATH, '//a[contains(@class,"grid-delete-row-link")]')

    def goto_create_product_page(self):
        self.click(self.CREATE_PRODUCT_LINK)
        self.click(self.STANDARD_PRODUCT_BUTTON)
        self.click(self.CREATE_PRODUCT_BUTTON)
        
    def delete_newest_product(self):
        self.click(self.DROPDOWN_NEWEST_PRODUCT_BUTTON)
        self.click(self.DELETE_NEWEST_PRODUCT_BUTTON)