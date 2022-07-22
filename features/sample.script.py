from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ellaoroz/Desktop/chromedriver')
driver.maximize_window()

driver.get('https://gettop.us/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys()

sleep(4)