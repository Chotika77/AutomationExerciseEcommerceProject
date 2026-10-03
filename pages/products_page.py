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

