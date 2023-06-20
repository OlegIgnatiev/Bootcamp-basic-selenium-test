import unittest
from pages.credentials_page import CredentialsPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.verification_page import VerificationPage


class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.credentials_page = CredentialsPage()
        self.forgot_password_page = ForgotPasswordPage()
        self.verification_page = VerificationPage()

        self.credentials_page.get_url(url="https://dev.bullphishid.net/login")

    def test_login_validation(self):

        # Step 1. Click Log In button
        self.credentials_page.click_log_in_button()

        # Step2. Check if email and password fields are required.
        if_email_field_is_required = self.credentials_page.check_if_email_field_required()
        self.assertTrue(if_email_field_is_required)
        if_password_field_is_required = self.credentials_page.check_if_password_field_required()
        self.assertTrue(if_password_field_is_required)

        # Step 3. Input invalid email, incorrect password and click 'Log in'.
        self.credentials_page.input_invalid_email()

        # Step 4. Invalid email error is displayed.
        if_invalid_email_error_is_displayed = self.credentials_page.check_if_invalid_email_error_is_present()
        self.assertTrue(if_invalid_email_error_is_displayed)

        # Step 5. Input valid email and incorrect password. Click 'Log in'.
        self.credentials_page.input_existing_email_incorrect_password()

        # Step 6. Check credentials error is displayed.
        if_credentials_error_is_displayed = self.credentials_page.check_if_check_your_credentials_error()
        self.assertTrue(if_credentials_error_is_displayed)

        # Step 7. Input not existing email and existing password.
        self.credentials_page.input_not_existing_email_existing_password()

        # Step 8. Check credentials error is displayed.
        if_credentials_error_displayed_second = self.credentials_page.check_if_check_your_credentials_error_second()
        self.assertTrue(if_credentials_error_displayed_second)

    def test_2fa_verification(self):
        # Step 1. Input valid email and valid password.
        self.credentials_page.input_valid_credentials()

        # Step 2. Check 'Log in' button is not present.
        if_element_is_present = self.credentials_page.check_if_login_button_is_not_presented_on_the_page()
        self.assertFalse(if_element_is_present)

        # Step 3. Click Verify button
        self.verification_page.click_verify_button()

        # Step 4. Check that verification field is required
        if_authentication_code_is_required = self.verification_page.check_that_verification_field_is_required()
        self.assertTrue(if_authentication_code_is_required)

        # Step 5. Input invalid 2FA code.
        self.verification_page.input_invalid_code()

        # Step 6. Check code must be 6 digits error message displayed.
        if_authentication_code_6_digits = self.verification_page.check_code_must_be_six_digits_error()
        self.assertTrue(if_authentication_code_6_digits)

        # Step 7. Input incorrect 2FA code.
        self.verification_page.input_incorrect_code()

        # Step 8. Check error message displayed.
        if_invalid_authentication_code = self.verification_page.check_incorrect_code_error()
        self.assertTrue(if_invalid_authentication_code)

    def test_reset_password(self):
        # Step 1. Click Forgot Password button.
        self.forgot_password_page.click_forgot_password_button()

        # Step 2. Check if Forgot Password page
        if_forgot_password_page = self.forgot_password_page.check_if_forgot_password_page_opened()
        self.assertTrue(if_forgot_password_page)


        # Step 3. Click Reset button
        self.forgot_password_page.click_reset_button()

        # Step 4. Check that email field required
        if_forgot_email_field_required = self.forgot_password_page.check_if_email_field_required()
        self.assertTrue(if_forgot_email_field_required)

        # Step 5. Input invalid forgot email.
        self.forgot_password_page.input_invalid_forgot_email()

        # Step 6. Check if invalid forgot email error displayed.
        if_invalid_forgot_email = self.forgot_password_page.check_invalid_forgot_email_error_displayed()
        self.assertTrue(if_invalid_forgot_email)

    def TearDown(self) -> None:
        self.credentials_page.quite_driver()


if __name__ == "__main__":
    unittest.main()
