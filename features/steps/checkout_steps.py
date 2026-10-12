from behave import when, then


@when('the user proceeds to checkout')
def step_impl(context):
    context.app.checkout_page.proceed_to_checkout()


@then('the user should be prompted to register or log in')
def step_impl(context):
    context.app.checkout_page.assert_login_prompt_displayed()


@then('the delivery address should match the registered user address')
def step_impl(context):
    context.app.checkout_page.assert_delivery_address_matches_registered_user(
        context.checkout_name,
        context.checkout_address,
    )


@then('the billing address should match the registered user address')
def step_impl(context):
    context.app.checkout_page.assert_billing_address_matches_registered_user(
        context.checkout_name,
        context.checkout_address,
    )


@then('the order details should match the shopping cart')
def step_impl(context):
    context.app.checkout_page.assert_order_details_match_cart()


# --- New step definitions for "Registered user can complete an order successfully" scenario ---
@when('reviews the delivery and order information')
def step_impl(context):
    """Verify the delivery address and order table are visible on the review/checkout page"""
    context.app.checkout_page.assert_review_section_displayed()


@when('enters an order comment')
def step_impl(context):
    context.app.checkout_page.enter_order_comment("Please leave the package at the door")



@when('proceeds to payment')
def step_impl(context):
    context.app.checkout_page.proceed_to_payment(context.base_url)


@when('enters valid payment information')
def step_impl(context):
    print("URL:", context.driver.current_url)
    context.app.checkout_page.enter_payment_information(
        "Test User", "4242424242424242", "311", "12", "2030"
    )


@when('confirms the order')
def step_impl(context):
    context.app.checkout_page.click_pay_and_confirm_order()


@then('the order should be placed successfully')
def step_impl(context):
    context.app.checkout_page.assert_order_placed()


@then('an order confirmation message should be displayed')
def step_impl(context):
    context.app.checkout_page.assert_order_confirmation_message_displayed()
