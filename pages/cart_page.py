from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class CartPage(Page):
    CART_LINK = (By.CSS_SELECTOR, 'a[href="/view_cart"]')
    CART_ROWS = (By.CSS_SELECTOR, "tr[id^='product-']")
    CART_PRICE = (By.CSS_SELECTOR, ".cart_price")
    CART_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    CART_TOTAL = (By.CSS_SELECTOR, ".cart_total")
    CART_DELETE_BUTTON = (By.CSS_SELECTOR, 'a.cart_quantity_delete')
    # CART_EMPTY_MESSAGE = (By.XPATH, "//b[contains(., 'Cart is empty!')]")

    def open_cart(self):
        self.wait_to_be_clickable_click(*self.CART_LINK)

    def remove_product_from_cart(self):
        delete_button = self.wait_for_element_to_appear(*self.CART_DELETE_BUTTON)
        self.driver.execute_script("arguments[0].click();", delete_button)

    def assert_product_removed_from_cart(self):
        self.wait.until(lambda d: len(d.find_elements(*self.CART_ROWS)) == 0)



    # def assert_product_removed_from_cart(self):
    #     rows = self.find_elements(*self.CART_ROWS)
    #     assert len(rows) == 0, f"Expected cart to be empty after removal, found {len(rows)} product rows"
    #     self.wait_for_element_to_appear(*self.CART_EMPTY_MESSAGE)

    # def assert_product_removed_from_cart(self):
    #     self.wait_to_be_clickable_click(*self.CART_DELETE_BUTTON)
    #     self.wait.until(
    #         EC.invisibility_of_element_located(self.CART_ROWS)
    #     )

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

    def assert_product_quantity(self, expected_quantity):
        rows = self.find_elements(*self.CART_ROWS)
        assert rows, "No products were found in the cart"

        actual_quantity = rows[0].find_element(*self.CART_QUANTITY).text.strip()
        assert actual_quantity == str(expected_quantity), (
            f"Expected quantity {expected_quantity}, got {actual_quantity}"
        )
