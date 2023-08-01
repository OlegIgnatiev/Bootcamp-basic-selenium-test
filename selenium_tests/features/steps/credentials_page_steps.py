from behave import *
from hamcrest import assert_that, is_


@when("I type following credentials on Login page and submit")
def step_impl(context):
    username = context.table[0]["username"]
    password = context.table[0]["password"]
    context.credentials_page.input_credentials_and_submit(login_value=username, password_value=password)


@then('"{expected_message}" message displayed on Login page')
def step_impl(context, expected_message: str):
    if_email_field_is_required = context.credentials_page.check_if_appropriate_error_displayed(expected_text=expected_message)
    assert_that(if_email_field_is_required, is_(True))


@when("I Input valid email and valid password and click Log In")
def step_impl(context):
    context.credentials_page.input_credentials_and_submit(login_value='Oleh.admin@email.com', password_value='Olegignatiev1!')



