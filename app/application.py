from pages.base_page import Page
from pages.main_page import MainPage
from pages.signup_login_page import SignupLoginPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.signup_login_page = SignupLoginPage(driver)
        self.products_page = ProductsPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)