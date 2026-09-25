from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_INPUT = (By.ID, 'search_product')
    SEARCH_BUTTON = (By.ID, 'submit_search')
    SEARCH_RESULTS_HEADING = (By.XPATH, "//h2[contains(., 'Searched Products')]")
    PRODUCT_CARDS = (By.CSS_SELECTOR, '.product-image-wrapper')

    def type_search_query(self, keyword):
        self.wait_to_be_clickable(*self.SEARCH_INPUT)
        self.input_text(keyword, *self.SEARCH_INPUT)

    def press_enter_in_search(self):
        self.find_element(*self.SEARCH_INPUT).send_keys('\n')

    def assert_results_page_displayed(self):
        self.wait_for_element_to_appear(*self.SEARCH_RESULTS_HEADING)

    def are_product_cards_valid(self):
        cards = self.find_elements(*self.PRODUCT_CARDS)
        assert cards, 'No search result cards were found.'
