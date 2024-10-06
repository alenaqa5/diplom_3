from selenium.webdriver.common.by import By

class ProfileLocators:
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"]
    LOGOUT_BUTTON = [By.XPATH,"//button[text()='Выход']"]
    TO_ORDERS_HISTORY = [By.XPATH,"//a[contains(@href, '/account/order-history')]"]
    ORDER_ID = [By.XPATH, "//p[contains(@class,'text text_type_digits-default')]"]


