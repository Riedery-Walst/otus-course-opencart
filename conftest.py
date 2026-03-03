import pytest
from selenium import webdriver

from tests.logger import create_logger


logger = create_logger(__name__)

pytest_plugins = [
    "fixtures.page_fixtures",
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
            driver = webdriver.Chrome()
        case "edge":
            driver = webdriver.Edge()
        case "firefox":
            driver = webdriver.Firefox()
        case _:
            pytest.fail(f"Unknown browser: {browser_name}")

    logger.info(f"Start browser: {browser_name}")

    yield driver

    logger.info(f"Close browser: {browser_name}")
    driver.quit()

