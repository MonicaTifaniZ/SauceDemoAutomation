from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utilities.read_properties import Read_Config
import time


class TestProductSort:
    url_web = Read_Config.get_url_web()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    def login(self,driver):
        driver.get(self.url_web)

        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))
        )


    def test_sort_by_name_az(self,setup):
        driver = setup
        self.login(driver)

        home = HomePage(driver)
        home.select_sort_option("Name (A to Z)")
        # Memverifikasi bahwa opsi yang dipilih sesuai
        selected_option = driver.find_element(*home.sort_dropdown_locator).get_attribute("value")
        assert selected_option == "az"

        product_names = home.get_product_names()
        assert product_names == sorted(product_names), "Produk tidak diurutkan secara alfabetis A-Z"


    def test_sort_by_name_za(self,setup):
        driver = setup
        self.login(driver)
        home = HomePage(driver)
        home.select_sort_option("Name (Z to A)")

        # Memverifikasi bahwa opsi yang dipilih sesuai
        selected_option = driver.find_element(*home.sort_dropdown_locator).get_attribute("value")
        assert selected_option == "za"

        product_names = home.get_product_names()
        assert product_names == sorted(product_names,reverse=True), "Produk tidak diurutkan secara alfabetis Z-A"

    def test_sort_by_price_lohi(self,setup):
        driver = setup
        self.login(driver)
        home = HomePage(driver)
        home.select_sort_option("Price (low to high)")

        # Memverifikasi bahwa opsi yang dipilih sesuai
        selected_option = driver.find_element(*home.sort_dropdown_locator).get_attribute("value")
        assert selected_option == "lohi"

        product_price = home.get_product_prices()
        assert  product_price == sorted(product_price), "Harga produk tidak diurutkan dari rendah ke tinggi"

    def test_sort_by_price_hilo(self,setup):
        driver = setup
        self.login(driver)
        home = HomePage(driver)
        home.select_sort_option("Price (high to low)")

        # Memverifikasi bahwa opsi yang dipilih sesuai
        selected_option = driver.find_element(*home.sort_dropdown_locator).get_attribute("value")
        assert selected_option == "hilo"

        product_price = home.get_product_prices()
        assert product_price == sorted(product_price, reverse=True), "Harga produk tidak diurutkan dari tinggi ke rendah"