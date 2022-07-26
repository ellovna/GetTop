from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    USER_ICON = (By. CSS_SELECTOR, "i.icon-user")
    IPHONE_BTN = (By.XPATH, '//*[@id="main-menu"]/div/ul/li[3]/a')
    # MENU = (By. XPATH, '//i[@class="icon-menu"]')
    MENU = (By. XPATH, '//*[@id="masthead"]/div[1]/div[2]/ul/li/a/i')

    def click_user_icon(self):
        self.click(*self.USER_ICON)

    def click_iphone_button(self):
        self.click(*self.IPHONE_BTN)

    def click_menu_button(self):
        self.click(*self.MENU)









