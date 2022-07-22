from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


bs_user = "ellaellovna_HO7acT"
bs_pw = "8xXmA8qytbYmCz9Y8Td9"

# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

def browser_init(context, lost_password):
    # options = Options()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    context.driver = webdriver.Chrome(executable_path='/Users/ellaoroz/Desktop/chromedriver')
    #context.driver = webdriver.Chrome(executable_path='/Users/ellaoroz/Desktop/chromedriver', chrome_options=options)
    #
    # options = FirefoxOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    # context.driver = webdriver.Firefox(executable_path='/Users/ellaoroz/Desktop/geckodriver', options=options)
    #
    # desired_cap = {
    #     "browser": "Edge",
    #     "browser_version": "103.0",
    #     "os": "Windows",
    #     "os_version": "11",
    #     "name": lost_password
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)

    context.app = Application(context.driver)
    # context.app.main_page.open_main_page()


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()