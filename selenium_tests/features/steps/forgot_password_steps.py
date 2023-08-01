from behave import *
from hamcrest import assert_that, is_


@when("I Click Forgot Password button")
def step_impl(context):
    context.forgot_password_page.click_forgot_password_button()


@then("Forgot Password page opened")
def step_impl(context):
    if_forgot_password_page = context.forgot_password_page.check_if_forgot_password_page_opened()
    assert_that(if_forgot_password_page, is_(True))


@then('"{expected_message}" error displayed on Forgot Password page')
def step_impl(context, expected_message):
    if_authentication_code_is_required = context.forgot_password_page.check_appropriate_error_displayed(expected_text=expected_message)
    assert_that(if_authentication_code_is_required, is_(True))


@when("I Input following Forgot Email and submit")
def step_impl(context):
    forgot_email = context.table[0]["forgot_email"]
    context.forgot_password_page.input_invalid_forgot_email_and_submit(invalid_forgot_email_value=forgot_email)
