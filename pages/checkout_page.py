from selenium.webdriver.common.by import By

from pages.base_page import Page


class CheckoutPage(Page):
    # Existing locators (already present)
    PROCEED_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, 'check_out')
    LOGIN_PROMPT = (By.XPATH, "//p[contains(., 'Register / Login account to proceed on checkout.')]")
    DELIVERY_ADDRESS = (By.ID, 'address_delivery')
    BILLING_ADDRESS = (By.ID, 'address_invoice')
    ORDER_TABLE = (By.ID, 'cart_info')

    # New locators required by the scenario
    ORDER_TABLE_ROWS = (By.CSS_SELECTOR, "tr[id^='product-']")  # New - represents rows in the order table
    ORDER_MESSAGE = (By.NAME, 'message')  # New - textarea for order comment
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[@href='/payment' and contains(., 'Place Order')]")  # New - proceeds to payment

    # Payment form locators (New)
    NAME_ON_CARD = (By.NAME, 'name_on_card')
    CARD_NUMBER = (By.NAME, 'card_number')
    CVC = (By.NAME, 'cvc')
    EXPIRY_MONTH = (By.NAME, 'expiry_month')
    EXPIRY_YEAR = (By.NAME, 'expiry_year')
    PAY_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="pay-button"]')

    # Order confirmation locators (New)
    ORDER_PLACED = (By.XPATH, "//b[contains(., 'Order Placed!')]")
    ORDER_CONFIRMATION_TEXT = (By.XPATH, "//p[contains(., 'Congratulations! Your order has been confirmed')]")

    # Existing method (already present)
    def proceed_to_checkout(self):
        self.wait_to_be_clickable_click(*self.PROCEED_TO_CHECKOUT_BUTTON)

    # Existing method (already present)
    def assert_login_prompt_displayed(self):
        self.wait_for_element_to_appear(*self.LOGIN_PROMPT)

    # Existing methods (already present)
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

    # New method required by the scenario
    def assert_review_section_displayed(self):
        """New - verify delivery address and order table rows are visible on the review/checkout page"""
        self.wait_for_element_to_appear(*self.DELIVERY_ADDRESS)
        self.wait_for_element_to_appear(*self.ORDER_TABLE_ROWS)

    def enter_order_comment(self, text):
        """New - enter a comment in the order message textarea"""
        self.input_text(text, *self.ORDER_MESSAGE)

    def proceed_to_payment(self, base_url):
        self.driver.get(f"{base_url}/payment")

    def enter_payment_information(self, name, number, cvc, month, year):
        """New - fill the payment form fields with provided values"""
        self.input_text(name, *self.NAME_ON_CARD)
        self.input_text(number, *self.CARD_NUMBER)
        self.input_text(cvc, *self.CVC)
        self.input_text(month, *self.EXPIRY_MONTH)
        self.input_text(year, *self.EXPIRY_YEAR)

    def click_pay_and_confirm_order(self):
        """New - click the Pay and Confirm Order button"""
        self.wait_to_be_clickable_click(*self.PAY_BUTTON)

    def assert_order_placed(self):
        """New - verify the order success indicator is present"""
        self.wait_for_element_to_appear(*self.ORDER_PLACED)

    def assert_order_confirmation_message_displayed(self):
        """New - verify the confirmation paragraph text is visible"""
        self.verify_partial_text('Congratulations! Your order has been confirmed', *self.ORDER_CONFIRMATION_TEXT)
