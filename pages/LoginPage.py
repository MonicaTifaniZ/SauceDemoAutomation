from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = "user-name"
        self.password_field = "password"
        self.login_button = "login-button"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button).click()
