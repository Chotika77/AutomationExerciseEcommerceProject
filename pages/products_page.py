from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductsPage(Page):
    ALL_PRODUCTS_HEADING = (By.XPATH, "//h2[contains(., 'All Products')]")
    VIEW_PRODUCT_LINK = (By.CSS_SELECTOR, 'a[href="/product_details/1"]')


    def assert_catalog_displayed(self):
        self.wait_for_element_to_appear(*self.ALL_PRODUCTS_HEADING)

    def open_product(self, base_url):
        self.driver.get(f"{base_url}/product_details/1")

        # link = self.wait_for_element_to_appear(*self.VIEW_PRODUCT_LINK)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        # self.wait_to_be_clickable_click(*self.VIEW_PRODUCT_LINK)
        print("AFTER CLICK URL:", self.driver.current_url)

