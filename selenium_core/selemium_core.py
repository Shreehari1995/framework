import pytest
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("setup")
class SeleniumCore:
    def __init__(self, setup):
        self.driver = setup

    def get_element(self, loc_type, loc_value):
        return self.driver.find_element(loc_type, loc_value)

    def click_element(self, loc_type, loc_value):
        self.get_element(loc_type, loc_value).click()

    def send_keys(self, loc_type, loc_value):
        self.get_element(loc_type, loc_value).send_keys()

    def move_to_the_element(self, loc_type, loc_value):
        element = self.get_element(loc_type, loc_value)
        ActionChains(self.driver).move_to_element(element)

    #ngishdhpifvubapiubvpiuasbhvpihwuigf