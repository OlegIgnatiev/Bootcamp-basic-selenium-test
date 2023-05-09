from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CredentialsPage(BasePage):

    __CREDENTIALS_USERNAME_FIELD = (By.XPATH, '//input[@data-testid="login-form-username-input"]')
    __CREDENTIALS_PASSWORD_FIELD = (By.XPATH, '//input[@data-testid="login-form-password-input"]')
    __CREDENTIALS_LOGIN_BUTTON = (By.XPATH, '//button[text()="Log In"]')
    __CREDENTIALS_INVALID_EMAIL_ERROR = (By.XPATH, '//div[text()="The email must be a valid email address."]')
    __CREDENTIALS_INCORRECT_CREDENTIALS = (By.XPATH, '//div[contains(text() , "Please check your credentials")]')

    def input_invalid_email(self):
        self.fill(by_locator=self.__CREDENTIALS_USERNAME_FIELD, value="emaildomain.com")
        self.fill(by_locator=self.__CREDENTIALS_PASSWORD_FIELD, value="123456789")
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)

    def check_if_invalid_email_error_is_present(self):
        return self.get_element(by_locator=self.__CREDENTIALS_INVALID_EMAIL_ERROR)

    def input_existing_email_incorrect_password(self):
        self.clear(by_locator=self.__CREDENTIALS_USERNAME_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_USERNAME_FIELD, value="oleh.admin@email.com")
        self.clear(by_locator=self.__CREDENTIALS_PASSWORD_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_PASSWORD_FIELD, value="123456789")
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)

    def check_if_check_your_credentials_error(self):
        return self.get_element(by_locator=self.__CREDENTIALS_INCORRECT_CREDENTIALS)

    def input_not_existing_email_existing_password(self):
        self.clear(by_locator=self.__CREDENTIALS_USERNAME_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_USERNAME_FIELD, value="email@domain.com")
        self.clear(by_locator=self.__CREDENTIALS_PASSWORD_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_PASSWORD_FIELD, value="Olegignatiev1!")
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)

    def check_if_check_your_credentials_error_second(self):
        return self.get_element(by_locator=self.__CREDENTIALS_INCORRECT_CREDENTIALS)

    def input_valid_credentials(self):
        self.clear(by_locator=self.__CREDENTIALS_USERNAME_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_USERNAME_FIELD, value="Oleh.admin@email.com")
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)

    def check_if_login_button_is_not_presented_on_the_page(self):
        if_element_is_present = True
        try:
            self.get_element(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)
        except NoSuchElementException:
            if_element_is_present = False
        return if_element_is_present


