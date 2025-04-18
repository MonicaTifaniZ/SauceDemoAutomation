import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from utilities.read_properties import Read_Config

class TestCart:
    url_web = Read_Config.get_url_web()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    def test_add_item_to_cart(self,setup):
        driver = setup
        driver.get(self.url_web)

        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,"inventory_item"))
        )

        # Tambahkan produk pertama ke cart
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        assert len(add_to_cart_buttons) > 0, "Tidak ada tombol Add to Cart ditemukan"
        add_to_cart_buttons[0].click()

        # Buka cart
        home = HomePage(driver)
        home.open_cart()

        # Verifikasi item ada di cart
        cart_page = CartPage(driver)
        count = cart_page.get_cart_items_count()
        assert count == 1, f"Jumlah item di cart tidak sesuai, ditemukan: {count}"

