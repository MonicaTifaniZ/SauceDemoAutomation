import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utilities.read_properties import Read_Config

class TestLogout:
    url_web = Read_Config.get_url_web()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    def test_logout_success(self,setup):
        driver = setup
        driver.get(self.url_web)

        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))
        )

        home = HomePage(driver)
        home.click_menu()

        WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))

        )
        home.click_logout()

           # Verifikasi kita kembali ke halaman login
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        assert login_button.is_displayed()
