from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from pages.header import Header

from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from pages.header import Header


@when('Click Login')
def click_login(context):
    context.app.reset_password_mobile_page.click_login()


@when('Click Lost your password')
def click_lost_psswrd(context):
    context.app.reset_password_mobile_page.click_lost_psswrd()


@when('Input {email}')
def input_email(context, email):
    context.app.reset_password_mobile_page.input_email(email)


@when('Click Reset Password button')
def click_reset_password(context):
    context.app.reset_password_mobile_page.click_reset_password()


@then('Verify {text} text is present')
def verify_text_is_shown(context, text):
    context.app.reset_password_mobile_page.verify_text_is_shown(text)


