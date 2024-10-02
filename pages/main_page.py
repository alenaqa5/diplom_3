from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def go_to_constructor_tab(self):
        self.wait_and_find_element(MainPageLocators.constructor).click()

    def go_to_orders_tab(self):
        self.wait_and_find_element(MainPageLocators.query_of_orders).click()

    def check_constructor_header(self):
        return self.wait_and_find_element(MainPageLocators.constructor_header).text

    def check_inscription_in_order_list(self):
        return self.wait_and_find_element(MainPageLocators.completed_orders_since_beginning).text

