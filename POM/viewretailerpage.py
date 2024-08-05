from Utilities._lib import SeleniumWrapper
from excel_lib import attach_elements
from time import sleep
from selenium.common.exceptions import NoSuchElementException

@attach_elements("view_retailer")
class ViewRetailerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def ViewRetailerPage(self,AddProducts):
        self.wrapper.click_element(self.AddProducts)

    def login(self, Productname, Price, UnitType, Category, StockManagement, Description, AddProduct):
            self.wrapper.enter_text(self.txt_productname, value=product:name)
            self.wrapper.enter_text(self.txt_password, value=password)
            self.wrapper.click_element(self.submit_button)
