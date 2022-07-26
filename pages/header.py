from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    USER_ICON = (By. CSS_SELECTOR, "i.icon-user")
    IPHONE_BTN = (By.XPATH, '//*[@id="menu-item-469"]/a')

    def click_user_icon(self):
        self.click(*self.USER_ICON)

    def click_iphone_button(self):
        self.click(*self.IPHONE_BTN)








