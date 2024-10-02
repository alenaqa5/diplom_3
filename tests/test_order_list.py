from time import sleep
from pages.orders_page import Orderslist
from pages.constructor_page import Constructor
from pages.main_page import MainPage
from pages.profile import Profile
import pytest
import allure

class TestOrderList:
    @allure.title('Отображение попапа о заказе при его раскрытии')
    @pytest.mark.parametrize('driver', [('chrome','orders'), ('firefox', 'orders')], indirect=True)
    def test_display_popup_order_info(self, driver):
        order_page = Orderslist(driver)
        order_page.tap_on_order()
        assert order_page.check_popup_order_info() == 'Cостав'

    @allure.title('Отображение айдишника заказа в списке заказов')
    def test_display_number_of_order_in_orders_list(self, login):
        order_page = Orderslist(login)
        order = Constructor(login)
        main_page = MainPage(login)
        profile = Profile(login)
        order.add_ingredient_to_burger()
        order.create_order()
        sleep(2)
        order.close_modal_window()
        sleep(2)
        profile.go_to_profile()
        sleep(1)
        profile.go_to_orders_history()
        user_order_id = profile.get_order_id()
        main_page.go_to_orders_tab()
        user_order_id_in_list_of_orders = order_page.get_order_id()
        assert user_order_id == user_order_id_in_list_of_orders

    @allure.title('Отображение заказа в статусе "в работе"')
    def test_display_number_of_order_in_progress_status(self, login):
        order_page = Orderslist(login)
        order = Constructor(login)
        main_page = MainPage(login)
        profile = Profile(login)
        order.add_ingredient_to_burger()
        order.create_order()
        sleep(2)
        order.close_modal_window()
        sleep(2)
        profile.go_to_profile()
        sleep(1)
        profile.go_to_orders_history()
        user_order_id = profile.get_order_id()
        main_page.go_to_orders_tab()
        user_order_id_in_list_of_orders = order_page.get_order_id_in_progress_status()
        assert user_order_id.strip('#') == user_order_id_in_list_of_orders

    @allure.title('Получение счетчика "заказов за все время" после создания заказа ')
    def test_counter_of_orders_since_beginning_is_growing_after_new_order(self, login):
        order_page = Orderslist(login)
        order = Constructor(login)
        main_page = MainPage(login)
        main_page.go_to_orders_tab()
        number_of_orders_before = order_page.get_number_from_orders_all_time_counter()
        main_page.go_to_constructor_tab()
        order.add_ingredient_to_burger()
        order.create_order()
        sleep(2)
        order.close_modal_window()
        sleep(1)
        main_page.go_to_orders_tab()
        number_of_orders_after = order_page.get_number_from_orders_all_time_counter()
        assert int(number_of_orders_before) < int(number_of_orders_after)

    @allure.title('Получение счетчика "заказов за сегодня" после создания заказа')
    def test_counter_of_orders_today_is_growing_after_new_order(self, login):
        order_page = Orderslist(login)
        order = Constructor(login)
        main_page = MainPage(login)
        main_page.go_to_orders_tab()
        number_of_orders_before = order_page.get_number_from_orders_today_counter()
        main_page.go_to_constructor_tab()
        order.add_ingredient_to_burger()
        order.create_order()
        sleep(2)
        order.close_modal_window()
        sleep(3)
        main_page.go_to_orders_tab()
        number_of_orders_after = order_page.get_number_from_orders_today_counter()
        assert int(number_of_orders_before) < int(number_of_orders_after)
