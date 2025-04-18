import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage
from utilities.read_properties import Read_Config


class TestLogin:
    url_web = Read_Config.get_url_web()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    invalid_password = Read_Config.get_invalid_password()
    invalid_credential = Read_Config.get_invalid_credential()
    username_required = Read_Config.get_error_username_required()
    password_required = Read_Config.get_error_password_required()

    def test_title_verification(self,setup):
        self.driver = setup
        self.driver.get(self.url_web)
        assert self.driver.title == "Swag Labs"

    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get(self.url_web)  # ini sekarang benar

        login_lp = LoginPage(self.driver)
        login_lp.enter_username(self.username)
        login_lp.enter_password(self.password)
        login_lp.click_login()

        product_text_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))
        )
        assert product_text_elem.text == "Products"

    def test_invalid_login_username(self, setup):
        self.driver = setup
        self.driver.get(self.url_web)
        login_lp = LoginPage(self.driver)
        login_lp.enter_username(self.invalid_username)
        login_lp.enter_password(self.password)
        login_lp.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3").text
        assert error_message == self.invalid_credential

    def test_invalid_login_password(self,setup):
        self.driver = setup
        self.driver.get(self.url_web)
        login_lp = LoginPage(self.driver)
        login_lp.enter_username(self.username)
        login_lp.enter_password(self.invalid_password)
        login_lp.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3").text
        assert error_message == self.invalid_credential

    def test_invalid_login_username_password(self,setup):
        self.driver = setup
        self.driver.get(self.url_web)
        login_lp = LoginPage(self.driver)
        login_lp.enter_username(self.invalid_username)
        login_lp.enter_password(self.invalid_password)
        login_lp.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3").text
        assert error_message == self.invalid_credential

    def test_empty_username_valid_password(self, setup):
        self.driver = setup
        self.driver.get(self.url_web)
        login_lp = LoginPage(self.driver)
        login_lp.enter_username("")
        login_lp.enter_password(self.password)
        login_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//h3").text
        assert error_message == self.username_required

    def test_username_valid_empty_password(self, setup):
        self.driver = setup
        self.driver.get(self.url_web)
        login_lp = LoginPage(self.driver)
        login_lp.enter_username(self.username)
        login_lp.enter_password("")
        login_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//h3").text
        assert error_message == self.password_required





