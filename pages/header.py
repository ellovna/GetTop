from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    USER_ICON = (By. CSS_SELECTOR, "i.icon-user")

    def click_user_icon(self):
        self.click(*self.USER_ICON)








