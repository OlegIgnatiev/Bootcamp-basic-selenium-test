from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class VerificationPage(BasePage):
    # static xpath. used as is
    __VERIFICATION_CODE_FIELD = (By.XPATH, '//input[@id ="code"]')
    __VERIFICATION_VERIFY_BUTTON = (By.XPATH, '//button[text() ="Verify"]')
    # dynamic xpath. should be transformed to (By.XPATH, "xpath") before use
    __VERIFICATION_ERROR = "//div[contains(text(), '{expected_text}')]"

    def click_verify_button(self):
        """
        Click Verify button.
        """
        self.click(by_locator=self.__VERIFICATION_VERIFY_BUTTON)

    def check_that_appropriate_verification_error(self, expected_text: str):
        """
        Check that Verification Field is required error displayed.
        """
        text_locator = (
            By.XPATH, self.__VERIFICATION_ERROR.format(expected_text=expected_text))
        return self.get_element(text_locator)

    def input_security_code_and_submit(self, security_value: str):
        """
        Input security code and click Submit.
        """
        self.clear(by_locator=self.__VERIFICATION_CODE_FIELD)
        self.fill(by_locator=self.__VERIFICATION_CODE_FIELD, value=security_value)
        self.click(by_locator=self.__VERIFICATION_VERIFY_BUTTON)

