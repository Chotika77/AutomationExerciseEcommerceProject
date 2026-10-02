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
