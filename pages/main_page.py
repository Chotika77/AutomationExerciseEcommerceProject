from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class MainPage(Page):
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')

    def open(self, url):
        self.driver.get(url)

    def open_signup_login_page(self):
        self.wait_to_be_clickable_click(*self.SIGNUP_LOGIN_LINK)