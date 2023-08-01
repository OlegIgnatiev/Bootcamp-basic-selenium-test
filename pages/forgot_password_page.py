from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    # static xpath. used as is
    __FORGOT_PASSWORD_HEADER = (By.XPATH, '//h4[text() = "Forgot Password"]')
    __FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[@data-testid="login-form-forgot-password-link"]')
    __FORGOT_PASSWORD_RESET_BUTTON = (By.XPATH, '//button[text() = "Reset"]')
    __FORGOT_PASSWORD_EMAIL_FIELD = (By.XPATH, '//input[@id = "email"]')
    # dynamic xpath. should be transformed to (By.XPATH, "xpath") before use
    __FORGOT_PASSWORD_ERROR = "//div[contains(text(), '{expected_text}')]"

    def click_forgot_password_button(self):
        """
        Click Forgot Password button.
        """
        self.click(by_locator=self.__FORGOT_PASSWORD_BUTTON)

    def check_appropriate_error_displayed(self, expected_text: str):
        """
        Check that appropriate error displayed.
        """
        text_locator = (By.XPATH, self.__FORGOT_PASSWORD_ERROR.format(expected_text=expected_text))
        return self.if_element_displayed(by_locator=text_locator)

    def check_if_forgot_password_page_opened(self):
        """
        Check that Forgot Password header displayed.
        """
        return self.if_element_displayed(by_locator=self.__FORGOT_PASSWORD_HEADER)

    def click_reset_button(self):
        """
        Click Reset button.
        """
        self.click(by_locator=self.__FORGOT_PASSWORD_RESET_BUTTON)

    def input_invalid_forgot_email_and_submit(self, invalid_forgot_email_value: str):
        """
        Fill the email field and click Reset button.
        """
        self.fill(by_locator=self.__FORGOT_PASSWORD_EMAIL_FIELD, value=invalid_forgot_email_value)
        self.click(by_locator=self.__FORGOT_PASSWORD_RESET_BUTTON)
