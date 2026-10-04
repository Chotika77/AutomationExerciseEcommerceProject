from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_LINK = (By.CSS_SELECTOR, 'a[href="/view_cart"]')
    CART_ROWS = (By.CSS_SELECTOR, "tr[id^='product-']")
    CART_PRICE = (By.CSS_SELECTOR, ".cart_price")
    CART_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    CART_TOTAL = (By.CSS_SELECTOR, ".cart_total")

    def open_cart(self):
        self.wait_to_be_clickable_click(*self.CART_LINK)

    def assert_cart_has_two_products(self):
        rows = self.find_elements(*self.CART_ROWS)
        assert len(rows) == 2, f"Expected 2 products in the cart, found {len(rows)}"

    def assert_price_quantity_total_present(self):
        rows = self.find_elements(*self.CART_ROWS)
        assert len(rows) == 2, f"Expected 2 products in the cart, found {len(rows)}"

        for row in rows:
            assert row.find_elements(*self.CART_PRICE), "Price cell is missing from a cart row"
            assert row.find_elements(*self.CART_QUANTITY), "Quantity cell is missing from a cart row"
            assert row.find_elements(*self.CART_TOTAL), "Total cell is missing from a cart row"
