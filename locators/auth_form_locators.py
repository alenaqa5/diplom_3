from selenium.webdriver.common.by import By

class AuthFormLocators:
    recover_password = [By.XPATH, "//a[@href='/forgot-password']"]
    input_email = [By.XPATH, "//input[contains(@class, 'input__text')]"]
    input_password = [By.XPATH, "//input[contains(@class, 'input__text') and contains(@name, 'Пароль')]"]
    recover_password_button = [By.XPATH, "//button[contains(@class, 'button_button')]"]
    displaying_password = [By.XPATH, "//div[contains(@class, 'input_type_password')]//*[name()='svg']//*[name()='path' and contains(@d, 'M12 4C14')]"]
    active_password_field = [By.XPATH, "//div[contains(@class, 'input_status_active')]"]

