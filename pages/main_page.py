from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')
    PRODUCTS_LINK = (By.CSS_SELECTOR, 'a[href="/products"]')

    def open(self, url):
        self.driver.get(url)

    def open_signup_login_page(self):
        self.wait_to_be_clickable_click(*self.SIGNUP_LOGIN_LINK)

    def open_products_page(self, base_url):
        self.driver.get(f"{base_url}/products")
        # self.wait_to_be_clickable_click(*self.PRODUCTS_LINK)