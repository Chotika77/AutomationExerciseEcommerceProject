from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductsPage(Page):
    ALL_PRODUCTS_HEADING = (By.XPATH, "//h2[contains(., 'All Products')]")
    VIEW_PRODUCT_LINK = (By.CSS_SELECTOR, 'a[href="/product_details/1"]')
    SEARCH_INPUT = (By.ID, 'search_product')
    SEARCH_BUTTON = (By.ID, 'submit_search')
    SEARCH_RESULTS_HEADING = (By.XPATH, "//h2[contains(., 'Searched Products')]")
    SEARCH_RESULT_NAMES = (By.CSS_SELECTOR, ".productinfo p")

    def assert_catalog_displayed(self):
        self.wait_for_element_to_appear(*self.ALL_PRODUCTS_HEADING)

    def open_product(self, base_url):
        self.driver.get(f"{base_url}/product_details/1")

        # link = self.wait_for_element_to_appear(*self.VIEW_PRODUCT_LINK)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        # self.wait_to_be_clickable_click(*self.VIEW_PRODUCT_LINK)
        print("AFTER CLICK URL:", self.driver.current_url)

    def search_for_product(self, search_term):
        self.wait_to_be_clickable(*self.SEARCH_INPUT)
        self.input_text(search_term, *self.SEARCH_INPUT)
        self.wait_to_be_clickable_click(*self.SEARCH_BUTTON)

    def assert_searched_products_displayed(self):
        self.wait_for_element_to_appear(*self.SEARCH_RESULTS_HEADING)

    def assert_products_matching_search_term(self, search_term):
        product_names = self.find_elements(*self.SEARCH_RESULT_NAMES)

        for product in product_names:
            if search_term.lower() in product.text.lower():
                return

        assert False, f'No product matched "{search_term}"'

    # New methods needed by the "add multiple products to cart" scenario
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-image-wrapper")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "a.add-to-cart")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button.close-modal")

    def add_two_products_to_cart(self):
        cards = self.find_elements(*self.PRODUCT_CARDS)[:2]
        for card in cards:
            button = card.find_element(*self.ADD_TO_CART_BUTTONS)
            self.driver.execute_script("arguments[0].click();", button)
            self.wait_to_be_clickable_click(*self.CONTINUE_SHOPPING_BUTTON)

        buttons = self.find_elements(*self.ADD_TO_CART_BUTTONS)
        print("BUTTON 2 ID:", buttons[1].get_attribute("data-product-id"))
        self.driver.execute_script("arguments[0].click();", buttons[1])
        self.wait_to_be_clickable_click(*self.CONTINUE_SHOPPING_BUTTON)


