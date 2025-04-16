from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = "react-burger-menu-btn"
        self.logout_link = "logout_sidebar_link"
        self.cart_items = (By.CLASS_NAME,"cart_item")
    
    def click_menu(self):
        self.driver.find_element(By.ID, self.menu_button).click()

    def click_logout(self):
        # Tunggu hingga elemen logout bisa diklik dan klik logout
        logout_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.logout_link))
        )
        logout_element.click()  # Klik logout setelah bisa diklik

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()