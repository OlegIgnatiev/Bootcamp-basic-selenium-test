# Created by oleh.ihnatiev at 11/07/2023
Feature: Forgot password feature
  As a user I should see valid error messages when I reset password

  @forgot_password
  Scenario: Reset password
  When I Click Forgot Password button
  Then Forgot Password page opened
  When I Input following Forgot Email and submit
      | forgot_email    |
      |                 |
  Then "The email field is required." error displayed on Forgot Password page
  When I Input following Forgot Email and submit
      | forgot_email    |
      | emaildomain.com |
  Then "The email must be a valid email address." error displayed on Forgot Password page
