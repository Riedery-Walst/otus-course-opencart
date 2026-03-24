import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
            options = Options()
            options.page_load_strategy = "eager"
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)

        case "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(options=options)

        case "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()

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
