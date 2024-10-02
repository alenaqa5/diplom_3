from pages.constructor_page import Constructor
from time import sleep
import pytest
import allure

class TestConstructor:
    @allure.title('Отображение попапа ингредиента')
    @pytest.mark.parametrize('driver', [('chrome','main_page'), ('firefox', 'main_page')], indirect=True)
    def test_open_ingredient_popup(self, driver):
        ingredient = Constructor(driver)
        ingredient.tap_on_ingredient()
        assert ingredient.check_ingredient_details_popup_title() == 'Детали ингредиента'

    @allure.title('Закрытие попапа с ингредиентом')
    @pytest.mark.parametrize('driver', [('chrome', 'main_page'), ('firefox', 'main_page')], indirect=True)
    def test_close_ingredient_popup(self, driver):
        ingredient = Constructor(driver)
        ingredient.tap_on_ingredient()
        ingredient.close_modal_window()
        sleep(1)
        assert ingredient.check_popup_closed() is True

    @allure.title('Получение счетчика добавленного ингредиента')
    @pytest.mark.parametrize('driver', [('chrome','main_page'), ('firefox', 'main_page')], indirect=True)
    def test_get_counter_after_adding_ingredient(self, driver):
        ingredient = Constructor(driver)
        ingredient_counter_before_adding = ingredient.get_counter_number()
        ingredient.add_ingredient_to_burger()
        ingredient_counter_after_adding = ingredient.get_counter_number()
        assert int(ingredient_counter_before_adding) < int(ingredient_counter_after_adding)

    @allure.title('Создание заказа')
    def test_create_order(self, login):
        order = Constructor(login)
        order.add_ingredient_to_burger()
        order.create_order()
        assert order.check_inscription_about_order() == 'идентификатор заказа'

