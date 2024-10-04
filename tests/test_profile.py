import data
from pages.profile import Profile
import allure

class TestProfile:
    @allure.title('Переход в историю заказов')
    def test_go_to_orders_history_in_profile(self, login):
        profile = Profile(login)
        profile.go_to_profile()
        profile.modal_window_is_closed()
        profile.go_to_orders_history()
        assert login.current_url == data.URLS['orders_history']

    @allure.title('Выход из профиля')
    def test_logout(self, login):
        profile = Profile(login)
        profile.go_to_profile()
        profile.modal_window_is_closed()
        profile.logout()
        profile.user_redirected(data.URLS['auth_form'])
        assert login.current_url == data.URLS['auth_form']
