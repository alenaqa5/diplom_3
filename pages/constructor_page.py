from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop
import allure
class Constructor(BasePage):
    @allure.step('Нажать на ингредиент')
    def tap_on_ingredient(self):
        self.wait_and_find_element(ConstructorLocators.ingredient).click()

    @allure.step('Проверить заголовок попапа ингредиента')
    def check_ingredient_details_popup_title(self):
        title = self.wait_and_find_element(ConstructorLocators.ingredient_details_popup_title)
        return title.text

    @allure.step('Проверить закрыт ли попап')
    def check_popup_closed(self):
        return self.is_element_not_visible(ConstructorLocators.ingredient_details_popup_title)

    @allure.step('Закрыть модальное окно')
    def close_modal_window(self):
        self.wait_and_find_element(ConstructorLocators.close_popup).click()

    @allure.step('Добавить ингредиент в бургер')
    def add_ingredient_to_burger(self):
        self.wait_and_find_element(ConstructorLocators.ingredient)
        source = self.driver.find_element(*ConstructorLocators.ingredient)
        target = self.driver.find_element(*ConstructorLocators.constructor_area)
        drag_and_drop(self.driver, source, target)

    @allure.step('Получить число из счетчика ингредиента')
    def get_counter_number(self):
        counter_text = self.wait_and_find_element(ConstructorLocators.counter_of_the_ingredient)
        return counter_text.text

    @allure.step('Создать заказ')
    def create_order(self):
        self.wait_and_find_element(ConstructorLocators.create_order).click()

    @allure.step('Проверить текст из попапа о совершении заказа')
    def check_inscription_about_order(self):
        return self.wait_and_find_element(ConstructorLocators.order_id_inscription).text

