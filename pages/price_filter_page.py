from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class PriceFilterPage(Page):
    FILTER_LEFT_BTN = (By. XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[1]/span[1]')
    FILTER_RIGHT_BTN = (By. XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[1]/span[2]')
    FILTER_BTN = (By. XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[2]/button')
    X_BTN_MIN = (By. XPATH, '//*[@id="woocommerce_layered_nav_filters-10"]/ul/li[1]/a')
    X_BTN_MAX = (By. XPATH, '//*[@id="woocommerce_layered_nav_filters-10"]/ul/li/a')
    SHOWING_RESULTS = (By. XPATH, '//*[@id="wrapper"]/div/div/div[2]/p')

    def slide_filter_left(self, *locator):
        actions = ActionChains(self.driver)
        elem1 = self.driver.find_element(*self.FILTER_LEFT_BTN)
        actions.drag_and_drop_by_offset(elem1, 80, 0)
        actions.perform()
        time.sleep(2)

    def slide_filter_right(self, *locator):
        actions = ActionChains(self.driver)
        elem2 = self.driver.find_element(*self.FILTER_RIGHT_BTN)
        actions.drag_and_drop_by_offset(elem2, -60, 0)
        actions.perform()
        time.sleep(4)

    def click_filter_btn(self, *locator):
        self.click(*self.FILTER_BTN)

    def x_active_filters_min(self, *locator):
        self.click(*self.X_BTN_MIN)

    def x_active_filters_max(self, *locator):
        self.click(*self.X_BTN_MAX)

    def verify_price_filter(self, *locator):
        self.driver.find_element(*self.SHOWING_RESULTS)

