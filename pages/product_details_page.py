from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductDetailsPage(Page):
    PRODUCT_DETAILS_PANEL = (By.CSS_SELECTOR, '.product-information')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-information h2')
    PRODUCT_CATEGORY = (By.XPATH, "//div[contains(@class,'product-information')]//p[contains(.,'Category:')]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product-information')]//span/span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//div[contains(@class,'product-information')]//p[contains(.,'Availability:')]")
    PRODUCT_CONDITION = (By.XPATH, "//div[contains(@class,'product-information')]//p[contains(.,'Condition:')]")
    PRODUCT_BRAND = (By.XPATH, "//div[contains(@class,'product-information')]//p[contains(.,'Brand:')]")
    QUANTITY_INPUT = (By.ID, 'quantity')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-default.cart')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, 'button.close-modal')

    FIELD_LOCATORS = {
        'name': PRODUCT_NAME,
        'category': PRODUCT_CATEGORY,
        'price': PRODUCT_PRICE,
        'availability': PRODUCT_AVAILABILITY,
        'condition': PRODUCT_CONDITION,
        'brand': PRODUCT_BRAND,
    }

    def assert_field_present(self, field_name):
        self.wait_for_element_to_appear(*self.FIELD_LOCATORS[field_name])

    def assert_product_details_panel_displayed(self):
        self.wait_for_element_to_appear(*self.PRODUCT_DETAILS_PANEL)

    def set_quantity(self, quantity):
        quantity_input = self.wait_for_element_to_appear(*self.QUANTITY_INPUT)
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def add_to_cart(self):
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_BUTTON)
        try:
            self.wait_to_be_clickable_click(*self.CONTINUE_SHOPPING_BUTTON)
        except Exception:
            pass
