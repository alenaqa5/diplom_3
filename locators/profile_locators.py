from selenium.webdriver.common.by import By

class ProfileLocators:
    personal_account_button = [By.XPATH, "//p[text()='Личный Кабинет']"]
    logout_button = [By.XPATH,"//button[text()='Выход']"]
    to_orders_history = [By.XPATH,"//a[contains(@href, '/account/order-history')]"]
    modal_overlay = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    order_id = [By.XPATH, "//p[contains(@class,'text text_type_digits-default')]"]


