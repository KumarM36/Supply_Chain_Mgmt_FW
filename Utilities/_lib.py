import json
import logging
from typing import Self

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import ElementClickInterceptedException

MAX_TIMEOUT = 10

def _wait(func):
    def wrapper(instance: Self, locator: tuple[str, str], **kwargs: dict[str, str]):
        # Wait until the element is loaded and visible
        print(f"waiting for element {locator}")
        w = WebDriverWait(instance.driver, MAX_TIMEOUT)
        v = visibility_of_element_located(locator)
        w.until(v)
        # original func (enter_text, click_element)
        func(instance, locator, **kwargs)
    return wrapper
def __wait(cls):
    for key, value in cls.__dict__.items():
        if callable(value) and key != "__init__" and key != "alert_box_accept":
            setattr(cls, key, _wait(value))
    return cls

@__wait
class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, xpath):
        try:
            self.driver.find_element(*xpath).click()
        except ElementClickInterceptedException:
            # self.scroll_to_end()
            self.click_element(xpath)

    # def enter_text(self, xpath, value):
    #     self.driver.find_element(*xpath).send_keys(value)

    def select_item(self, xpath, value):
        select = Select(self.driver.find_element(*xpath))
        select.select_by_visible_text(value)

    def send_text(self,xpath,value):
        self.driver.find_element(*xpath).send_keys(value)

    def alert_box_accept(self):
        alert = self.driver.switch_to.alert.accept()
