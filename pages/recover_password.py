import data
from locators.auth_form_locators import AuthFormLocators
from pages.base_page import BasePage


class RecoverPassword(BasePage):
    def go_to_recover_password_form(self):
        self.wait_and_find_element(AuthFormLocators.recover_password).click()

    def input_email_to_reset_password_form(self):
        email_field = self.wait_and_find_element(AuthFormLocators.input_email)
        email_field.send_keys(data.email)
        email_field.click()

    def show_password(self):
        self.wait_and_find_element(AuthFormLocators.input_password).send_keys(data.password)
        self.wait_and_find_element(AuthFormLocators.displaying_password).click()

    def password_field_is_active(self):
        return self.is_element_visible(AuthFormLocators.active_password_field)

    def click_recover_password_button(self):
        self.wait_and_find_element(AuthFormLocators.recover_password_button).click()

    def check_password_field_presented(self):
        return self.wait_and_find_element(AuthFormLocators.recover_password_field).text




