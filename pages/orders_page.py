from locators.orders_list_locators import OrdersListLocators
from pages.base_page import BasePage


class Orderslist(BasePage):
    def tap_on_order(self):
        self.wait_and_find_element(OrdersListLocators.order_item).click()

    def check_popup_order_info(self):
        return self.wait_and_find_element(OrdersListLocators.structure_of_order).text

    def get_number_from_orders_all_time_counter(self):
        return self.wait_and_find_element(OrdersListLocators.completed_orders_since_beginning_counter).text

    def get_number_from_orders_today_counter(self):
        return self.wait_and_find_element(OrdersListLocators.completed_orders_today_counter).text

    def get_order_id(self):
        return self.wait_and_find_element(OrdersListLocators.order_id).text

    def get_order_id_in_progress_status(self):
        return self.wait_and_find_element(OrdersListLocators.orders_in_progress).text

