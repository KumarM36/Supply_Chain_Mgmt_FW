# from _lib import SeleniumWrapper
# from excel_lib import attach_elements
# from time import sleep
# from selenium.common.exceptions import NoSuchElementException
#
# @attach_elements("welcome_admin")
# class AdminPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wrapper = SeleniumWrapper(self.driver)
#
#     def Admin(self,Retailers):
#         self.wrapper.click_element(self.Retailers
#
#         def add_product(self, name, price, unit, category, stock, description):
#             self.wrapper.click_element(self.add_products)
#             self.wrapper.send_text(self.product_name, name)
#             self.wrapper.send_text(self.product_price, price)
#             self.wrapper.select_item(self.unit_dropdown, unit)
#             self.wrapper.select_item(self.category_dropdown, category)
#             if stock.upper() == "ENABLE":
#                 self.wrapper.click_element(self.sm_enable)
#             elif stock.upper() == "DISABLE":
#                 self.wrapper.click_element(self.sm_enable)
#             else:
#                 raise Exception("Please choose a valid option")
#             self.wrapper.send_text(self.product_discription, description)
#             self.wrapper.click_element(self.btn_add_prod)
#             self.wrapper.alert_box_accept()
#
#         def check_product(self, search_data):
#             self.wrapper.click_element(self.nav_products)
#             xpath = str(self.search_product)
#             newpath = xpath.replace("{search_data}", search_data)
#             return self.wrapper.check_element(literal_eval(newpath))
#
#         def match_product_price(self, search_product, price):
#             self.wrapper.click_element(self.nav_products)
#             xpath = str(self.p_price)
#             newpath = xpath.replace("{search_product}", search_product)
#             xpath = newpath.replace("{product_price}", price)
#             return self.wrapper.check_element(literal_eval(xpath))
#
#         def edit_product(self, search_data, new_price):
#             self.wrapper.click_element(self.nav_products)
#             xpath = str(self.search_product)
#             newpath = xpath.replace("{search_data}", search_data)
#             try:
#                 self.wrapper.click_element(literal_eval(newpath))
#             except TimeoutError:
#                 raise f"{search_data} Element not found"
#             self.wrapper.clear_text(self.product_price)
#             self.wrapper.send_text(self.product_price, new_price)
#             self.wrapper.click_element(self.sm_enable)
#             self.wrapper.click_element(self.btn_update)
#             # self.wrapper.send_text(self.p_price, new_price)
#             # self.wrapper.click_element(self.btn_update)
#             self.wrapper.alert_box_accept()
