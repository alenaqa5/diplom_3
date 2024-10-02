from selenium.webdriver.common.by import By

class OrdersListLocators:
    order_item = [By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]"]
    structure_of_order = [By.XPATH, "//p[contains(text(), 'Cостав')]"]
    completed_orders_since_beginning_counter = [By.XPATH, "//p[contains(text(),'Выполнено за все время:')]/following-sibling::*[contains(@class,'OrderFeed_number')]"]
    completed_orders_today_counter = [By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/following-sibling::*[contains(@class,'OrderFeed_number')]"]
    orders_in_progress = [By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//*[contains(@class,'text text_type_digits-default mb-2')]"]
    order_id = [By.XPATH, "//p[contains(@class,'text text_type_digits-default')]"]

