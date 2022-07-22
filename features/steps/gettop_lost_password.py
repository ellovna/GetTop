from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from pages.header import Header


@given('Open GetTop page')
def open_get_top(context):
    context.app.main_page.open_main_page()


@when('Click the user icon')
def user_icon(context):
    context.app.header.click_user_icon()


@when('Click Lost your password link')
def click_lost_password(context):
    context.app.reset_password_page.click_lost_password()


@when('User input {email}')
def input_email(context, email):
    context.app.reset_password_page.input_email(email)


@when('Click Reset Password button')
def click_reset_password(context):
    context.app.reset_password_page.click_reset_password()


@then('Verify {text} text is present')
def verify_text_is_shown(context, text):
    context.app.reset_password_page.verify_text_is_shown(text)
