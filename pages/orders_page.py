from locators.orders_list_locators import OrdersListLocators
from pages.base_page import BasePage
import allure

class Orderslist(BasePage):
    @allure.step('Нажать на заказ')
    def tap_on_order(self):
        self.wait_and_find_element(OrdersListLocators.order_item).click()

    @allure.step('Проверить наличие текста в попапе')
    def check_popup_order_info(self):
        return self.wait_and_find_element(OrdersListLocators.structure_of_order).text

    @allure.step('Получить число из счетчика заказов за все время')
    def get_number_from_orders_all_time_counter(self):
        return self.wait_and_find_element(OrdersListLocators.completed_orders_since_beginning_counter).text

    @allure.step('Получить число из счетчика заказов за сегодня')
    def get_number_from_orders_today_counter(self):
        return self.wait_and_find_element(OrdersListLocators.completed_orders_today_counter).text

    @allure.step('Получить id заказа в списке заказов')
    def get_order_id(self):
        return self.wait_and_find_element(OrdersListLocators.order_id).text

    @allure.step('Получить id заказа в статусе "в работе"')
    def get_order_id_in_progress_status(self):
        return self.wait_and_find_element(OrdersListLocators.orders_in_progress).text

