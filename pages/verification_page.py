from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class VerificationPage(BasePage):

    __VERIFICATION_CODE_FIELD = (By.XPATH, '//input[@id ="code"]')
    __VERIFICATION_VERIFY_BUTTON = (By.XPATH, '//button[text() ="Verify"]')
    __VERIFICATION_SIX_DIGITS_ERROR = (By.XPATH, '//div[text() ="The authentication code must be 6 digits."]')
    __VERIFICATION_INCORRECT_CODE_ERROR = (By.XPATH, '//div[text() ="Invalid authentication code, please try again"]')
    __VERIFICATION_CODE_FIELD_REQUIRED_ERROR = (By.XPATH, '//div[text() = "The authentication code is required."]')

    def click_verify_button(self):
        self.click(by_locator=self.__VERIFICATION_VERIFY_BUTTON)

    def check_that_verification_field_is_required(self):
        return self.get_element(by_locator=self.__VERIFICATION_CODE_FIELD_REQUIRED_ERROR)

    def input_invalid_code(self):
        self.fill(by_locator=self.__VERIFICATION_CODE_FIELD, value="123456789")
        self.click(by_locator=self.__VERIFICATION_VERIFY_BUTTON)

    def check_code_must_be_six_digits_error(self):
        return self.get_element(by_locator=self.__VERIFICATION_SIX_DIGITS_ERROR)

    def input_incorrect_code(self):
        self.clear(by_locator=self.__VERIFICATION_CODE_FIELD)
        self.fill(by_locator=self.__VERIFICATION_CODE_FIELD, value="000000")
        self.click(by_locator=self.__VERIFICATION_VERIFY_BUTTON)

    def check_incorrect_code_error(self):
        return self.get_element(by_locator=self.__VERIFICATION_INCORRECT_CODE_ERROR)
