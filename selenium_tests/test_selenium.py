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

    def test_login_validation_credentials(self):

        # Step 1. When I click Log In button with empty login and password fields on Login page
        self.credentials_page.click_log_in_button()

        # Step2. Then I see the messages that email and password fields are required on Login page
        """
        Check that email field required.
        """
        if_email_field_is_required = self.credentials_page.check_if_appropriate_error_displayed(expected_text="The email field is required.")
        self.assertTrue(if_email_field_is_required)
        """
        Check that Password field required.
        """
        if_password_field_is_required = self.credentials_page.check_if_appropriate_error_displayed(expected_text="The password field is required.")
        self.assertTrue(if_password_field_is_required)

        # Step 3. When I input invalid email, incorrect password and click Log in on Login page
        self.credentials_page.input_credentials_and_submit(login_value='emaildomain.com', password_value='123456789')

        # Step 4. Then I see that invalid email error is displayed on Login page
        if_invalid_email_error_is_displayed = self.credentials_page.check_if_appropriate_error_displayed(expected_text="The email must be a valid email address.")
        self.assertTrue(if_invalid_email_error_is_displayed)

        # Step 5. When I input valid email and incorrect password and Click Log in on Login page
        self.credentials_page.input_credentials_and_submit(login_value='oleh.admin@email.com', password_value='123456789')

        # Step 6. Then I see that credentials error is displayed on Login page
        if_credentials_error_is_displayed = self.credentials_page.check_if_appropriate_error_displayed(expected_text="Please check your credentials")
        self.assertTrue(if_credentials_error_is_displayed)

        # Step 7. When I input not existing email and existing password on Login page
        self.credentials_page.input_credentials_and_submit(login_value='email@domain.com', password_value='Olegignatiev1!')

        # Step 8. Then I see that credentials error is displayed on Login page
        if_credentials_error_displayed_second = self.credentials_page.check_if_appropriate_error_displayed(expected_text="Please check your credentials")
        self.assertTrue(if_credentials_error_displayed_second)

    def test_2fa_verification(self):
        # Step 1. When I Input valid email and valid password and click Log In
        self.credentials_page.input_credentials_and_submit(login_value='Oleh.admin@email.com', password_value='Olegignatiev1!')

        # Step 2. Then Log in button is not present
        if_element_is_present = self.credentials_page.check_if_login_button_is_not_presented_on_the_page()
        self.assertFalse(if_element_is_present)

        # Step 3. When I click Verify button and 2FA field is empty
        self.verification_page.click_verify_button()

        # Step 4. Then I see that verification field is required
        if_authentication_code_is_required = self.verification_page.check_that_appropriate_verification_error(expected_text="The authentication code is required.")
        self.assertTrue(if_authentication_code_is_required)

        # Step 5. When I Input invalid 2FA code and click Log In
        self.verification_page.input_security_code_and_submit(security_value='123456789')

        # Step 6. Then I see that code must be 6 digits error message displayed
        if_authentication_code_6_digits = self.verification_page.check_that_appropriate_verification_error(expected_text="The authentication code must be 6 digits.")
        self.assertTrue(if_authentication_code_6_digits)

        # Step 7. When I Input incorrect 2FA code and click Log In
        self.verification_page.input_security_code_and_submit(security_value='000000')

        # Step 8. Then Invalid code error message displayed
        if_invalid_authentication_code = self.verification_page.check_that_appropriate_verification_error(expected_text="Invalid authentication code, please try again")
        self.assertTrue(if_invalid_authentication_code)

    def test_reset_password(self):
        # Step 1. When I Click Forgot Password button
        self.forgot_password_page.click_forgot_password_button()

        # Step 2. Then Forgot Password page opened
        if_forgot_password_page = self.forgot_password_page.check_if_forgot_password_page_opened()
        self.assertTrue(if_forgot_password_page)

        # Step 3. When email field is empty and I Click Reset button
        self.forgot_password_page.click_reset_button()

        # Step 4. Then I see that email field required
        if_forgot_email_field_required = self.forgot_password_page.check_appropriate_error_displayed(expected_text="The email field is required.")
        self.assertTrue(if_forgot_email_field_required)

        # Step 5. When I Input invalid forgot email
        self.forgot_password_page.input_invalid_forgot_email_and_submit(invalid_forgot_email_value='emaildomain.com')

        # Step 6. Then I see that invalid forgot email error displayed
        if_invalid_forgot_email = self.forgot_password_page.check_appropriate_error_displayed(expected_text="The email must be a valid email address.")
        self.assertTrue(if_invalid_forgot_email)

    def TearDown(self) -> None:
        self.credentials_page.quite_driver()


if __name__ == "__main__":
    unittest.main()
