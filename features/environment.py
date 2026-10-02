from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
load_dotenv()
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application
import os


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)



    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
    #
    # bs_user = 'davitchkuaseli_KSk4vy'
    # bs_key = 'yxxfCf9AtwmzcmQHxxjm'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "10",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    # #
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

def before_all(context):
    context.base_url = os.getenv("BASE_URL")
    context.email = os.getenv("TEST_USER_EMAIL")
    context.password = os.getenv("TEST_USER_PASSWORD")


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    if getattr(context, "driver", None):
        context.app.main_page.close_extra_windows()
    print('\nStarted step: ', step)



def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
