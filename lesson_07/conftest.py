import pytest
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = Chrome(options=options)
    yield driver
    driver.quit()
