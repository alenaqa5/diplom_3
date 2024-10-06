from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop
import allure
class Constructor(BasePage):
    @allure.step('Нажать на ингредиент')
    def tap_on_ingredient(self):
        self.wait_and_find_element(ConstructorLocators.INGREDIENT).click()

    @allure.step('Проверить заголовок попапа ингредиента')
    def check_ingredient_details_popup_title(self):
        title = self.wait_and_find_element(ConstructorLocators.INGREDIENT_DETAILS_POPUP_TITLE)
        return title.text

    @allure.step('Дождаться закрытия попапа')
    def wait_popup_is_closed(self):
        return self.wait_element_disappeared(ConstructorLocators.INGREDIENT_DETAILS_POPUP_TITLE)

    @allure.step('Проверить закрыт ли попап')
    def check_popup_closed(self):
        return self.is_element_not_visible(ConstructorLocators.INGREDIENT_DETAILS_POPUP_TITLE)

    @allure.step('Закрыть модальное окно')
    def close_modal_window(self):
        self.wait_element_to_be_clickable(ConstructorLocators.CLOSE_POPUP).click()

    @allure.step('Добавить ингредиент в бургер')
    def add_ingredient_to_burger(self):
        self.wait_and_find_element(ConstructorLocators.INGREDIENT)
        source = self.driver.find_element(*ConstructorLocators.INGREDIENT)
        target = self.driver.find_element(*ConstructorLocators.CONSTRUCTOR_AREA)
        drag_and_drop(self.driver, source, target)

    @allure.step('Получить число из счетчика ингредиента')
    def get_counter_number(self):
        counter_text = self.wait_and_find_element(ConstructorLocators.COUNTER_OF_THE_INGREDIENT)
        return counter_text.text

    @allure.step('Создать заказ')
    def create_order(self):
        self.wait_and_find_element(ConstructorLocators.CREATE_ORDER).click()

    @allure.step('Проверить текст из попапа о совершении заказа')
    def check_inscription_about_order(self):
        return self.wait_and_find_element(ConstructorLocators.ORDER_ID_INSCRIPTION).text

