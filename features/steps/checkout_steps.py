from behave import when, then


@when('the user proceeds to checkout')
def step_impl(context):
    context.app.checkout_page.proceed_to_checkout()


@then('the user should be prompted to register or log in')
def step_impl(context):
    context.app.checkout_page.assert_login_prompt_displayed()
