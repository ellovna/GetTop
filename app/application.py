from pages.main_page import MainPage
from pages.header import Header
from selenium import webdriver
from pages.reset_password_page import ResetPasswordPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.reset_password_page = ResetPasswordPage(self.driver)











