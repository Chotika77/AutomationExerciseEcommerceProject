from selenium.webdriver.common.by import By

from pages.base_page import Page


class CheckoutPage(Page):
    PROCEED_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, 'check_out')
    LOGIN_PROMPT = (By.XPATH, "//p[contains(., 'Register / Login account to proceed on checkout.')]")

    def proceed_to_checkout(self):
        self.wait_to_be_clickable_click(*self.PROCEED_TO_CHECKOUT_BUTTON)

    def assert_login_prompt_displayed(self):
        self.wait_for_element_to_appear(*self.LOGIN_PROMPT)
