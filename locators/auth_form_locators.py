from selenium.webdriver.common.by import By

class AuthFormLocators:
    RECOVER_PASSWORD = [By.XPATH, "//a[@href='/forgot-password']"]
    INPUT_EMAIL = [By.XPATH, "//input[contains(@class, 'input__text')]"]
    INPUT_PASSWORD = [By.XPATH, "//input[contains(@class, 'input__text') and contains(@name, 'Пароль')]"]
    RECOVER_PASSWORD_BUTTON = [By.XPATH, "//button[contains(@class, 'button_button')]"]
    RECOVER_PASSWORD_FIELD = [By.XPATH, "//div[contains(@class,'input pr-6 pl-6 input_type_password input_size_default')]//label[contains(@class, 'input__placeholder text')]"]
    DISPLAYING_PASSWORD = [By.XPATH, "//div[contains(@class, 'input_type_password')]//*[name()='svg']//*[name()='path' and contains(@d, 'M12 4C14')]"]
    ACTIVE_PASSWORD_FIELD = [By.XPATH, "//div[contains(@class, 'input_status_active')]"]

