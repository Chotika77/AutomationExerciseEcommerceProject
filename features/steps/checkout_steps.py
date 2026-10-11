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
