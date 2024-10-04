from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage
import allure

class Profile(BasePage):
    @allure.step('Перейти в профиль')
    def go_to_profile(self):
        self.wait_and_find_element(ProfileLocators.personal_account_button).click()

    @allure.step('Перейти в историю заказов')
    def go_to_orders_history(self):
        self.wait_element_to_be_clickable(ProfileLocators.to_orders_history).click()

    @allure.step('Выйти из профиля')
    def logout(self):
        logout_button = self.wait_element_to_be_clickable(ProfileLocators.logout_button)
        logout_button.click()

    @allure.step('Получить id заказа')
    def get_order_id(self):
        return self.wait_and_find_element(ProfileLocators.order_id).text

    @allure.step('Подождать исчезновение модального окна')
    def modal_window_is_closed(self):
        self.wait_element_disappeared(ProfileLocators.modal_overlay)

    @allure.step('Подождать загрузки страницы')
    def user_redirected(self, url):
        self.wait_url_to_be_loaded(url)
