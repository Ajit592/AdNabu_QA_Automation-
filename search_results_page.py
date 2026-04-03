from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage

class SearchResultsPage(BasePage):

    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-item")

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)
        return ProductPage(self.driver)
