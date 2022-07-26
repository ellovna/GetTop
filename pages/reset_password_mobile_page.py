from selenium.webdriver.common.by import By
from pages.base_page import Page


class ResetPasswordMobilePage(Page):
    LOGIN = (By.CSS_SELECTOR, ".header-account-title")
    LOST_PSSWRD = (By. XPATH, '//*[@id="main"]/div[2]/div/div/div[2]/div/form/p[4]/a')
    USER_EMAIL = (By. XPATH, '//*[@id="user_login"]')
    RESET_PASSWORD_BTN = (By. XPATH, '//*[@id="main"]/div[2]/div/div/form/p[3]/button')
    TEXT = (By. XPATH, '//*[@id="wrapper"]/ul/li/div')

    def click_login(self):
        self.click(*self.LOGIN)

    def click_lost_psswrd(self):
        self.click(*self.LOST_PSSWRD)

    def input_email(self, email, *locator):
        self.input_text(email, *self.USER_EMAIL)

    def click_reset_password(self):
        self.click(*self.RESET_PASSWORD_BTN)

    def verify_text_is_shown(self, text, *locator):
        self.verify_text(text, *self.TEXT)

