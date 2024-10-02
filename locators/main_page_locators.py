from selenium.webdriver.common.by import By

class MainPageLocators:
    constructor = [By.XPATH, "//p[contains(@class, 'AppHeader') and contains(text(), 'Конструктор')]"]
    query_of_orders = [By.XPATH, "//p[contains(@class, 'AppHeader') and contains(text(), 'Лента Заказов')]"]
    constructor_header = [By.XPATH, "//h1[contains(text(),'Соберите бургер')]"]
    completed_orders_since_beginning = [By.XPATH, "//p[contains(text(),'Выполнено за все время:')]"]

