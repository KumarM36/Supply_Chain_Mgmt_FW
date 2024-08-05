from Utilities._lib import SeleniumWrapper
from Utilities.excel_lib import attach_elements
from selenium.common.exceptions import NoSuchElementException


@attach_elements("loginpage")
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def login(self, Username, Password, User_Type):
        self.wrapper.send_text(self.txt_username, value=Username)
        self.wrapper.send_text(self.txt_password, value=Password)
        self.wrapper.select_item(self.select_type, value=User_Type)
        self.wrapper.click_element(self.btn_login)
