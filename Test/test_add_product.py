from Utilities.excel_lib import get_test_data_header, get_test_data
from pytest import mark


class Test_Admin:
    admin_header = get_test_data_header("testdata", "admin_login")
    admin_data = get_test_data("testdata", "admin_login")
    add_manufacturer_header = get_test_data_header("testdata", "test_add_manufacturer")
    add_manufacturer_data = get_test_data("testdata", "test_add_manufacturer")
    add_product_header = get_test_data_header("testdata", "add_product")
    add_product_data = get_test_data("testdata", "add_product")


    @mark.parametrize(admin_header, admin_data)
    @mark.parametrize(add_product_header, add_product_data)
    def test_add_product(
        self,
        pages,
        name,
        price,
        unit,
        category,
        stock,
        description,
        username,
        password,
        user_type,
    ):

        pages.loginpage.login(username, password, user_type)
        pages.adminpage.add_product(name, price, unit, category, stock, description)
        # assert True == pages.adminpage.check_product(search_data), f"Product {search_data} not found"
        # pages.adminpage.edit_product(update_product, update_price)
        # assert True == pages.adminpage.match_product_price(update_product, product_price), f"{update_product} is not in the list"