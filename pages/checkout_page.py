from selenium.webdriver.common.by import By

from pages.base_page import Page


class CheckoutPage(Page):
    PROCEED_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, 'check_out')
    LOGIN_PROMPT = (By.XPATH, "//p[contains(., 'Register / Login account to proceed on checkout.')]")
    DELIVERY_ADDRESS = (By.ID, 'address_delivery')
    BILLING_ADDRESS = (By.ID, 'address_invoice')
    ORDER_TABLE = (By.ID, 'cart_info')

    def proceed_to_checkout(self):
        self.wait_to_be_clickable_click(*self.PROCEED_TO_CHECKOUT_BUTTON)

    def assert_login_prompt_displayed(self):
        self.wait_for_element_to_appear(*self.LOGIN_PROMPT)

    def assert_delivery_address_matches_registered_user(self, expected_name, expected_address):
        address_block = self.wait_for_element_to_appear(*self.DELIVERY_ADDRESS)
        address_text = ' '.join(address_block.text.split())
        assert expected_name in address_text, f"Expected {expected_name} in delivery address, got {address_text}"
        assert expected_address in address_text, f"Expected {expected_address} in delivery address, got {address_text}"

    def assert_billing_address_matches_registered_user(self, expected_name, expected_address):
        address_block = self.wait_for_element_to_appear(*self.BILLING_ADDRESS)
        address_text = ' '.join(address_block.text.split())
        assert expected_name in address_text, f"Expected {expected_name} in billing address, got {address_text}"
        assert expected_address in address_text, f"Expected {expected_address} in billing address, got {address_text}"

    def assert_order_details_match_cart(self):
        order_table = self.wait_for_element_to_appear(*self.ORDER_TABLE)
        product_row = order_table.find_element(By.CSS_SELECTOR, "tr[id^='product-']")

        product_name = product_row.find_element(By.CSS_SELECTOR, '.cart_description h4 a').text.strip()
        product_price = product_row.find_element(By.CSS_SELECTOR, '.cart_price p').text.strip()
        product_quantity = product_row.find_element(By.CSS_SELECTOR, '.cart_quantity button').text.strip()
        product_total = product_row.find_element(By.CSS_SELECTOR, '.cart_total_price').text.strip()
        total_amount = order_table.find_element(By.XPATH, ".//td[normalize-space()='Total Amount']/following-sibling::td/p").text.strip()

        assert product_name == 'Blue Top', f'Expected product Blue Top in checkout, got {product_name}'
        assert product_price == 'Rs. 500', f'Expected product price Rs. 500, got {product_price}'
        assert product_quantity == '1', f'Expected quantity 1, got {product_quantity}'
        assert product_total == 'Rs. 500', f'Expected product total Rs. 500, got {product_total}'
        assert total_amount == 'Rs. 500', f'Expected total amount Rs. 500, got {total_amount}'
