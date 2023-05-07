import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.credentials_page import CredentialsPage
from pages.verification_page import VerificationPage


class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get(url="https://dev.bullphishid.net/login")

        self.credentials_page = CredentialsPage(driver=self.driver)
        self.verification_page = VerificationPage(driver=self.driver)

    def test_login_validation(self):
        # Step 1. Input invalid email, incorrect password and click 'Log in'.
        self.credentials_page.input_invalid_email()

        # Step 2. Invalid email error is displayed.
        if_invalid_email_error = self.credentials_page.check_if_invalid_email_error_is_present()
        self.assertTrue(if_invalid_email_error)

        # Step 3. Input existing email and incorrect password. Click 'Log in'.
        self.credentials_page.input_existing_email_incorrect_password()

        # Step 4. Check credentials error is displayed.
        if_check_your_credentials_error = self.credentials_page.check_if_check_your_credentials_error()
        self.assertTrue(if_check_your_credentials_error)

        # Step 5. Input not existing email and existing password.
        self.credentials_page.input_not_existing_email_existing_password()

        # Step 6. Check credentials error is displayed.
        if_check_your_credential_error = self.credentials_page.check_if_check_your_credentials_error_second()
        self.assertTrue(if_check_your_credential_error)

        # Step 7. Input valid email and valid password.
        self.credentials_page.input_valid_credentials()

        # Step 8. Check 'Log in' button is not present.
        if_element_is_present = self.credentials_page.check_if_login_button_is_not_presented_on_the_page()
        self.assertFalse(if_element_is_present)

        # Step 9. Input invalid 2FA code.
        self.verification_page.input_invalid_code()

        # Step 10. Check error message displayed.
        code_must_be_six_digits_error = self.verification_page.check_code_must_be_six_digits_error()
        self.assertTrue(code_must_be_six_digits_error)

        # Step 11. Input incorrect 2FA code.
        self.verification_page.input_incorrect_code()

        # Step 12. Check error message displayed.
        incorrect_code_error = self.verification_page.check_incorrect_code_error()
        self.assertTrue(incorrect_code_error)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
