from selenium.webdriver.common.by import By


class ConstructorLocators:
    ingredient = [By.XPATH, "//a[contains(@class ,'BurgerIngredient_ingredient')]"]
    ingredient_details_popup_title = [By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"]
    close_ingredient_info_popup = [By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]"]
    counter_of_the_ingredient =  [By.XPATH, "//p[contains(@class, 'counter_counter')]"]
    constructor_area = [By.XPATH, "//*[contains(@class, 'constructor-element')]"]
    create_order = [By.XPATH, "//button[contains(text(),'Оформить заказ')]"]
    order_id_inscription = [By.XPATH, "//p[contains(text(),'идентификатор заказа')]"]




