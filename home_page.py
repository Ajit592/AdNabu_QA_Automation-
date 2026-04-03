from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage

class HomePage(BasePage):

    SEARCH_BOX = (By.NAME, "q")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.driver.find_element(*self.SEARCH_BOX).send_keys(Keys.RETURN)
        return SearchResultsPage(self.driver)
