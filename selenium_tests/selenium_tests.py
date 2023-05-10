import unittest

from pages.credentials_page import CredentialsPage
from pages.verification_page import VerificationPage


class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.credentials_page = CredentialsPage()
        self.verification_page = VerificationPage()
        self.credentials_page.open_url("https://dev.bullphishid.net/login")

    def test_login_validation(self):
        # When I type invalid email and incorrect password and click [Log In] button,
        self.credentials_page.input_invalid_email()

        # Then I see error message “The email must be a valid email address”.
        if_invalid_email_error = self.credentials_page.check_if_invalid_email_error_is_present()
        self.assertTrue(if_invalid_email_error)

        # When I type existing email and incorrect password and click [Log In] button,
        self.credentials_page.input_existing_email_incorrect_password()

        # Then I see error message “Please check your credentials and domain”.
        if_check_your_credentials_error = self.credentials_page.check_if_check_your_credentials_error()
        self.assertTrue(if_check_your_credentials_error)

        # When I type not existing email and existing password and click [Log In] button,
        self.credentials_page.input_not_existing_email_existing_password()

        # Then I see error message “Please check your credentials and domain”.
        if_check_your_credential_error = self.credentials_page.check_if_check_your_credentials_error_second()
        self.assertTrue(if_check_your_credential_error)

        # When I type valid email and valid password and click [Log in button,
        self.credentials_page.input_valid_credentials()

        # Then Verification page opened and [Log in] button not present.
        if_element_is_present = self.credentials_page.check_if_login_button_is_not_presented_on_the_page()
        self.assertFalse(if_element_is_present)

        # When I input 2FA code more then 6 digits and click [Verify] button,
        self.verification_page.input_invalid_code()

        # Then I see error message “The authentication code must be 6 digits”.
        code_must_be_six_digits_error = self.verification_page.check_code_must_be_six_digits_error()
        self.assertTrue(code_must_be_six_digits_error)

        # When I input incorrect 2FA code and click [Verify] button,
        self.verification_page.input_incorrect_code()

        # Then I see error message “Invalid authentication code, please try again”.
        incorrect_code_error = self.verification_page.check_incorrect_code_error()
        self.assertTrue(incorrect_code_error)

    def tearDown(self) -> None:
        self.credentials_page.quite_driver()


if __name__ == "__main__":
    unittest.main()
