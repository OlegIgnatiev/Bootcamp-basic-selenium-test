from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CredentialsPage(BasePage):

    __CREDENTIALS_LOGIN_BUTTON = (By.XPATH, '//button[text()="Log In"]')
    __CREDENTIALS_USERNAME_FIELD = (By.XPATH, '//input[@data-testid="login-form-username-input"]')
    __CREDENTIALS_PASSWORD_FIELD = (By.XPATH, '//input[@data-testid="login-form-password-input"]')
    __CREDENTIALS_INVALID_EMAIL_ERROR = (By.XPATH, '//div[text()="The email must be a valid email address."]')
    __CREDENTIALS_INCORRECT_CREDENTIALS = (By.XPATH, '//div[contains(text() , "Please check your credentials")]')
    __CREDENTIALS_EMAIL_FIELD_REQUIRED_ERROR = (By.XPATH, '//div[text() = "The email field is required."]')
    __CREDENTIALS_PASSWORD_FIELD_REQUIRED_ERROR = (By.XPATH, '//div[text() = "The password field is required."]')

    def click_log_in_button(self):
        """
        Click Login button
        """
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)

    def check_if_email_field_required(self):
        """
        Check that email field required.
        """
        return self.get_element(by_locator=self.__CREDENTIALS_EMAIL_FIELD_REQUIRED_ERROR)

    def check_if_password_field_required(self):
        """
        Check that Password field required.
        """
        return self.get_element(by_locator=self.__CREDENTIALS_PASSWORD_FIELD_REQUIRED_ERROR)

    def check_if_invalid_email_error_is_present(self):
        """
        Check that Invalid Email Error displayed.
        """
        return self.get_element(by_locator=self.__CREDENTIALS_INVALID_EMAIL_ERROR)

    def check_if_check_your_credentials_error(self):
        """
        Check that Incorrect Credentials Error displayed.
        """
        return self.get_element(by_locator=self.__CREDENTIALS_INCORRECT_CREDENTIALS)

    def check_if_check_your_credentials_error_second(self):
        """
        Check that Incorrect Credentials Error displayed.
        """
        return self.get_element(by_locator=self.__CREDENTIALS_INCORRECT_CREDENTIALS)

    def check_if_login_button_is_not_presented_on_the_page(self):
        """
        Check if Login button not on the page.
        """
        self.if_element_not_present_on_the_page(self.__CREDENTIALS_LOGIN_BUTTON)

    def input_credentials_and_submit(self, login_value: str, password_value: str):
        """
        Clear and fill Username and Password fields and click Login.
        """
        self.clear(by_locator=self.__CREDENTIALS_USERNAME_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_USERNAME_FIELD, value=login_value)
        self.clear(by_locator=self.__CREDENTIALS_PASSWORD_FIELD)
        self.fill(by_locator=self.__CREDENTIALS_PASSWORD_FIELD, value=password_value)
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)






