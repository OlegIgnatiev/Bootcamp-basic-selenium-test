from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    __FORGOT_PASSWORD_HEADER = (By.XPATH, '//h4[text() = "Forgot Password"]')
    __FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[@data-testid="login-form-forgot-password-link"]')
    __FORGOT_PASSWORD_RESET_BUTTON = (By.XPATH, '//button[text() = "Reset"]')
    __FORGOT_PASSWORD_REQUIRED_FIELD_ERROR = (By.XPATH, '//div[text() = "The email field is required."]')
    __FORGOT_PASSWORD_EMAIL_FIELD = (By.XPATH, '//input[@id = "email"]')
    __FORGOT_PASSWORD_INVALID_EMAIL_ERROR = (By.XPATH, '//div[text() = "The email must be a valid email address."]')

    def click_forgot_password_button(self):
        """
        Click Forgot Password button.
        """
        self.click(by_locator=self.__FORGOT_PASSWORD_BUTTON)

    def check_if_forgot_password_page_opened(self):
        """
        Check that Forgot Password header displayed.
        """
        return self.get_element(by_locator=self.__FORGOT_PASSWORD_HEADER)

    def click_reset_button(self):
        """
        Click Reset button.
        """
        self.click(by_locator=self.__FORGOT_PASSWORD_RESET_BUTTON)

    def check_if_email_field_required(self):
        """
        Check that Email field is required.
        """
        return self.get_element(by_locator=self.__FORGOT_PASSWORD_REQUIRED_FIELD_ERROR)

    def input_invalid_forgot_email_and_submit(self, invalid_forgot_email_value: str):
        """
        Fill the email field and click Reset button.
        """
        self.fill(by_locator=self.__FORGOT_PASSWORD_EMAIL_FIELD, value=invalid_forgot_email_value)
        self.click(by_locator=self.__FORGOT_PASSWORD_RESET_BUTTON)

    def check_invalid_forgot_email_error_displayed(self):
        """
        Check that Invalid Email error displayed.
        """
        return self.get_element(by_locator=self.__FORGOT_PASSWORD_INVALID_EMAIL_ERROR)
