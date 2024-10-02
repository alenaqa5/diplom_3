import pytest
import allure
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Переход на страницу "Конструктор"')
    @pytest.mark.parametrize('driver', [('chrome','orders'), ('firefox', 'orders')], indirect=True)
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_constructor_tab()
        assert main_page.check_constructor_header() == 'Соберите бургер'

    @allure.title('Переход на страницу "Лента заказов"')
    @pytest.mark.parametrize('driver', [('chrome','main_page'), ('firefox', 'main_page')], indirect=True)
    def test_go_to_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_orders_tab()
        assert main_page.check_inscription_in_order_list() == 'Выполнено за все время:'

