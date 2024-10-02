from conftest import driver
from pages.recover_password import RecoverPassword
import pytest
import allure

class TestRecoverPassword:
    @allure.title('Активация поля пароля при восстановлении пароля')
    @pytest.mark.parametrize('driver', [('chrome','auth_form'), ('firefox', 'auth_form')], indirect=True)
    def test_recover_password(self, driver):
        auth_page = RecoverPassword(driver)
        auth_page.go_to_recover_password_form()
        auth_page.input_email_to_reset_password_form()
        auth_page.click_recover_password_button()
        assert auth_page.check_password_field_presented() == 'Пароль'

    @allure.title('Отображение пароля')
    @pytest.mark.parametrize('driver', [('chrome', 'auth_form'), ('firefox', 'auth_form')], indirect=True)
    def test_show_password(self, driver):
        auth_page = RecoverPassword(driver)
        auth_page.show_password()
        assert auth_page.password_field_is_active() is True