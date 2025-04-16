from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_items = (By.CLASS_NAME,"cart_item")
        self.button_remove = (By.CLASS_NAME, "cart_button")

    def open_cart(self):
        self.driver.find_element(*self.shopping_cart).click()

    def get_cart_items_count(self):
       return len(self.driver.find_elements(*self.cart_items))

    def remove_item(self):
        self.driver.find_element(*self.button_remove).click()
