from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage

class Profile(BasePage):
    def go_to_profile(self):
        self.wait_and_find_element(ProfileLocators.personal_account_button).click()

    def go_to_orders_history(self):
        self.wait_and_find_element(ProfileLocators.to_orders_history).click()

    def logout(self):
        logout_button = self.wait_element_to_be_clickable(ProfileLocators.logout_button)
        logout_button.click()

    def get_order_id(self):
        return self.wait_and_find_element(ProfileLocators.order_id).text

