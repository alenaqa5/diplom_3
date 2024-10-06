from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR = [By.XPATH, "//p[contains(@class, 'AppHeader') and contains(text(), 'Конструктор')]"]
    QUERY_OF_ORDERS = [By.XPATH, "//p[contains(@class, 'AppHeader') and contains(text(), 'Лента Заказов')]"]
    CONSTRUCTOR_HEADER = [By.XPATH, "//h1[contains(text(),'Соберите бургер')]"]
    COMPLETED_ORDERS_SINCE_BEGINNING = [By.XPATH, "//p[contains(text(),'Выполнено за все время:')]"]

