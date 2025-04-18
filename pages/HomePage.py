from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = "react-burger-menu-btn"
        self.logout_link = "logout_sidebar_link"
        self.sort_dropdown_locator = (By.CLASS_NAME, "product_sort_container")
        self.product_name_locator = (By.CLASS_NAME, "inventory_item_name")
        self.product_price_locator = (By.CLASS_NAME, "inventory_item_price")

    def click_menu(self):
        self.driver.find_element(By.ID, self.menu_button).click()

    def click_logout(self):
        # Tunggu hingga elemen logout bisa diklik dan klik logout
        logout_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.logout_link))
        )
        logout_element.click()  # Klik logout setelah bisa diklik
    
    #Sort
    def select_sort_option(self, option_text):
        # Menunggu dropdown penyortiran muncul
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.sort_dropdown_locator)
        )
        # Menemukan dropdown dan memilih opsi berdasarkan teks
        sort_dropdown = self.driver.find_element(*self.sort_dropdown_locator)
        select = Select(sort_dropdown)
        select.select_by_visible_text(option_text)

    def get_product_names(self):
        elements= self.driver.find_elements(*self.product_name_locator)
        return [elem.text for elem in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.product_price_locator)
        prices = []
        for elem in elements:
            price_text = elem.text.replace("$", "").strip()
            try:
                price = float(price_text)
                prices.append(price)
            except ValueError:
                continue
        return prices




