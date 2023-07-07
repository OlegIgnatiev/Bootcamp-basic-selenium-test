from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CredentialsPage(BasePage):
    # static xpath. used as is
    __CREDENTIALS_LOGIN_BUTTON = (By.XPATH, '//button[text()="Log In"]')
    __CREDENTIALS_USERNAME_FIELD = (By.XPATH, '//input[@data-testid="login-form-username-input"]')
    __CREDENTIALS_PASSWORD_FIELD = (By.XPATH, '//input[@data-testid="login-form-password-input"]')
    # dynamic xpath. should be transformed to (By.XPATH, "xpath") before use
    __CREDENTIALS_ERROR = "//div[contains(text(), '{expected_text}')]"

    def click_log_in_button(self):
        """
        Click Login button
        """
        self.click(by_locator=self.__CREDENTIALS_LOGIN_BUTTON)

    def check_if_appropriate_error_displayed(self, expected_text: str):
        """
        Check that email field required.
        """
        text_locator = (By.XPATH, self.__CREDENTIALS_ERROR.format(expected_text=expected_text))
        return self.get_element(text_locator)

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








