from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class VerificationPage(BasePage):

    __VERIFICATION_CODE_FIELD = (By.XPATH, '//input[@id ="code"]')
    __VERIFICATION_VERIFY_BUTTON = (By.XPATH, '//button[text() ="Verify"]')
    __VERIFICATION_SIX_DIGITS_ERROR = (By.XPATH, '//div[text() ="The authentication code must be 6 digits."]')
    __VERIFICATION_INCORRECT_CODE_ERROR = (By.XPATH, '//div[text() ="Invalid authentication code, please try again"]')

    def input_invalid_code(self):
        self.fill(self.__VERIFICATION_CODE_FIELD, "123456789")
        self.click(self.__VERIFICATION_VERIFY_BUTTON)

    def check_code_must_be_six_digits_error(self):
        return self.get_element(self.__VERIFICATION_SIX_DIGITS_ERROR)

    def input_incorrect_code(self):
        self.clear(self.__VERIFICATION_CODE_FIELD)
        self.fill(self.__VERIFICATION_CODE_FIELD, "000000")
        self.click(self.__VERIFICATION_VERIFY_BUTTON)

    def check_incorrect_code_error(self):
        return self.get_element(self.__VERIFICATION_INCORRECT_CODE_ERROR)

