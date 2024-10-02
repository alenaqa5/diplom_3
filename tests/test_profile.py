from pages.profile import Profile
from time import sleep

class TestProfile:
    def test_go_to_orders_history_in_profile(self, login):
        profile = Profile(login)
        profile.go_to_profile()
        sleep(5)
        profile.go_to_orders_history()
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    def test_logout(self, login):
        profile = Profile(login)
        profile.go_to_profile()
        sleep(3)
        profile.logout()
        sleep(2)
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'
