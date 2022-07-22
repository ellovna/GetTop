from pages.base_page import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage(Page):

    def open_main_page(self):
        self.open_page('https://gettop.us/')

