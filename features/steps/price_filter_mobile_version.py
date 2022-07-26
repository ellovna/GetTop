import time

from selenium.webdriver.common.by import By
from behave import when, given, then


@when('Click on IPHONE btn')
def click_iphone(context):
    context.app.header.click_iphone_button()


@when('Click on Menu Button')
def click_menu(context):
    context.app.header.click_menu_button()


@when('Click on Filter')
def click_filter_btn(context):
    context.app.price_filter_mobile_page.click_filter()


@when('Slide Left Filter')
def slide_filter_left_btn(context):
    context.app.price_filter_mobile_page.slide_filter_left()


@when('Slide Right Filter')
def slide_filter_right_btn(context):
    context.app.price_filter_mobile_page.slide_filter_right()


@when('Click on Filter Btn')
def click_filter_btn(context):
    context.app.price_filter_mobile_page.click_filter_btn()


@when('Click on X from Active filters Min')
def x_active_f_min(context):
    context.app.price_filter_mobile_page.x_active_filters_min()


@when('Click on X from Active filters Max')
def x_active_f_max(context):
    context.app.price_filter_mobile_page.x_active_filters_max()


@then('Verify that Mobile Price Filter Slider handle position resents')
def verify_price_filter(context):
    context.app.price_filter_mobile_page.verify_mobile_filter()

