from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignupLoginPage(Page):
    LOGIN_HEADING = (By.XPATH, "//h2[contains(., 'Login to your account')]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_USER = (By.XPATH, "//a[contains(., 'Logged in as')]")

    def assert_login_page_displayed(self):
        self.verify_partial_url('/login')
        # self.wait_for_element_to_appear(*self.LOGIN_HEADING)
        # self.wait_for_element_to_appear(*self.EMAIL_FIELD)
        # self.wait_for_element_to_appear(*self.PASSWORD_FIELD)
        # self.wait_for_element_to_appear(*self.LOGIN_BUTTON)

    def assert_login_heading_visible(self):
        self.verify_partial_text('Login to your account', *self.LOGIN_HEADING)

    def assert_email_and_password_fields_visible(self):
        self.wait_for_element_to_appear(*self.EMAIL_FIELD)
        self.wait_for_element_to_appear(*self.PASSWORD_FIELD)

    def assert_login_fields_visible(self):
        self.assert_email_and_password_fields_visible()

    def assert_login_button_visible(self):
        self.wait_for_element_to_appear(*self.LOGIN_BUTTON)

    def enter_email(self, email):
        self.wait_to_be_clickable(*self.EMAIL_FIELD)
        self.input_text(email, *self.EMAIL_FIELD)

    def enter_password(self, password):
        self.wait_to_be_clickable(*self.PASSWORD_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_login(self):
        self.wait_to_be_clickable_click(*self.LOGIN_BUTTON)

    def log_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def assert_logged_in(self):
        self.wait_for_element_to_appear(*self.LOGGED_IN_USER)
        self.verify_partial_text('Logged in as', *self.LOGGED_IN_USER)



