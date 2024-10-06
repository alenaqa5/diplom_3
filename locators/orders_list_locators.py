from selenium.webdriver.common.by import By

class OrdersListLocators:
    ORDER_ITEM = [By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]"]
    STRUCTURE_OF_ORDER = [By.XPATH, "//p[contains(text(), 'Cостав')]"]
    COMPLETED_ORDERS_SINCE_BEGINNING_COUNTER = [By.XPATH, "//p[contains(text(),'Выполнено за все время:')]/following-sibling::*[contains(@class,'OrderFeed_number')]"]
    COMPLETED_ORDERS_TODAY_COUNTER = [By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/following-sibling::*[contains(@class,'OrderFeed_number')]"]
    ORDERS_IN_PROGRESS = [By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//*[contains(@class,'text text_type_digits-default mb-2')]"]
    ORDER_ID = [By.XPATH, "//p[contains(@class,'text text_type_digits-default')]"]

