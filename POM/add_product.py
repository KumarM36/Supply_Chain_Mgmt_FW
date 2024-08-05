from Utilities._lib import SeleniumWrapper
from Utilities.excel_lib import worksheet, attach_elements
from ast import literal_eval


@worksheet("welcome_admin_page")
# @worksheet("product")
# @worksheet("homepage")
@worksheet("add_product_page")
# @worksheet("manufacturer")
@attach_elements("add_product_page")
class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)
    def add_product(self, name, price, unit, category, stock, description):
        from time import sleep
        sleep(2)
        self.wrapper.click_element(self.add_products)
        sleep(5)
        self.wrapper.send_text(self.product_name, value=name)
        self.wrapper.send_text(self.product_price, value=price)
        self.wrapper.select_item(self.unit_dropdown, value=unit)
        self.wrapper.select_item(self.category_dropdown, value=category)
        if stock.upper() == "ENABLE":
            self.wrapper.click_element(self.sm_enable)
        elif stock.upper() == "DISABLE":
            self.wrapper.click_element(self.sm_enable)
        else:
            raise Exception("Please choose a valid option")
        self.wrapper.send_text(self.product_discription, value=description)
        self.wrapper.click_element(self.btn_add_prod)
        sleep(5)
        self.wrapper.alert_box_accept()