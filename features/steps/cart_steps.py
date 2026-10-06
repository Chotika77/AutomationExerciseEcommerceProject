from behave import given, when, then


@given('the user opens a product details page')
def step_impl(context):
    context.app.products_page.open_product(context.base_url)


@when('the user sets the product quantity to "{quantity}"')
def step_impl(context, quantity):
    context.app.product_details_page.set_quantity(quantity)


@when('adds the product to the cart')
def step_impl(context):
    context.app.product_details_page.add_to_cart()


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


@then('the product quantity should be "{quantity}"')
def step_impl(context, quantity):
    context.app.cart_page.assert_product_quantity(quantity)
