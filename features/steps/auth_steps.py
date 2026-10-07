from behave import given, when, then


@given('a registered user account exists')
def step_impl(context):
    assert context.email, 'TEST_USER_EMAIL is not configured in .env'
    assert context.password, 'TEST_USER_PASSWORD is not configured in .env'


@given('the user is on the Signup Login page')
def step_impl(context):
    context.app.main_page.open(context.base_url)
    context.app.main_page.open_signup_login_page()
    context.app.signup_login_page.assert_login_page_displayed()


@when('the user enters valid login credentials')
def step_impl(context):
    context.app.signup_login_page.enter_email(context.email)
    context.app.signup_login_page.enter_password(context.password)


@when('logs in with valid credentials')
def step_impl(context):
    context.app.signup_login_page.enter_email(context.email)
    context.app.signup_login_page.enter_password(context.password)
    context.app.signup_login_page.click_login()


@when('clicks the Login button')
def step_impl(context):
    context.app.signup_login_page.click_login()


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


@then('the user should be logged in successfully')
def step_impl(context):
    context.app.signup_login_page.assert_logged_in()


@when('the user enters "{email}" and "{password}"')
def step_impl(context, email, password):
    context.app.signup_login_page.enter_email(email)
    context.app.signup_login_page.enter_password(password)


@then('the invalid login error message should be displayed')
def step_impl(context):
    context.app.signup_login_page.assert_invalid_login_error_message()


@given('the user is logged in')
def step_impl(context):
    # Navigate to signup/login page and perform login using configured test credentials
    context.app.main_page.open(context.base_url)
    context.app.main_page.open_signup_login_page()
    context.app.signup_login_page.log_in(context.email, context.password)
    context.app.signup_login_page.assert_logged_in()


@when('the user clicks the Logout button')
def step_impl(context):
    context.app.signup_login_page.click_logout()


@then('the user should be logged out')
def step_impl(context):
    # logout redirects to /login; reuse existing assertion
    context.app.signup_login_page.assert_login_page_displayed()


@then('the Signup Login page should be displayed')
def step_impl(context):
    context.app.signup_login_page.assert_login_page_displayed()
