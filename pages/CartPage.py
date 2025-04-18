from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_items = (By.CLASS_NAME,"cart_item")
        self.button_remove = (By.CLASS_NAME, "cart_button")
        self.title_items = (By.CLASS_NAME,"inventory_item_name")
        self.items_prices = (By.CLASS_NAME,"inventory_item_price")


    def get_inventory_title_items(self):
        self.driver.find_element(By.CLASS_NAME,self.title_items)

    def select_sort_type_by_text(self, visible_text_option):
        self.dsl.select_by_visible_text('//select[@data-test="product_sort_container"]', visible_text_option)

    def get_sort_type_text(self):
        return self.dsl.get_visible_text_selected('//select[@data-test="product_sort_container"]')


