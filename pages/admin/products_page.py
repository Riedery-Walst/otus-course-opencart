from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ProductsPage(BasePage):
    CREATE_PRODUCT_LINK = (By.ID, "page-header-desc-configuration-add")
    CREATE_PRODUCT_BUTTON = (By.ID, "create_product_create")
    DROPDOWN_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"dropdown-toggle-dots")])[1]')
    DELETE_NEWEST_PRODUCT_BUTTON = (By.XPATH, '(//a[contains(@class,"grid-delete-row-link")])[1]')
    NEWEST_PRODUCT_NAME_TEXT = (By.XPATH, '(//*[contains(@class,"column-name")])[1]')
    CONFIRM_DELETE_BUTTON = (By.CLASS_NAME, 'btn-confirm-submit')

    def goto_create_product_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.ID, "modal-create-product"))
        )

        self.wait_until_visible(self.CREATE_PRODUCT_LINK)
        self.click(self.CREATE_PRODUCT_LINK)

        modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "modal-create-product"))
        )

        iframe = WebDriverWait(modal, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )

        self.driver.switch_to.frame(iframe)

        self.wait_until_visible(self.CREATE_PRODUCT_BUTTON)
        self.click(self.CREATE_PRODUCT_BUTTON)

        self.driver.switch_to.default_content()
        
    def delete_newest_product(self):
        self.click(self.DROPDOWN_NEWEST_PRODUCT_BUTTON)
        self.click(self.DELETE_NEWEST_PRODUCT_BUTTON)
        self.click(self.CONFIRM_DELETE_BUTTON)

    def get_newest_product_name(self):
        element = self.find_element(self.NEWEST_PRODUCT_NAME_TEXT)
        return element.text