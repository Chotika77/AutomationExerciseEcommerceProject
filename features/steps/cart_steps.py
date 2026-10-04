from behave import when, then


@when('the user adds two different products to the cart')
def step_impl(context):
    context.app.products_page.add_two_products_to_cart()


@when('opens the shopping cart')
def step_impl(context):
    context.app.cart_page.open_cart()


@then('both products should be displayed in the cart')
def step_impl(context):
    context.app.cart_page.assert_cart_has_two_products()


@then('the correct price should be displayed for each product')
def step_impl(context):
    context.app.cart_page.assert_price_quantity_total_present()


@then('the correct quantity should be displayed for each product')
def step_impl(context):
    context.app.cart_page.assert_price_quantity_total_present()


@then('the correct total should be displayed for each product')
def step_impl(context):
    context.app.cart_page.assert_price_quantity_total_present()
