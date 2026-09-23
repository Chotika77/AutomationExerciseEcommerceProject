from behave import given, when, then


@given('the user opens the Automation Exercise website')
def step_impl(context):
    context.app.main_page.open(context.base_url)


@when('the user navigates to the Signup Login page')
def step_impl(context):
    context.app.main_page.open_signup_login_page()