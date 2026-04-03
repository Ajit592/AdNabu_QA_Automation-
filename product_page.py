from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = (By.NAME, "add")
    CART_COUNT = (By.CSS_SELECTOR, ".cart-count")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def is_product_added_to_cart(self):
        cart = self.wait_for_element(self.CART_COUNT)
        return int(cart.text) > 0
