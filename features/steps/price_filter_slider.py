from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from pages.header import Header
from pages.base_page import Page


@when('Click on IPHONE button')
def click_iphone(context):
    context.app.header.click_iphone_button()


@when('Slide Left Filter Button')
def slide_left_btn(context):
    context.app.price_filter_page.slide_filter_left()


@when('Slide Right Filter Button')
def slide_right_btn(context):
    context.app.price_filter_page.slide_filter_right()


@when('Click on Filter Button')
def click_filter_btn(context):
    context.app.price_filter_page.click_filter_btn()


@when('Click on closing X from Active filters Min')
def x_active_filters_min(context):
    context.app.price_filter_page.x_active_filters_min()


@when('Click on closing X from Active filters Max')
def x_active_filters_max(context):
    context.app.price_filter_page.x_active_filters_max()


@then('Verify that Price Filter Slider handle position resents')
def verify_price_filter(context):
    context.app.price_filter_page.verify_price_filter()

