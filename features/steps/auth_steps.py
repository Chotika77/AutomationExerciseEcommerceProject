from behave import given, when, then


@then('the Login form should be displayed')
def step_impl(context):
    context.app.signup_login_page.assert_login_page_displayed()


@then('the "Login to your account" heading should be visible')
def step_impl(context):
    context.app.signup_login_page.assert_login_heading_visible()


@then('the Email and Password fields should be visible')
def step_impl(context):
    context.app.signup_login_page.assert_login_fields_visible()


@then('the Login button should be visible')
def step_impl(context):
    context.app.signup_login_page.assert_login_button_visible()



