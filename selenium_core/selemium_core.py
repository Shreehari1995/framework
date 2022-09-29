import pytest


@pytest.mark.usefixtures("setup")
class SeleniumCore:
    def __init__(self, setup):
        self.driver = setup

    #  asdfghjkl;cvbnm,
    def get_element(self, loc_type, loc_value):
        return self.driver.find_element(loc_type, loc_value)

    def click_element(self, loc_type, loc_value):
        self.get_element(loc_type, loc_value).click()

    def send_keys(self, loc_type, loc_value):
        self.get_element(loc_type, loc_value).send_keys()
