from selenium.webdriver.common.by import By


class ConstructorLocators:
    INGREDIENT = [By.XPATH, "//a[contains(@class ,'BurgerIngredient_ingredient')]"]
    INGREDIENT_DETAILS_POPUP_TITLE = [By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"]
    CLOSE_POPUP = [By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]"]
    COUNTER_OF_THE_INGREDIENT =  [By.XPATH, "//p[contains(@class, 'counter_counter')]"]
    CONSTRUCTOR_AREA = [By.XPATH, "//*[contains(@class, 'constructor-element')]"]
    CREATE_ORDER = [By.XPATH, "//button[contains(text(),'Оформить заказ')]"]
    ORDER_ID_INSCRIPTION = [By.XPATH, "//p[contains(text(),'идентификатор заказа')]"]




