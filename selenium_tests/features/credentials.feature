# Created by oleh.ihnatiev at 11/07/2023
Feature: Credentials feature
  As a user I should see valid error messages on Login page

  @credentials
  Scenario: Login with invalid/ incorrect credentials
  When I type following credentials on Login page and submit
      | username             | password        |
      |                      |                 |
  Then "The email field is required." message displayed on Login page
  When I type following credentials on Login page and submit
      | username             | password        |
      | emaildomain.com      | 123456789       |
  Then "The email must be a valid email address." message displayed on Login page
  When I type following credentials on Login page and submit
      | username             | password        |
      | oleh.admin@email.com | 123456789       |
  Then "Please check your credentials" message displayed on Login page
  When I type following credentials on Login page and submit
      | username             | password        |
      | email@domain.com     | Olegignatiev1!  |
  Then "Please check your credentials" message displayed on Login page

  @mfa
  Scenario: Input invalid/ incorrect 2FA code
  When I type following credentials on Login page and submit
      | username             | password        |
      | Oleh.admin@email.com | Olegignatiev1!  |
  Then Log In button is not present
  When I Input following 2FA code and click Log In
      | mfa_code  |
      |           |
  Then "The authentication code is required." message displayed on MFA page
  When I Input following 2FA code and click Log In
      | mfa_code  |
      | 123456789 |
  Then "The authentication code must be 6 digits." message displayed on MFA page
  When I Input following 2FA code and click Log In
      | mfa_code  |
      | 000000    |
  Then "Invalid authentication code, please try again" message displayed on MFA page
