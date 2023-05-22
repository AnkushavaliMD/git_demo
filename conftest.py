import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # Initialize the WebDriver instance
    driver = webdriver.Chrome()

    # Optionally, you can set up additional configurations
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Return the WebDriver instance to be used in tests
    yield driver

    # Clean up after the tests
    driver.quit()
