import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from logger import create_logger

logger = create_logger(__name__)

pytest_plugins = [
    "fixtures.pages_fixtures"
]

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        action="store",
        help="Select a browser driver",
    )
    parser.addoption(
        "--url",
        default="http://localhost:8081",
        action="store",
        help="Base URL",
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = None

    match browser_name:
        case "chrome":
            options = ChromeOptions()
            options.page_load_strategy = "eager"
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        case "firefox":
            options = FirefoxOptions()
            options.page_load_strategy = "eager"
            options.add_argument("--headless")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            driver.maximize_window()

        case "edge":
            options = EdgeOptions()
            options.page_load_strategy = "eager"
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )

        case _:
            pytest.fail(f"Unknown browser: {browser_name}")

    logger.info(f"Start browser: {browser_name}")

    yield driver

    logger.info(f"Close browser: {browser_name}")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=AttachmentType.PNG
                )
            except Exception as e:
                allure.attach(
                    str(e),
                    name="screenshot_error",
                    attachment_type=AttachmentType.TEXT
                )