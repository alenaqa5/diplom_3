from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop

class Constructor(BasePage):
    def tap_on_ingredient(self):
        self.wait_and_find_element(ConstructorLocators.ingredient).click()

    def check_ingredient_details_popup_title(self):
        title = self.wait_and_find_element(ConstructorLocators.ingredient_details_popup_title)
        return title.text

    def check_popup_closed(self):
        return self.is_element_not_visible(ConstructorLocators.ingredient_details_popup_title)

    def close_modal_window_of_ingredient(self):
        self.wait_and_find_element(ConstructorLocators.close_ingredient_info_popup).click()

    def add_ingredient_to_burger(self):
        self.wait_and_find_element(ConstructorLocators.ingredient)
        source = self.driver.find_element(*ConstructorLocators.ingredient)
        target = self.driver.find_element(*ConstructorLocators.constructor_area)
        drag_and_drop(self.driver, source, target)

    def get_counter_number(self):
        counter_text = self.wait_and_find_element(ConstructorLocators.counter_of_the_ingredient)
        return counter_text.text

    def create_order(self):
        self.wait_and_find_element(ConstructorLocators.create_order).click()

    def check_inscription_about_order(self):
        return self.wait_and_find_element(ConstructorLocators.order_id_inscription).text

