from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    @allure.step('Перейти в таб "Конструктор"')
    def go_to_constructor_tab(self):
        self.wait_and_find_element(MainPageLocators.CONSTRUCTOR).click()

    @allure.step('Перейти в таб "Лента заказов"')
    def go_to_orders_tab(self):
        self.wait_and_find_element(MainPageLocators.QUERY_OF_ORDERS).click()

    @allure.step('Проверить заголовок таба "Конструктор"')
    def check_constructor_header(self):
        return self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_HEADER).text

    @allure.step('Проверить заголовок таба "Лента заказов"')
    def check_inscription_in_order_list(self):
        return self.wait_and_find_element(MainPageLocators.COMPLETED_ORDERS_SINCE_BEGINNING).text

