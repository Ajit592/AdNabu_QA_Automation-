import pytest
from pages.home_page import HomePage
from utils.driver_factory import get_driver

class TestAddToCart:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get("https://adnabuteststore.myshopify.com")
        self.home_page = HomePage(self.driver)

    def test_search_and_add_to_cart(self):
        search_results = self.home_page.search_product("Shoes")
        product_page = search_results.select_first_product()
        product_page.add_to_cart()
        assert product_page.is_product_added_to_cart()

    def teardown_method(self):
        self.driver.quit()
