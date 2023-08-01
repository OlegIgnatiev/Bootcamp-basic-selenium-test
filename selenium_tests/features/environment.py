from pages.credentials_page import CredentialsPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.verification_page import VerificationPage
from utils.capabilities_util import get_driver


def before_all(context):
    # setup global variables
    setup = context.config.userdata
    context.driver = get_driver(browser=setup["browser"])
    # setup page_objects
    context.credentials_page = CredentialsPage(context=context)
    context.forgot_password_page = ForgotPasswordPage(context=context)
    context.verification_page = VerificationPage(context=context)
    # open application under test
    context.credentials_page.get_url(url="https://dev.bullphishid.net/login")


def after_scenario(context, scenario):
    context.credentials_page.clear_cookies()


def after_all(context):
    context.credentials_page.quite_driver()
