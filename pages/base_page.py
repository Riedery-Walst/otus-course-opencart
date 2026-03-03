from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.logger import create_logger

logger = create_logger(__name__)


class BasePage:
    TITLE = ""
    PATH = ""

    @property
    def url(self):
        return f"{self.base_url}{self.PATH}"

    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        logger.info(f"Open {self.url}")

        self.driver.get(self.url)

    def find_element(self, locator):
        logger.info(f"Find {locator}")

        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        logger.info(f"Find {locator}")

        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        logger.info(f"Click {locator}")

        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.title_contains(self.TITLE))
