from behave import *
from hamcrest import assert_that, is_


@then("Log In button is not present")
def step_impl(context):
    if_element_is_not_present = context.credentials_page.check_if_login_button_is_not_presented_on_the_page()
    assert_that(if_element_is_not_present, is_(True))


@then('"{expected_message}" message displayed on MFA page')
def step_impl(context, expected_message):
    if_authentication_code_is_required = context.verification_page.check_that_appropriate_verification_error(expected_text=expected_message)
    assert_that(if_authentication_code_is_required, is_(True))


@when("I Input following 2FA code and click Log In")
def step_impl(context):
    mfa_code = context.table[0]["mfa_code"]
    context.verification_page.input_security_code_and_submit(security_value=mfa_code)


