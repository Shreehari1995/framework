from selenium.webdriver import Chrome

import helium
from pytest import fixture
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@fixture(scope="session")
def setup():
    driver = Chrome(ChromeDriverManager().install())
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.delete_all_cookies()
    helium.set_driver(driver)
    yield driver
    driver.quit()

def browser_options(browser_type="", headless="no"):
    if headless.lower() == "yes":



