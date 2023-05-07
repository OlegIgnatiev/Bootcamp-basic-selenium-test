from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class CredentialsPage:

    def __init__(self, driver):
        self.driver = driver

    def input_invalid_email(self):
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys(
            "emaildomain.com")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

    def check_if_invalid_email_error_is_present(self):
        return self.driver.find_element(By.XPATH, '//div[text()="The email must be a valid email address."]')

    def input_existing_email_incorrect_password(self):
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys(
            "oleh.admin@email.com")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

    def check_if_check_your_credentials_error(self):
        return self.driver.find_element(By.XPATH, '//div[contains(text() , "Please check your credentials")]')

    def input_not_existing_email_existing_password(self):
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys(
            "email@domain.com")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').send_keys(
            "Olegignatiev1!")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

    def check_if_check_your_credentials_error_second(self):
        return self.driver.find_element(By.XPATH, '//div[contains(text() , "Please check your credentials")]')

    def input_valid_credentials(self):
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys(
            "Oleh.admin@email.com")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

    def check_if_login_button_is_not_presented_on_the_page(self):
        if_element_is_present = True
        try:
            self.driver.find_element(By.XPATH, '//button[text()="Log In"]')
        except NoSuchElementException:
            if_element_is_present = False
        return if_element_is_present



