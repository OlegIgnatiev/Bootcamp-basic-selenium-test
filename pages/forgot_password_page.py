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
        self.click(by_locator=self.__FORGOT_PASSWORD_BUTTON)

    def check_if_forgot_password_page_opened(self):
        return self.get_element(by_locator=self.__FORGOT_PASSWORD_HEADER)

    def click_reset_button(self):
        self.click(by_locator=self.__FORGOT_PASSWORD_RESET_BUTTON)

    def check_if_email_field_required(self):
        return self.get_element(by_locator=self.__FORGOT_PASSWORD_REQUIRED_FIELD_ERROR)

    def input_invalid_forgot_email(self):
        self.fill(by_locator=self.__FORGOT_PASSWORD_EMAIL_FIELD, value='emaildomain.com')
        self.click(by_locator=self.__FORGOT_PASSWORD_RESET_BUTTON)

    def check_invalid_forgot_email_error_displayed(self):
        return self.get_element(by_locator=self.__FORGOT_PASSWORD_INVALID_EMAIL_ERROR)
