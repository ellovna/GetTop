from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class PriceFilterMobilePage(Page):
    FILTER = (By.CSS_SELECTOR, ".category-filtering.category-filter-row.show-for-medium i.icon-menu")
    # FILTER_LEFT = (By. XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[1]/span[1]')
    FILTER_LEFT = (By.CSS_SELECTOR, "span[style='left: 0%;']")
    FILTER_RIGHT = (By. XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[1]/span[2]')
    FILTER_BTN = (By. XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[2]/button')
    X_BTN_MIN = (By. XPATH, '//*[@id="wrapper"]/div/div/div[1]/div[2]/div/div/ul/li[1]/a')
    X_BTN_MAX = (By. XPATH, '//*[@id="wrapper"]/div/div/div[1]/div[2]/div/div/ul/li/a')
    SHOWING_RESULTS = (By. XPATH, '//*[@id="wrapper"]/div/div/div[1]/div[2]/a/strong')

    def click_filter(self):
        # self.click(*self.FILTER)
        self.wait_for_element_click(*self.FILTER)
        time.sleep(5)

    def slide_filter_left(self, *locator):
        self.wait_for_element_appear(*self.FILTER_LEFT)
        actions = ActionChains(self.driver)
        elem1 = self.driver.find_element(*self.FILTER_LEFT)
        actions.drag_and_drop_by_offset(elem1, 20, 0)
        actions.perform()
        # time.sleep(2)

    def slide_filter_right(self, *locator):
        self.wait_for_element_appear(*self.FILTER_RIGHT)
        actions = ActionChains(self.driver)
        elem2 = self.driver.find_element(*self.FILTER_RIGHT)
        actions.drag_and_drop_by_offset(elem2, -30, 0)
        actions.perform()
        # time.sleep(4)

    def click_filter_btn(self, *locator):
        self.click(*self.FILTER_BTN)

    def x_active_filters_min(self, *locator):
        self.click(*self.X_BTN_MIN)

    def x_active_filters_max(self, *locator):
        self.click(*self.X_BTN_MAX)

    def verify_mobile_filter(self, *locator):
        self.driver.find_element(*self.SHOWING_RESULTS)
