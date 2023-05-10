Feature: Log in validation
  Application should show validation messages if user input incorrect credentials and 2FA code

  Scenario: Log in validation messages
    When I type invalid email and incorrect password and click [Log In] button
    Then I see error message “The email must be a valid email address”
    When I type existing email and incorrect password and click [Log In] button
    Then I see error message “Please check your credentials and domain”
    When I type not existing email and existing password and click [Log In] button
    Then I see error message “Please check your credentials and domain”
    When I type valid email and valid password and click [Log in button
    Then Verification page opened and [Log in] button not present
    When I input 2FA code more then 6 digits and click [Verify] button
    Then I see error message “The authentication code must be 6 digits”
    When I input incorrect 2FA code and click [Verify] button
    Then I see error message “Invalid authentication code, please try again
